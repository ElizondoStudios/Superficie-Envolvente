# Extraer la superficie envolvente de modelos tridimensionales

## Acerca del proyecto
Cuando el usuario sube un modelo tridimensional, puede visualizar el objeto voxelizado, así como, la superficie envolvente, la cuál se conforma de las caras externas de los voxeles que conforman el objeto voxelizado.
El usuario puede observar el conteo de caras de cada modelo así como descargar los archivos procesados.

## Requisitos para correr el proyecto
- [Python 3](https://www.python.org/downloads/)

## Cómo descargar un repositorio de Github
[Cómo descargar un repositorio de Github](https://docs.github.com/en/get-started/start-your-journey/downloading-files-from-github)

## Cómo ejecutar el proyecto
1. Instalar las dependencias en caso de ser necesario (instrucciones abajo en el documento)
2. Ejecutar el archivo `app.py`
3. Ingresar a http://localhost:5000

## Uso del programa
1. Selecciona un documento .obj o .ply (hay opciones en la carpeta public) 
2. Dar click en el botón azul que dice "Procesar"
3. En caso de querer descargar los objetos de la superficie envolvente dar click en el botón azul que dice "Descargar Archivos"


## Pasos para instalar las dependencias
Seguir los siguientes pasos en la terminal

### Paso 1:
```sh
python -m venv .venv
```
### Paso 2:
```sh
.venv\Scripts\activate
```

### Paso 3:
```sh
pip install -r requirements.txt
```