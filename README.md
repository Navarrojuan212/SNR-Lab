# SNR-Lab
For scientific purpose
---

# Detalles Estadísticos — Glosario, justificación metodológica y caracterización de escenarios

> Documento de trabajo que consolida (a) la interpretación de cada columna de la Tabla 4.1 del manuscrito, (b) la justificación de la cadena estadística empleada con base en el árbol de decisión de Marusteri & Bacarea (2010), (c) la justificación del escalado robusto previo a las pruebas estadísticas y a los métodos de reducción de dimensión, y (d) la descripción física de cada escenario de medición. Sirve como insumo para alimentar Cap. 3 (escenarios), Cap. 4 (discusión) y el Anexo de métodos estadísticos del manuscrito en Overleaf.

---

## A. A qué evaluador(es) responde

| Evaluador | Punto | Qué pidió | Cómo lo cubre este documento |
|---|---|---|---|
| **E3** | #4 | "no se hizo descripción suficiente para determinar los escenarios indoor… condiciones de alcance y **movilidad del usuario**" | Caracterización por escenario (Bloque 4) + narrativa de tráfico humano en Sótano 1 (Bloque 5) |
| **E3** | #4 | "anexo que explique los **dos métodos** [estadísticos] utilizados" | Glosario (Bloque 1) + justificación de cadena Shapiro–Wilk → Kruskal–Wallis con árbol de decisión (Bloque 2) |
| **E3** | #5 | "no se explica el entorno y escenarios… no hay contundencia en la discusión" | Narrativa que conecta varianza observada con condiciones del entorno (Bloque 5) |
| **E1** | #4 | "condiciones de adquisición, comparabilidad entre escenarios" | Tabla de escenarios con condiciones físicas (Bloque 4) |
| **E2** | #2 | "variables controladas… formato de base de datos" | Documenta cada fila = ubicación; cada columna = estadístico (Bloque 1) |

Cruza con **Tema 2** (Cálculo SNR + análisis estadístico) y **Tema 7** (Descripción de escenarios) del documento [RespuestaSIRVENalos3Evaluadores.md](RespuestaSIRVENalos3Evaluadores.md).

---

## Bloque 1 — Glosario de columnas de la Tabla 4.1

Cada fila de la tabla corresponde a una **ubicación de medición** (`Lugar`). Las columnas reportan estadísticos descriptivos del SNR (en dB) calculados sobre las **N = 200** muestras adquiridas en ese punto.

> **Notación alineada con el manuscrito (Tabla 4.1):** se usan $\bar{x}$ (media muestral), $\tilde{x}$ (mediana), $\hat{x}$ (moda), $\sigma$ (desviación estándar muestral) y $\sigma^2$ (varianza muestral). El orden de columnas reproduce el del manuscrito.

| Columna | Símbolo | Definición | Cómo interpretarla |
|---|---|---|---|
| **Lugar** | — | Ubicación física donde se tomó la medida. | Identificador del escenario (Antena, Piso 1–5, Sótano 1–2, RF–VLC). |
| **$Q_1$** | $Q_1$ | Primer cuartil (percentil 25) en dB. | El 25 % de las muestras quedan por debajo de este valor. Marca el límite inferior de la caja del boxplot. |
| **$\bar{x}$** | $\bar{x}$ | Media muestral en dB. | Valor "promedio" del SNR. Sensible a outliers; no representa bien distribuciones asimétricas. |
| **$Q_3$** | $Q_3$ | Tercer cuartil (percentil 75) en dB. | El 75 % de las muestras quedan por debajo. Límite superior de la caja del boxplot. |
| **IQR** | $\text{IQR}=Q_3-Q_1$ | Rango intercuartílico en dB. | **Medida robusta de dispersión**: cuán "ancha" es la mitad central de los datos. IQR alto ⇒ alta variabilidad del enlace. |
| **↓ Atípico** | $\bar{x}-1.5\cdot\text{IQR}$ | Frontera inferior para considerar un valor atípico (en dB). | Cualquier muestra por debajo es candidata a outlier. *Variante de Tukey adoptada en este estudio: usa la media en lugar de $Q_1$.* |
| **↑ Atípico** | $\bar{x}+1.5\cdot\text{IQR}$ | Frontera superior para outliers (en dB). | Cualquier muestra por encima es candidata a outlier (misma variante). |
| **$\tilde{x}$** | $\tilde{x}$ | Mediana muestral en dB (percentil 50). | Valor central robusto. Si $\tilde{x}\ne\bar{x}$ la distribución es asimétrica. **Mejor descriptor central que la media** cuando hay outliers (caso de este estudio). |
| **$\hat{x}$** | $\hat{x}$ | Moda muestral en dB. | Valor de SNR más frecuente. Útil con datos discretizados; en muestras continuas conviene mirarla junto al histograma. |
| **$\sigma^2$** | $\sigma^2$ | Varianza muestral en dB². | **Termómetro de inestabilidad** del canal: mayor varianza ⇒ canal más perturbado. |
| **$\sigma$** | $\sigma$ | Desviación estándar muestral en dB. | Dispersión "promedio" alrededor de la media (raíz de la varianza). En dB indica cuán estable es el enlace. |

