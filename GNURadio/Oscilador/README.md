# GNU Radio — `oscilador.py`

> Flowgraph **standalone** que implementa únicamente el **oscilador local (LO)** del sistema híbrido RF–VLC: emite una portadora continua (CW) a **142 MHz** desde una USRP NI 2900/2901, lista para alimentar la entrada LO del **mezclador AD831**.

> [!NOTE]
> En el manuscrito de tesis (Sec. 3.1.4) este bloque LO aparece integrado dentro del flowgraph principal `TxRx_FM.py`, gestionado por la "segunda USRP". Este script lo aísla como un programa autónomo y se mantiene con el nombre **`oscilador.py`** que es como está en disco.

---

## Rol dentro del sistema híbrido

El sistema híbrido necesita **dos frecuencias simultáneas** en la entrada del mezclador AD831:

1. La **señal re-transmitida a 140 MHz** (proveniente de [`../Rx_TxFM.py`](../Rx_TxFM.py), USRP-A).
2. El **oscilador local a 142 MHz** (este script, USRP-B).

La diferencia $|f_{LO}-f_{Tx}|=|142-140|=\mathbf{2\ MHz}$ es la frecuencia intermedia (FI) que viaja por el canal óptico (LED → fotodetector ThorLabs).

> [!TIP]
> Aunque `Rx_TxFM.py` ya contiene un sink configurado para generar la LO, **lanzar `oscilador.py` por separado** permite (i) controlar la LO desde una GUI independiente sin reiniciar todo el flowgraph principal, (ii) usar una USRP distinta físicamente dedicada al LO, y (iii) facilitar el debug del enlace RF–VLC variando solo $f_{LO}$ y $g_{ol}$ sin tocar la cadena de captura/retransmisión.

---

## Variables del flowgraph

| Variable | Valor por defecto | Rango (slider) | Significado |
|---|---:|:---:|---|
| `fol` | **142 MHz** | 80 – 480 MHz, paso 0.1 MHz | Frecuencia del oscilador local entregada al mezclador AD831. |
| `gol` | **40 dB** | 0 – 80 dB, paso 1 dB | Ganancia del SDR-Tx que genera la LO. |
| `samp_rate` | **48 kHz** | — | Sample rate base. |
| `f_factor` | **40** | — | Multiplicador del sample rate (presente por consistencia con el flowgraph principal). |

> [!IMPORTANT]
> El manuscrito (Tabla 3.3) reporta `gol = 45 dB` como valor operativo. Este script viene con un **valor por defecto de 40 dB** que se ajusta en vivo desde el slider. Eleva la ganancia hasta el rango operativo (≈ 45 dB) verificando con un analizador de espectro (TinySA) el nivel de potencia que llega al puerto LO del AD831 — debe estar dentro del rango lineal del mezclador.

---

## Hardware

| Bloque | Detalle |
|---|---|
| **USRP** | NI 2900/2901, serial **`30B5874`** declarado en el código. |
| **Antena / puerto** | Salida `TX/RX`. |
| **Sample format** | `fc32` (complejo float32). |

> [!CAUTION]
> Si tu USRP tiene un serial distinto al declarado, edita la línea `serial=30B5874` en el `__init__` antes de lanzar el script, o usa `uhd_find_devices` para listar las USRP disponibles.

---

## Cadena de procesamiento

Es trivial — el script no hace mezcla ni filtrado, solo emite una constante compleja que la USRP convierte en una **portadora pura (CW)** a la frecuencia configurada:

```
Const Source (CW, amplitud 1)
        │  fc32
        ▼
USRP Sink (30B5874)
  center_freq = fol = 142 MHz
  gain        = gol = 40 dB (ajustable)
        │
        ▼
Salida TX/RX  ──►  Mezclador AD831 (entrada LO)
```

---

## Cómo ejecutar

```bash
# Requisitos: GNU Radio 3.10.4.0 + UHD + PyQt5
python3 oscilador.py
```

Se abrirá una ventana Qt con dos sliders:

- **Frecuencia de oscilador local** → ajusta `fol` en vivo (80–480 MHz)
- **Ganancia oscilador local** → ajusta `gol` en vivo (0–80 dB)

Y dos pestañas vacías (`Spectrum RF Input` / `Spectrum RF Output`) que quedaron del esqueleto generado por GNU Radio Companion pero **no se usan en este script**, ya que el oscilador no procesa señal entrante ni reporta espectro propio.

> [!TIP]
> Para verificar que la portadora a 142 MHz está siendo emitida correctamente, conecta la salida `TX/RX` a un **TinySA** (analizador de espectro portátil) o a un segundo SDR en modo Rx centrado en 142 MHz. Debe verse un pico estrecho en $f_{LO}$ con piso de ruido limpio alrededor.

---

## Conexión con el resto del repositorio

| Recurso | Relación |
|---|---|
| [`../Rx_TxFM.py`](../Rx_TxFM.py) | Flowgraph principal. Lánzalo en paralelo con este script para tener el sistema híbrido completo (Rx FM + retransmisión a 140 MHz + LO a 142 MHz). |
| [`../../Maestria_ok.pdf`](../../Maestria_ok.pdf) | Manuscrito de la tesis. **Sec. 3.1.2** y **Tabla 3.1** describen el rol de la USRP como oscilador local; **Sec. 3.1.5** justifica la elección de $f_{LO}=142$ MHz. |
