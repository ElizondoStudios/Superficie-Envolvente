# Instrumento medida de carga

import time
import trimesh

def medir_tiempo_carga(path):
    start = time.time()
    trimesh.load_mesh(path, force='mesh')
    end = time.time()
    return end - start


archivo = ""

try:
    tiempo = medir_tiempo_carga(archivo)
    print(f"{archivo} -> Tiempo de carga: {tiempo:.4f} segundos")
except Exception as e:
    print(f"Error cargando {archivo}: {e}")
