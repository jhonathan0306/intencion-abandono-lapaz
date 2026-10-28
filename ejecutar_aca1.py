# Ejecuta las celdas del cuaderno desde la carpeta del proyecto.
import json
from pathlib import Path
nb=json.loads(Path('notebooks/ACA1_Holguin_Rivera.ipynb').read_text(encoding='utf-8'))
ns={'__name__':'__main__'}
for cell in nb['cells']:
    if cell['cell_type']=='code': exec(compile(cell['source'],'ACA1','exec'),ns)
