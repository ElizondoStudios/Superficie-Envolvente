import numpy as np

# Tiempos de procesamiento para cada método (en segundos)
tiempos_A = [
    0.5363, 10.1169, 7.1094, 0.7257, 0.4169, 2.0768, 
    0.3799, 0.1767, 50.7370, 1.6076
]

tiempos_B = [
    0.0254, 0.0152, 0.190, 0.0135, 0.0168, 0.0309, 
    0.0146, 0.0147, 0.1021, 0.0187
]

tiempos_C = [
    0.0135, 0.0065, 0.0084, 0.0058, 0.0079, 0.0266, 
    0.0060, 0.0070, 0.0648, 0.0068
]

# Calcular la desviación estándar para cada conjunto de tiempos
desviacion_estandar_A = np.std(tiempos_A)
desviacion_estandar_B = np.std(tiempos_B)
desviacion_estandar_C = np.std(tiempos_C)

# Imprimir los resultados
print(f"Desviación estándar del Método A: {desviacion_estandar_A}")
print(f"Desviación estándar del Método B: {desviacion_estandar_B}")
print(f"Desviación estándar del Método C: {desviacion_estandar_C}")