> **Nota sobre la fórmula de outliers:** la regla canónica de Tukey utiliza $Q_1-1.5\cdot\text{IQR}$ y $Q_3+1.5\cdot\text{IQR}$. En este estudio se adoptó la variante $\bar{x}\pm 1.5\cdot\text{IQR}$ (centrada en la media) por razones operativas. La diferencia es marginal cuando $\bar{x}\approx \tilde{x}$ (distribuciones casi simétricas) y se documenta explícitamente para que el lector pueda replicar los cálculos.

### Valores de la Tabla 4.1 (espejo del manuscrito)

> Réplica markdown de los valores actualmente en [`chapter4.tex`](Tesis-V4-overleaf/Tesis-ITM/chapter4.tex) (`tab:datos-estadisticos`). Sirve para verificación cruzada contra el manuscrito y contra los datos brutos en [`SNR Degradation Study/Data/`](../SNR%20Degradation%20Study/Data/). Los marcadores `↓` y `↑` que acompañan a las celdas $\bar{x}$ de Sótano 2 y RF–VLC señalan que esos escenarios son los extremos absolutos del estudio (mínimo y máximo, respectivamente).

| Lugar | $Q_1$ | $\bar{x}$ | $Q_3$ | IQR | ↓ Atípico | ↑ Atípico | $\tilde{x}$ | $\hat{x}$ | $\sigma^2$ | $\sigma$ |
|---|---|---|---|---|---|---|---|---|---|---|
| Piso 1   | 24.06 | 25.07     | 26.05 | 1.99 | 22.08 | 28.06 | 24.98 | 25.45 | 2.44  | 1.56 |
| Piso 2   | 19.70 | 20.34     | 21.00 | 1.30 | 18.38 | 22.29 | 20.28 | 20.17 | 0.86  | 0.93 |
| Piso 3   | 19.14 | 20.20     | 21.68 | 2.54 | 16.39 | 24.01 | 19.57 | 19.21 | 3.41  | 1.85 |
| Piso 4   | 21.03 | 21.93     | 22.63 | 1.60 | 19.52 | 24.33 | 21.92 | 21.15 | 2.35  | 1.53 |
| Piso 5   | 24.56 | 25.75     | 26.68 | 2.12 | 22.56 | 28.94 | 25.72 | 25.15 | 3.09  | 1.76 |
| Antena   | 28.62 | 29.14     | 29.71 | 1.09 | 27.51 | 30.78 | 28.98 | 28.62 | 0.45  | 0.67 |
| RF–VLC   | 36.62 | ↑ 36.90   | 37.15 | 0.53 | 36.10 | 37.69 | 36.81 | 36.62 | 0.23  | 0.48 |
| Sótano 1 |  7.88 | 11.50     | 11.82 | 3.94 |  5.60 | 17.41 |  8.56 |  8.26 | 34.77 | 5.90 |
| Sótano 2 |  4.61 | ↓ 4.93    |  5.18 | 0.57 |  4.07 |  5.78 |  4.93 |  4.57 | 0.12  | 0.34 |

