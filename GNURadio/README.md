# GNU Radio — `Rx_TxFM.py`

> Flowgraph principal que implementa la cadena de procesamiento digital del **sistema híbrido RF–VLC** propuesto en la tesis. Captura la portadora **FM comercial a 103.5 MHz** desde la antena Yagi outdoor, la **re-transmite a 140 MHz** y, en conjunto con el oscilador local de 142 MHz, produce la **frecuencia intermedia de 2 MHz** que viaja por el canal óptico (LED → fotodetector ThorLabs).

> [!NOTE]
> En el manuscrito de tesis (Sec. 3.1.4 y Tabla 3.3) este flowgraph aparece referenciado como `TxRx_FM.py`. En el repositorio se mantiene con el nombre **`Rx_TxFM.py`** que es como está en disco; ambos nombres se refieren al mismo programa.

---

## Rol dentro del sistema híbrido

El flowgraph orquesta dos USRP **NI 2900/2901** simultáneamente:

| USRP | Serial | Rol |
|---|---|---|
| **USRP-A** (Rx/Tx FM) | `30C2C26` | Captura la portadora a **103.5 MHz** desde la antena Yagi outdoor **y** la re-transmite a **140 MHz** al mezclador AD831. |
| **USRP-B** (LO) | `30B584D` | Genera el **oscilador local a 142 MHz** que alimenta al mismo mezclador AD831 para producir la frecuencia intermedia. |

> [!TIP]
> El oscilador local también puede ejecutarse de forma independiente con [`Oscilador/oscilador.py`](Oscilador/oscilador.py) — útil cuando se prefiere desacoplar el control de la LO del flowgraph principal en un proceso separado.

La salida de la mezcla genera dos componentes en frecuencia:

- **Suma:** $f_{LO}+f_{Tx}=142+140=\mathbf{282\ MHz}$ — eliminada por filtrado pasa-bajos posterior.
- **Diferencia:** $|f_{LO}-f_{Tx}|=|142-140|=\mathbf{2\ MHz}$ — **frecuencia intermedia útil** que modula el LED blanco.

> [!IMPORTANT]
> La elección de **2 MHz** no es arbitraria: el LED blanco con fósforo amarillo utilizado tiene una respuesta en frecuencia tipo pasa-bajos de primer orden con ancho de banda útil (−3 dB) en el orden de **2 MHz**, dominado por la lenta dinámica del fósforo. Las frecuencias 140 y 142 MHz se eligieron porque caen dentro del rango plano de las USRP NI 2900/2901 (70 MHz – 6 GHz), están alejadas de las bandas comerciales activas en Medellín (FM hasta 108 MHz, aeronáutica 108–137 MHz, VHF TV/radioaficionados desde 174 MHz), y la suma $f_{LO}+f_{Tx}=282$ MHz queda lo suficientemente alejada para ser eliminada por filtrado posterior sin diseño adicional.

---

## Variables del flowgraph (Tabla 3.3 del manuscrito)

| Variable | Valor | Unidad | Significado |
|---|---:|:---:|---|
| `Frec_Tomada` | **103.5** | MHz | Portadora de la emisora FM comercial captada por la Yagi outdoor. |
| `Frec_TxRx_A1` | **140** | MHz | Frecuencia de re-transmisión RF desde GNU Radio hacia el mezclador AD831. |
| `fol` | **142** | MHz | Oscilador local generado por la segunda USRP, entregado al mezclador AD831. |
| `samp_rate` | **48** | kHz | Sample rate base (audio). El SDR opera a `samp_rate × f_factor`. |
| `f_factor` | **40** | — | Multiplicador del sample rate → tasa efectiva del SDR: **1.92 MS/s**. |
| `Gain` | **78** | dB | Ganancia del SDR-Rx (USRP `30C2C26`). |
| `Gain_TxRx_A1` | **45** | dB | Ganancia del SDR-Tx que retransmite a 140 MHz. |
| `gol` | **45** | dB | Ganancia del oscilador local (USRP `30B584D`). |
| `vol` | **−2** | dB | Volumen de la salida de audio (rama de monitoreo FM). |

---

## Cadena de procesamiento

```
Antena Yagi outdoor (Piso 4)
        │  103.5 MHz
        ▼
USRP-A Source (30C2C26)
  center_freq = 103.5 MHz + 250 kHz   ← offset anti-DC
        │  fc32 @ 1.92 MS/s
        ▼
DC Blocker  ──►  Freq Xlating FIR (shift −250 kHz, low-pass)
        │
        ├──►  WBFM Receiver  →  LPF  →  ×vol  →  Audio Sink   (rama de monitoreo)
        │
        └──►  USRP-A Sink (30C2C26)  →  140 MHz  ──►  Mezclador AD831 ┐
                                                                       │
                                                                       ▼
                                                              componente diferencia
                                                                  = 2 MHz (FI)
                                                                       │
                                                                       ▼
                                                              Bias-T → LED blanco
```

