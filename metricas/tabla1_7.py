import pandas as pd

# Datos proporcionados
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

# Calcular los porcentajes de reducción
def porcentaje_reduccion(a, b):
    return ((a - b) / a) * 100

# Crear la tabla
data = {
    'Objeto': [f'Objeto {i+1}' for i in range(len(pesos_A))],
    'Reducción A vs B (%)': [porcentaje_reduccion(a, b) for a, b in zip(pesos_A, pesos_B)],
    'Reducción A vs C (%)': [porcentaje_reduccion(a, c) for a, c in zip(pesos_A, pesos_C)]
}

# Convertir a DataFrame para presentar en tabla
df = pd.DataFrame(data)
print(df)