> **Nota de verificación (2026-04-28):** los valores $Q_1$ y $\hat{x}$ de la fila RF–VLC (ambos `36.62`) corresponden a la corrección aplicada en su día sobre la versión PDF original, donde aparecían erróneamente como `36.02` (que es el **mínimo** de la serie, no el primer cuartil ni la moda). El resto de celdas se verificó contra los datos brutos de [`SNR Degradation Study/Data/`](../SNR%20Degradation%20Study/Data/) con el script [`_verify_stats.py`](_verify_stats.py); todas coinciden con `RF-VLC_SNR.xlsx` y los demás `.xlsx`/`.csv` por escenario. Esta tabla reproduce los mismos valores numéricos del manuscrito (`chapter4.tex`, `tab:datos-estadisticos`); aquí se presentan con dos cifras decimales uniformes para facilitar la lectura en markdown.

---

## Bloque 2 — Justificación de la cadena estadística (Shapiro–Wilk → Kruskal–Wallis)

> **Referencia metodológica:** Marusteri, M., & Bacarea, V. (2010). *Comparing groups for statistical differences: how to choose the right statistical test?* Biochemia Medica, 20(1), 15–32. El árbol de decisión de la Figura 4 de este artículo guía la elección del test correcto en función del número de muestras, normalidad y emparejamiento. Archivo local: [Marusteri_M_Comparing_groups_for_statistical_differences.pdf](Marusteri_M_Comparing_groups_for_statistical_differences.pdf).

### Camino de decisión seguido en este estudio

![Árbol de decisión de Marusteri & Bacarea (2010)](Estudio_Estadistico/Study_images/estudio.png)

### Paso 1 — Selección de la rama "Three or more sample"

El estudio compara **9 ubicaciones independientes**: Antena, Piso 1, Piso 2, Piso 3, Piso 4, Piso 5, Sótano 1, Sótano 2 y el banco RF–VLC. Como $k=9>2$, se ingresa por la rama "Three or more sample" del árbol de decisión.

### Paso 2 — Prueba de normalidad: Shapiro–Wilk

**Hipótesis:**
- $H_0$: la SNR proviene de una distribución normal.
- $H_1$: la SNR no proviene de una distribución normal.

**Resultado obtenido:**

| Estadístico W | p-value | Decisión ($\alpha=0.05$) |
|---|---|---|
| 0.928 | $\approx 0$ (p ≪ 0.05) | **Se rechaza $H_0$** |

**Interpretación.** La SNR agregada **no sigue una distribución gaussiana**, lo que descarta el uso de pruebas paramétricas (ANOVA, t-test). Esto es coherente con la presencia de outliers documentados en las columnas ↓/↑ Atípico de la Tabla 4.1 y con la asimetría observada entre $\bar{x}$ y $\tilde{x}$ en varias ubicaciones (notablemente Sótano 1: $\bar{x}=11.5$ vs. $\tilde{x}=8.56$).

### Paso 3 — Verificación de no emparejamiento

Las muestras **no son pareadas** porque cada ubicación corresponde a un punto espacial distinto, sin correspondencia uno-a-uno entre observaciones de grupos diferentes. No existe el supuesto de "el mismo sujeto medido en dos condiciones" que justificaría una prueba pareada (Friedman, repeated measures ANOVA).

### Paso 4 — Selección de Kruskal–Wallis

Combinando **k ≥ 3**, **no normalidad** y **no pareamiento**, el árbol de Marusteri & Bacarea conduce inequívocamente al **test de Kruskal–Wallis** — la alternativa no paramétrica al ANOVA de una vía, que compara medianas de $k$ grupos independientes.

**Hipótesis:**
- $H_0$: las medianas de SNR de las 9 ubicaciones son iguales.
- $H_1$: al menos una mediana difiere.

**Resultado obtenido:**

| Estadístico H | p-value | Decisión ($\alpha=0.05$) |
|---|---|---|
| 1403.11 | $1.20\times 10^{-297}$ | **Se rechaza $H_0$** |

