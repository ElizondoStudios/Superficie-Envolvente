# Extraer la superficie envolvente de modelos tridimensionales

## Objetivo
Que el usuario suba un modelo tridimensional, y mostremos usando [ThreeJS](https://threejs.org/), el modelo tridimensional que subió el usuario, así como, la malla (superficie envolvente) del modelo. Estos modelos se van a mostrar en un espacio interactivo, donde mostraremos también, características de cada modelo.
También, el usuario va a poder descargar el modelo del mallado.

## Comentarios
- Para ejecutar la aplicación solo es necesario correr el archivo app.py
- Los archivos de `/templates` son plantillas html que vamos a mostrar al usuario
- Usamos bootstrap en html

## En caso de tener errores con las dependencias crear un .venv

### Paso 1:
Desde el folder del proyecto usando bash:
python -m venv .venv

### Paso 2:
.venv\Scripts\activate

### Paso 3:
pip install -r requirements.txt