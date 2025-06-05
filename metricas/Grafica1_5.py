import matplotlib.pyplot as plt
import numpy as np

# Datos de los pesos en bytes para A, B y C
pesos_A = [
    3138605, 44250798, 35140546, 15200290, 16199643, 38751625,
    7997428, 2315083, 146837048, 28297841
]
pesos_B = [
    629760, 324608, 434176, 289792, 383232, 368640, 
    334592, 355328, 712704, 452764.5
]
pesos_C = [
    250880, 77171, 17408, 75482, 123904, 90662, 83763, 119808, 195584, 50104
]
import matplotlib.pyplot as plt

# Datos de los pesos en bytes para A, B y C
pesos_A = [
    3138605, 44250798, 35140546, 15200290, 16199643, 38751625,
    7997428, 2315083, 146837048, 28297841
]
pesos_B = [
    629760, 324608, 434176, 289792, 383232, 368640, 
    334592, 355328, 712704, 452764.5
]
pesos_C = [
    250880, 77171, 17408, 75482, 123904, 90662, 83763, 119808, 195584, 50104
]

# Etiquetas para los puntos (pueden ser los nombres de los archivos o cualquier etiqueta)
etiquetas = [f"Objeto {i+1}" for i in range(len(pesos_A))]

# Crear la gráfica de líneas con colores armónicos
plt.figure(figsize=(10, 6))
plt.plot(etiquetas, pesos_A, label='Peso A', marker='o', color='#6fa3ef')  # Azul suave
plt.plot(etiquetas, pesos_B, label='Peso B', marker='s', color='#f7a37f')  # Naranja suave
plt.plot(etiquetas, pesos_C, label='Peso C', marker='^', color='#8dbf6d')  # Verde suave

# Personalizar el gráfico
plt.title("Comparación de Tamaños de Objetos A, B y C", fontsize=14, fontweight='bold')
plt.xlabel("Objetos", fontsize=12)
plt.ylabel("Tamaño en Bytes", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend()

# Mostrar la gráfica
plt.tight_layout()
plt.show()