**Interpretación.** Existen **diferencias estadísticamente significativas** entre al menos dos ubicaciones. El valor de $H$ extremadamente alto y un p-value prácticamente nulo confirman que el escenario de medición tiene un efecto medible sobre la SNR — **validación cuantitativa** de que la degradación reportada no es ruido aleatorio.

### Resumen para el manuscrito

> *"La selección de la prueba estadística siguió el árbol de decisión de Marusteri & Bacarea (2010, Fig. 4). Como (i) se comparan $k=9>2$ grupos independientes, (ii) la prueba de Shapiro–Wilk rechaza la hipótesis de normalidad sobre la SNR ($W=0.928$, $p\ll 0.05$) y (iii) las muestras no son pareadas (cada ubicación es un punto espacial distinto), la prueba apropiada es **Kruskal–Wallis**, alternativa no paramétrica al ANOVA de una vía. El test arrojó $H=1403.11$ y $p=1.20\times 10^{-297}$, rechazando la hipótesis de igualdad de medianas y confirmando que la ubicación tiene un efecto significativo sobre la SNR."*

---

## Bloque 3 — Justificación del escalado robusto (`RobustScaler`)

Antes de aplicar Shapiro–Wilk y Kruskal–Wallis, así como los métodos de reducción de dimensión (PCA, LDA, t-SNE), se realiza un escalado de las columnas `SNR` y `Time_Index` mediante `RobustScaler` (de `sklearn.preprocessing`).

### ¿Qué es `RobustScaler`?

Aplica la transformación:

$$x'_i = \frac{x_i - \tilde{x}}{\text{IQR}}$$

es decir, centra los datos en la **mediana** y los escala por el **rango intercuartílico**, en lugar de usar la media y la desviación estándar (como `StandardScaler`) o el mínimo/máximo (como `MinMaxScaler`).

### Comparación de scalers para este caso

| Scaler | Centrado | Escala | Sensibilidad a outliers | Apto para SNR de este estudio |
|---|---|---|---|---|
| `StandardScaler` | $\bar{x}$ | $\sigma$ | **Alta** (media y desv. estándar son sensibles) | ❌ Sesgado por outliers (Sótano 1 tiene $\sigma=5.9$ dB) |
| `MinMaxScaler` | $x_{\min}$ | $x_{\max}-x_{\min}$ | **Muy alta** (un solo valor extremo deforma toda la escala) | ❌ Aún más sensible |
| **`RobustScaler`** | $\tilde{x}$ | $\text{IQR}$ | **Baja** (mediana e IQR son estadísticos robustos) | ✅ **Adecuado** |

### Por qué `RobustScaler` es la opción correcta aquí

Tres razones, todas verificables en los propios datos del estudio:

1. **Los datos no son normales** (Shapiro–Wilk lo rechaza con $p\ll 0.05$). El uso de $\bar{x}$ y $\sigma$ —estadísticos óptimos para distribuciones gaussianas— produciría un centrado y una escala distorsionados.
2. **Existen outliers documentados** en cada ubicación (columnas ↓/↑ Atípico de la Tabla 4.1). En particular, Sótano 1 tiene $\sigma^2=34.77$ dB², casi **290 veces** la varianza del Sótano 2 (0.12 dB²). Un `StandardScaler` ajustado a estos datos quedaría dominado por la dispersión de Sótano 1 y comprimiría los demás escenarios.
3. **Las escalas de las dos features son disímiles:** SNR ∈ [4, 38] dB y `Time_Index` ∈ [0, 20] s. Sin escalado, PCA/t-SNE asignarían pesos arbitrarios; con `RobustScaler` ambas features quedan en rangos comparables sin que los outliers de SNR contaminen el escalado de `Time_Index`.

### Resumen para el manuscrito

