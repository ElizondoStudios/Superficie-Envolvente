import matplotlib.pyplot as plt

# Datos
categorias = ['Reducción Tiempo A→B', 'Reducción Tiempo A→C', 'Reducción Caras B→C']
valores = [96.97, 98.63, 79.54]

# Tonos de gris para las barras
grises = ['#555555', '#888888', '#BBBBBB']

# Crear gráfico de barras
plt.figure(figsize=(8,5))
bars = plt.bar(categorias, valores, color=grises)

# Añadir valores encima de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.2f}%', ha='center', fontsize=12, color='black')

plt.ylim(0, 110)
plt.ylabel('Porcentaje de reducción (%)')
plt.title('Promedio de reducción en tiempo y conteo de caras')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
