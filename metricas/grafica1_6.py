import matplotlib.pyplot as plt
import numpy as np

# Datos de los pesos en bytes para B y C
pesos_B = [
    629760, 324608, 434176, 289792, 383232, 368640, 
    334592, 355328, 712704, 452764.5
]

pesos_C = [
    250880, 77171, 17408, 75482, 123904, 90662, 83763, 119808, 195584, 50104
]

# Crear un array con los índices de las imágenes
imagenes = np.arange(1, len(pesos_B) + 1)

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))

bar_width = 0.35  # Ancho de las barras
index = np.arange(len(pesos_B))  # Posiciones de las barras en el eje x

# Graficar los pesos de B y C
plt.bar(index - bar_width / 2, pesos_B, bar_width, label="Peso B", color="g")
plt.bar(index + bar_width / 2, pesos_C, bar_width, label="Peso C", color="r")

# Etiquetas y título
plt.xlabel('Número de Objeto')
plt.ylabel('Peso en Bytes')
plt.title('Comparación de Pesos en Bytes (B vs C) de los Objetos')
plt.xticks(index, imagenes)  # Etiquetas del eje x
plt.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