> *"Previo a las pruebas estadísticas y a la reducción de dimensión, las features `SNR` y `Time_Index` se escalaron con `RobustScaler` (Pedregosa et al., 2011), que centra los datos en la mediana y los normaliza por el IQR. Esta elección obedece a tres razones: (i) la no normalidad de la SNR confirmada por Shapiro–Wilk descarta el uso de estadísticos basados en media/desviación estándar; (ii) la presencia de outliers severos en escenarios de alta movilidad humana —notablemente Sótano 1, con $\sigma^2=34.77$ dB$^2$— dominaría un escalado tipo `StandardScaler`; (iii) la disparidad de unidades entre SNR (dB) y tiempo (s) requiere normalización para que los métodos de reducción de dimensión (PCA, LDA, t-SNE) no asignen pesos espurios a una de las dos."*

---

## Bloque 4 — Caracterización física de cada escenario

### Marco general

Las medidas se realizaron en una **edificación universitaria** del **ITM, Campus Fraternidad (Medellín)** de 6 pisos + 2 sótanos: el 6º piso corresponde a la **terraza propiamente dicha** (no se utiliza en este estudio); el estudio se concentra en los **5 pisos habitables** (Pisos 1–5) y los **2 sótanos** (–1 y –2). El receptor de cada sesión es un **AIRSPY** que adquiere **N = 200 muestras** por escenario con separación temporal de 0.1 s (≈ 22 s de adquisición continua).

### Captura de la señal de referencia (antena Yagi)

La **señal de referencia** a 103.5 MHz (banda FM comercial) se captura mediante una **antena Yagi outdoor al aire libre ubicada en el Piso 4**, no en la terraza del 6º piso. La elección del Piso 4 obedece a una razón estructural concreta:

> **El Piso 4 dispone de una zona al aire libre que queda físicamente justo encima de los sótanos.** Esto permite **tender un cable** desde la salida de la Yagi outdoor hasta el **Sótano 2 (–2)**, sin recurrir a multi-saltos ni a re-radiadores intermedios.

Esta arquitectura es **deliberada** y forma parte del diseño experimental: emula un **escenario hostil outdoor → indoor profundo** en el que la señal se capta en aire libre y luego se transporta físicamente hasta el punto más degradado del edificio. La antena Yagi actúa, por tanto, simultáneamente como (i) **línea base outdoor** del estudio estadístico y (ii) **fuente de entrada del sistema híbrido propuesto**, que la procesa antes de redistribuirla.

### Protocolo de movilidad del receptor

> **Receptor estático en el "punto óptimo" de cada nivel.** En cada piso/sótano se realizó un barrido manual previo y, una vez identificado el punto donde la señal se capta con mejor calidad (mejor SNR observada), el receptor se **fijó en ese punto** durante los ≈ 22 s de adquisición. No se trata, por tanto, de una caracterización aleatoria del piso, sino de la **mejor SNR alcanzable** en ese nivel — lo cual hace la comparación entre niveles más conservadora (los pisos más bajos / sótanos no están penalizados por una mala selección de punto).

### Cronograma de adquisición (sesiones)

Las medidas se realizaron en **cuatro sesiones distintas** entre marzo y octubre de 2024. Las fechas se extrajeron directamente de la columna `Timestamp` de los archivos `.xlsx`/`.csv` originales:

| Sesión | Fecha | Hora local | Día semana | Escenarios cubiertos |
|---|---|---|---|---|
| 1 | **2024-03-22** | 15:47 – 16:09 | viernes (PM) | Pisos 1–5 (en este orden temporal: P4 → P3 → P2 → P1 → P5) |
| 2 | **2024-04-05** | 11:28 – 11:36 | **viernes (AM, hora pico de clases)** | Sótano 1 (11:28) → Sótano 2 (11:36) |
| 3 | 2024-10-08 | 11:36 | martes | Antena Yagi outdoor (Piso 4) |
| 4 | 2024-10-22 | 16:53 | martes | Banco RF–VLC (laboratorio) |

> **Observación relevante para la discusión:** la sesión de los sótanos se hizo un **viernes a las 11:28 AM**, en plena hora de clases. Esto refuerza la narrativa de alto flujo humano en Sótano 1 (enfermería + ludoteca activas) frente a Sótano 2 (laboratorios con menos gente). Si se hubieran tomado en fin de semana o en horario nocturno, la varianza diferencial probablemente sería menor.

### Tabla de escenarios

