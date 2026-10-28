# Intención de abandono en estudiantes de pregrado de La Paz

Autor del proyecto: Jhonathan Holguin Rivera. Especialización en Analítica de Datos, CUN.

## Objetivo del ACA 1
Caracterizar las condiciones sociodemográficas, socioeconómicas y de experiencia académica mediante preparación y EDA de la encuesta pública de 2025. Se mantienen tres dimensiones ordinales de intención de abandono. No se mide deserción efectiva ni se entrena un predictor.

## Cómo reproducir
1. Abrir `notebooks/ACA1_Holguin_Rivera.ipynb` en Colab o Jupyter.
2. Descargar el ZIP original de https://data.mendeley.com/datasets/kxgrpy8sfp/2. En Colab, cargarlo cuando la celda de adquisición lo solicite. En ejecución local, guardarlo como `data/raw/student_retention_dataset_lapaz_2025.zip`.
3. Ejecutar todas las celdas en orden desde un entorno limpio. Los resultados se crean en `results/`. Fuera de Colab, instalar `requirements.txt` y usar Jupyter o `python ejecutar_aca1.py`.
4. Verificar que el SHA-256 coincida con la ficha. Las aserciones detienen la ejecución si la fuente cambia.

## Entorno
La ejecución local se hizo en Python 3.12.14, CPU, sin GPU. Versiones en `requirements.txt` y `results/environment.json`. Semilla fija 20261024. El código se ejecutó secuencialmente en Python; no se ha abierto todavía en una sesión real de Colab. El archivo original se requiere para regenerar auditoría y análisis completos.

## Datos y resultados
La copia procesada se guarda en `data/processed/`. Los diccionarios, ficha, controles ETL, correlaciones, VIF, subgrupos, sensibilidad y protocolo están en `results/tables/`. Las figuras se entregan en PNG de 300 dpi y SVG. Las cifras del documento deben provenir de estas salidas. `results/resumen_ejecucion.json` resume los controles.

## Límites
Muestra de encuesta, sin seguimiento de matrícula. Las puntuaciones 4–5 son un resumen exploratorio y no un umbral validado. Pearson y VIF sobre puntuaciones ordinales son diagnósticos de sensibilidad. Las pruebas confirmatorias están previstas para fases posteriores. La copia procesada reduce detalle personal, pero no cuenta con certificación formal de anonimización. No publicar el original ni datos individuales de grupos pequeños.

## Estado de entrega
Paquete local del ACA 1. Pendientes: confirmar fecha de descarga, revisión y comprensión del autor, ejecutar en Colab, crear repositorio público y publicar release con etiqueta v0.1. Este paquete no crea esa release ni contiene enlaces públicos inventados. El PDF del documento de grado se consolida en una etapa posterior.

## Licencias y citas
Datos: Correa, C. (2026), Mendeley Data V2, https://doi.org/10.17632/kxgrpy8sfp.2, CC BY 4.0. Código propio: MIT. Consultar `DATA_LICENSE.md` y `DECLARACION_IA.md`.

## Referencias técnicas
SciPy, correlación de Spearman: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html
Statsmodels, definición del VIF: https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html
El VIF se implementa con mínimos cuadrados mediante NumPy, sin dependencia de statsmodels.

## Corrección de dirección de las escalas
Consultar ESCALAS.md y auditoria_recodificacion_escalas.csv. Esta versión sustituye el paquete anterior: tres columnas conservan las respuestas originales y las tres columnas analíticas usan 6 - x. La base preparada ahora contiene 33 columnas, sin reincorporar campos personales excluidos.
