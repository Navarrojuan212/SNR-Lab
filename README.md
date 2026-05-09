# SNR-Lab

> Repositorio del estudio de **degradación SNR** y del **sistema híbrido RF–VLC** desarrollado para la tesis de maestría *"Comunicación híbrida radio-óptica para mejorar los sistemas de telecomunicaciones indoor"* (ITM, Campus Fraternidad, Medellín). Caracteriza el SNR a 103.5 MHz en **9 escenarios** (Antena Yagi outdoor, Pisos 1–5, Sótanos 1–2 y banco RF–VLC) y respalda estadísticamente la **Tabla 4.1** del manuscrito.

## Mapa del repositorio

| Carpeta / archivo | Contenido | Empieza por aquí |
|---|---|---|
| [Data/](Data/) | Datos brutos de SNR — 9 archivos `.xlsx` / `.csv`, 200 muestras por escenario. | Solo si quieres los datos crudos. |
| [Estudio_Estadistico/](Estudio_Estadistico/) | Notebook reproducible + análisis estadístico (Shapiro–Wilk, Kruskal–Wallis), figuras y glosario. | **[Estudio_Estadistico/README.md](Estudio_Estadistico/README.md)** — lectura completa del estudio con bloques de código listos para Jupyter/Colab. |
| [GNURadio/](GNURadio/) | Flowgraph principal `Rx_TxFM.py`: Rx FM 103.5 MHz + retransmisión a 140 MHz + LO. | **[GNURadio/README.md](GNURadio/README.md)** — variables, cadena de procesamiento y cómo ejecutar. |
| [GNURadio/Oscilador/](GNURadio/Oscilador/) | Flowgraph standalone `oscilador.py`: oscilador local CW a 142 MHz. | **[GNURadio/Oscilador/README.md](GNURadio/Oscilador/README.md)** |

## ¿Qué busco?

- **Reproducir el análisis estadístico (figuras + tests)** → [Estudio_Estadistico/README.md](Estudio_Estadistico/README.md) o abrir directamente [Estudio_Estadistico/SNRDegradationStudy.ipynb](Estudio_Estadistico/SNRDegradationStudy.ipynb).
- **Entender la cadena SDR / GNU Radio del sistema híbrido** → [GNURadio/README.md](GNURadio/README.md).
- **Acceder a los datos crudos** → [Data/](Data/) (también se cargan automáticamente desde GitHub `raw` en el notebook, sin clonar).