| Ubicación | Nivel | Uso del espacio | Sesión | Movilidad / tráfico humano | Condición esperada del enlace RF |
|---|---|---|---|---|---|
| **Antena Yagi** | **Outdoor — zona al aire libre del Piso 4** (justo encima de los sótanos para permitir el cableado vertical hasta Sótano 2) | Captura de señal de referencia que alimenta el sistema híbrido | 3 | Estático, sin obstrucción humana, LoS al transmisor comercial | **Línea base outdoor** (alta SNR, baja varianza) |
| **Piso 5** | Indoor — superior | Aulas / oficinas | 1 | Receptor estático en punto óptimo del piso | Atenuación moderada por techo y muros |
| **Piso 4** | Indoor | Aulas (mismo nivel donde está la zona al aire libre con la Yagi outdoor; la medida indoor se hace **dentro del piso**, no afuera) | 1 | Receptor estático en punto óptimo del piso | Atenuación moderada |
| **Piso 3** | Indoor | Aulas | 1 | Receptor estático en punto óptimo | Atenuación + multitrayecto |
| **Piso 2** | Indoor | Aulas | 1 | Receptor estático en punto óptimo | Atenuación acumulada |
| **Piso 1** | Indoor — bajo | Aulas / áreas comunes | 1 | Receptor estático en punto óptimo | Mayor atenuación por estructura sobre el piso |
| **Sótano 1** | Subterráneo (–1) | **Enfermería + ludoteca** | 2 (vie 11:28 AM, hora pico) | **Alto y dinámico** — mayor flujo de personas en movimiento del edificio | Atenuación severa + **shadowing dinámico** por personas en movimiento ⇒ **alta varianza** |
| **Sótano 2** | Subterráneo (–2) | Laboratorios | 2 (vie 11:36 AM) | Bajo (poca gente) | Atenuación máxima por profundidad estructural, **pero varianza menor** que Sótano 1 al haber poco movimiento |
| **RF–VLC** | Laboratorio controlado | Banco de pruebas del sistema híbrido propuesto | 4 | Estático, condiciones controladas | Caso de validación del aporte de la arquitectura |

### Implicación para la comparabilidad entre sesiones

Las sesiones 3 y 4 (octubre) están separadas ~7 meses de la sesión 1 (marzo) y ~6 meses de la sesión 2 (abril). Para evitar que un evaluador atribuya las diferencias entre escenarios al **paso del tiempo** (variación atmosférica, posibles cambios en la potencia del transmisor comercial), conviene aclarar en el manuscrito que:

1. La **frecuencia de referencia** (103.5 MHz, emisora comercial estable) se controla con la captura outdoor de la antena Yagi, que actúa como **ancla**.
2. La comparación crítica del estudio (degradación piso a piso y entre sótanos) se hace dentro de la **misma sesión** (sesión 1 para pisos, sesión 2 para sótanos), por lo que las conclusiones de degradación intra-edificio no dependen de la ancla outdoor.
3. La validación del sistema híbrido (sesión 4) se hace en condiciones de laboratorio independientes y se compara contra la línea base de la antena (sesión 3), ambas tomadas en el mismo periodo (octubre).

### Alcance del estudio estadístico

> **El análisis estadístico se restringe estrictamente a los 9 escenarios reportados en la Tabla 4.1 del manuscrito**: Antena Yagi (Piso 4 outdoor), Pisos 1–5, Sótanos 1 y 2, y banco RF–VLC. **No se incluyen** otras mediciones que pudieran existir en versiones previas del repositorio (p. ej. "Floor 6" o "Terrace 6" del 6º piso/terraza), ya que no forman parte del alcance experimental documentado en la tesis. El notebook [SNRDegradationStudy.ipynb](../SNR%20Degradation%20Study/SNRDegradationStudy.ipynb) carga exactamente estos 9 archivos.

---

## Bloque 5 — Hallazgo clave: datos ↔ escenario (con valores reales de la Tabla 4.1)

> **El Sótano 1 presenta una varianza ~290× superior al Sótano 2**, a pesar de que Sótano 2 es el nivel más profundo del edificio.

### Valores reales medidos

