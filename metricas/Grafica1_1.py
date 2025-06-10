import matplotlib.pyplot as plt

# Comparacion de tiempo de AB Y C  en escala logarimtica para que se aprecie mejor 
tiempos_a = [0.5363, 10.1169, 7.1094, 0.7257, 0.4169, 2.0768, 0.3799, 0.1767, 50.7370, 1.6076]
tiempos_b = [0.0254, 0.0152, 0.1900, 0.0135, 0.0168, 0.0309, 0.0146, 0.0147, 0.1021, 0.0187]
tiempos_c = [0.0135, 0.0065, 0.0084, 0.0058, 0.0079, 0.0266, 0.0060, 0.0070, 0.0648, 0.0068]


objetos = [f'Objeto {i+1}' for i in range(10)]

plt.figure(figsize=(12, 6))

plt.plot(objetos, tiempos_a, marker='o', color='red', label='Tiempo A')
plt.plot(objetos, tiempos_b, marker='o', color='orange', label='Tiempo B')
plt.plot(objetos, tiempos_c, marker='o', color='yellow', label='Tiempo C')

plt.yscale('log')

plt.xlabel('Objetos')
plt.ylabel('Tiempo (segundos, escala logarítmica)')
plt.title('Comparación de Tiempos por Objeto (Líneas, Escala Logarítmica)')
plt.xticks(rotation=45)
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

plt.show()