Mientras tanto, en paralelo:

```
Const Source (CW)
        │
        ▼
USRP-B Sink (30B584D)
  center_freq = 142 MHz, gain = 45 dB
        │  142 MHz
        ▼
Mezclador AD831 (entrada LO)
```

---

## Detalles relevantes de implementación

### Offset anti-DC de +250 kHz

> [!WARNING]
> El mezclador IQ del front-end de las USRP no es perfecto y deja un residuo de continua (**DC leakage**) en el centro de la banda base. Sintonizar la captura exactamente en 103.5 MHz haría que la portadora coincidiera con ese residuo, contaminando la medida.

**Solución implementada:** se sintoniza el SDR a $f_c + 250\ \text{kHz} = 103{,}75\ \text{MHz}$ y se compensa por software con un `freq_xlating_fir_filter` configurado con un desplazamiento de **−250 kHz**. La señal regresa a su frecuencia central nominal y el artefacto DC queda fuera de la banda útil, sin requerir hardware adicional.

### Ganancias

| Etapa | Valor | Criterio |
|---|---:|---|
| **SDR-Rx** | 78 dB | Máximo valor que **no produce saturación del ADC** para el nivel de portadora FM comercial recibido en el campus ITM (verificado en tiempo real con `qtgui_freq_sink`). |
| **SDR-Tx** | 45 dB | Nivel adecuado para alimentar al **mezclador AD831 dentro de su rango lineal** (hoja de datos). |
| **Oscilador local** | 45 dB | Nivel suficiente en la entrada LO del AD831 para mezcla efectiva. |
| **LNA** (Tx y Rx) | 30 dB | Especificación del fabricante; compensa pérdidas acumuladas por mezcladores y conectorización. |

### Rama de monitoreo FM

El flowgraph incluye una **rama paralela de demodulación WBFM** (`analog.wfm_rcv` → low-pass → audio sink) que permite **escuchar en tiempo real la emisora FM** capturada. Sirve como verificación cualitativa de que la portadora a 103.5 MHz está siendo recibida correctamente antes de pasar al procesamiento óptico.

---

## Cómo ejecutar

> [!CAUTION]
> Antes de lanzar, asegúrate de que **ambas USRP estén conectadas y reconocidas** (`uhd_find_devices`) y que los **seriales** declarados en el código (`30C2C26` y `30B584D`) coincidan con tu hardware. Si no, edita los `serial=` en el `__init__` o usa `uhd_image_loader` para verificar.

```bash
# Requisitos: GNU Radio 3.10.5.1 + UHD + PyQt5
python3 Rx_TxFM.py
```

Se abrirá una ventana Qt con sliders para ajustar en vivo:

- `Frecuencia Rx Radio` → mueve `Frec_Tomada` (rango 80–480 MHz, paso 0.1 MHz)
- `Frecuencia Tx` → mueve `Frec_TxRx_A1` (rango 80–480 MHz)
- `Frecuencia de oscilador local` → mueve `fol` (rango 80–480 MHz)
- `Ganancia RF Radio` / `Ganancia Tx` / `Ganancia oscilador local` (0–80 dB)
- `Volumen` (audio FM, −40 a 10 dB)

Las pestañas **`Spectrum RF Input`** y **`Spectrum RF Output`** muestran el espectro centrado en `Frec_Tomada` y `Frec_TxRx_A1` respectivamente, con `qtgui.freq_sink_c` en ventana Blackman-Harris (FFT 1024).

---

## Conexión con el resto del repositorio

| Recurso | Relación |
|---|---|
| [`Oscilador/oscilador.py`](Oscilador/oscilador.py) | Versión **standalone** del bloque LO (solo USRP-B a 142 MHz). Usa este script si prefieres ejecutar el oscilador en un proceso separado. |
| [`../Data/`](../Data/) | Datos de SNR (`.xlsx` / `.csv`) capturados por el receptor **AIRSPY** centrado en `Frec_TxRx_A1 = 140 MHz` — son los archivos analizados estadísticamente en [`../Estudio_Estadistico/`](../Estudio_Estadistico/). |
| [`../Maestria_ok.pdf`](../Maestria_ok.pdf) | Manuscrito de la tesis. Sec. 3.1.2–3.1.5 describe la arquitectura del Tx/Rx híbrido; **Tabla 3.3** lista las variables del flowgraph; **Tabla 3.4** consolida los parámetros maestros del sistema. |