| Métrica | Antena | Piso 1 | Sótano 1 | Sótano 2 | RF–VLC |
|---|---|---|---|---|---|
| $\bar{x}$ (dB) | 29.14 | 25.07 | 11.50 | **4.93** ↓ | **36.90** ↑ |
| $\tilde{x}$ (dB) | 28.98 | 24.98 | **8.56** | 4.93 | 36.81 |
| $\sigma^2$ (dB²) | 0.45 | 2.44 | **34.77** | 0.12 | 0.23 |
| $\sigma$ (dB) | 0.67 | 1.56 | **5.90** | 0.34 | 0.48 |
| IQR (dB) | 1.09 | 1.99 | **3.94** | 0.57 | 0.53 |

**Comparación clave Sótano 1 vs Sótano 2:**

| Métrica | Sótano 1 | Sótano 2 | Ratio |
|---|---|---|---|
| Varianza $\sigma^2$ | 34.77 dB² | 0.12 dB² | **~290×** |
| Desv. estándar $\sigma$ | 5.90 dB | 0.34 dB | ~17× |
| IQR | 3.94 dB | 0.57 dB | ~7× |
| Asimetría ($\bar{x}-\tilde{x}$) | 2.94 dB | 0.00 dB | Sótano 1 fuertemente asimétrico |

### Explicación física

- **Sótano 1** alberga la **enfermería y la ludoteca** del campus, lo que lo convierte en el área con **mayor flujo de personas en movimiento** del edificio durante una jornada típica. El cuerpo humano es absorbente y dispersor en banda VHF (≈103.5 MHz, $\lambda\approx 2.9$ m), por lo que el tránsito constante introduce **shadowing dinámico** y multitrayecto variable que se manifiesta directamente en una **varianza extrema** (34.77 dB²) y en una marcada **asimetría** (la mediana 8.56 dB queda 2.94 dB por debajo de la media 11.5 dB, evidencia de una cola superior larga inducida por momentos de despejes momentáneos del LoS).
- **Sótano 2**, aun siendo el nivel más bajo (mayor atenuación estructural por profundidad), está dedicado a **laboratorios** con baja ocupación: el canal es notablemente más estable temporalmente, lo que se refleja en una varianza prácticamente nula (0.12 dB²). Su SNR media es la más baja del edificio (4.93 dB), pero el canal es **predecible**.

### Lectura formal (sugerida para el manuscrito, Cap. 4)

> *"La varianza observada en el Sótano 1 ($\sigma^2 = 34.77$ dB$^2$, IQR $= 3.94$ dB) excede en aproximadamente **290 veces** la del Sótano 2 ($\sigma^2 = 0.12$ dB$^2$), escenario más profundo pero con menor tránsito de personas. La asimetría del Sótano 1 ($\bar{x}-\tilde{x}=2.94$ dB) refuerza esta lectura: existe una cola larga hacia valores altos de SNR que se atribuye a despejes momentáneos del trayecto cuando no hay personas interpuestas. Este resultado es coherente con un régimen de **shadowing dinámico inducido por la movilidad humana**, característico de espacios de uso clínico-recreativo (enfermería y ludoteca), y refuerza que el comportamiento del canal RF indoor a 103.5 MHz no se explica únicamente por la cota de profundidad o la atenuación estructural, sino también por la **dinámica de ocupación** del entorno. Esta observación se enmarca en el modelo de shadowing log-normal del canal RF descrito en la Sec. 2.4 y aporta evidencia empírica al análisis de sensibilidad solicitado por el evaluador 3 sin requerir una corrida experimental adicional."*

---

## Bloque 6 — Dónde se propone pegar este contenido en el manuscrito

Cinco ubicaciones complementarias (no excluyentes), alineadas con la nueva estructura de [new.md](new.md):

| # | Archivo destino | Qué se agrega | Para qué sirve |
|---|---|---|---|
| 1 | **Cap. 3 — sección 3.2.1 "Escenarios indoor"** | Tabla del Bloque 4 (caracterización física) + texto narrativo del Bloque 5 | Responde E3 #4 directamente |
| 2 | **Anexo nuevo "Métodos estadísticos"** (Tema 2 del consolidado) | Glosario completo (Bloque 1) + árbol de decisión y justificación (Bloque 2) + justificación del escalado (Bloque 3) | Responde E3 #4 ("anexo que explique los métodos") y E1 #4 |
| 3 | **Cap. 4 — discusión** (responde a E3 #5) | Lectura formal del Bloque 5 (Sótano 1 vs. Sótano 2) | Da la "contundencia" que E3 reclama; aporta análisis de sensibilidad sin nueva experimentación |
| 4 | **[RespuestaSIRVENalos3Evaluadores.md](RespuestaSIRVENalos3Evaluadores.md) — Tema 7** | Tabla del Bloque 4 como entregable | Cierra el punto en la respuesta consolidada |
| 5 | **[SNRDegradationStudy.ipynb](../SNR%20Degradation%20Study/SNRDegradationStudy.ipynb)** (opcional) | Celda markdown nueva tras la tabla de estadísticas con el glosario del Bloque 1 + nota sobre `RobustScaler` y árbol de decisión | Hace el notebook autocontenido para el evaluador |

---

## Bloque 7 — Estado de los datos a confirmar

Para no inventar números al redactar la versión final del manuscrito:

1. ~~**Sótano 1 vs Sótano 2 — valores de varianza/IQR**.~~ ✅ Resueltos: Sótano 1 $\sigma^2=34.77$, IQR=3.94; Sótano 2 $\sigma^2=0.12$, IQR=0.57 (Tabla 4.1).
2. ~~**Antena outdoor**: ¿estaba en azotea/terraza, o cerca de una ventana?~~ ✅ Resuelto: **Antena Yagi al aire libre desde el Piso 4**, apuntada al transmisor. La señal capturada alimenta el sistema híbrido propuesto.
3. ~~**Movilidad del Rx en cada piso**~~. ✅ Resuelto: **estático en el punto óptimo** de cada nivel (selección manual previa de la mejor recepción, luego receptor fijo durante los ~22 s de adquisición).
4. ~~**Hora del día / día de la semana** de la sesión en Sótano 1~~. ✅ Resuelto a partir de los timestamps de los CSV: **Sótanos = viernes 5-Abr-2024, 11:28 AM** (hora pico de clases) → refuerza la narrativa de tráfico humano. Pisos = viernes 22-Mar-2024 PM. Antena = martes 8-Oct-2024. RF–VLC = martes 22-Oct-2024 PM.
5. **Iluminación ambiente** en sótanos. 🟡 **Pendiente**: Juan tomará las medidas con luxómetro **esta semana** (relevante para E3 #5 si se discute interferencia de luminarias en el caso RF–VLC).

---

## Referencias citadas en este documento

- **Marusteri, M., & Bacarea, V. (2010).** Comparing groups for statistical differences: how to choose the right statistical test? *Biochemia Medica*, 20(1), 15–32. [Marusteri_M_Comparing_groups_for_statistical_differences.pdf](Marusteri_M_Comparing_groups_for_statistical_differences.pdf).
- **Pedregosa, F. et al. (2011).** Scikit-learn: Machine Learning in Python. *JMLR*, 12, 2825–2830 (sección sobre `RobustScaler`).
- **Shapiro, S. S., & Wilk, M. B. (1965).** An analysis of variance test for normality (complete samples). *Biometrika*, 52(3/4), 591–611.
- **Kruskal, W. H., & Wallis, W. A. (1952).** Use of ranks in one-criterion variance analysis. *JASA*, 47(260), 583–621.

---

## Próximos pasos sugeridos

1. **Decidir con Juan** las 4 aclaraciones pendientes del Bloque 7.
2. **Migrar contenido** a las cinco ubicaciones del Bloque 6 (Cap. 3, Cap. 4, Anexo, respuesta consolidada y notebook) en Overleaf.
3. **Actualizar [Avance.md](Avance.md)** marcando los temas E3 #4, E3 #5, E1 #4 y E2 #2 como 🟡 en progreso.
4. **Citar Marusteri & Bacarea (2010) y Pedregosa et al. (2011)** en `references.bib` si aún no están.
