from flask import Flask, request, render_template, send_file, session
from voxeles import Voxelizar

app = Flask(__name__)
app.secret_key = 'clave-secreta-super-segura'

@app.route("/")
def root():
    return render_template("solicitar-archivo.html")

@app.route("/extraer-superficie", methods=["POST"])
def extraer_superficie():
    archivo = request.files["archivo"]
 
    # Extraer la superficie envolvente
    if archivo.filename != "":
        try:
            extension= archivo.filename.split('.')[-1]
            session["extension"]= extension
            
            # Guardar el objeto original
            archivo.save(f"./static/mesh/object.{extension}")
            
            # Voxelizar el objeto original (sólido)
            obj_vox, obj_count= Voxelizar(f"./static/mesh/object.{extension}")

            #Voxelizar extrayendo únicamente la superficie envolvente (hueco)
            mesh_vox, mesh_count= Voxelizar(f"./static/mesh/object.{extension}", True)

            return render_template("archivo-procesado.html", file_name=archivo.filename, mesh_url = mesh_vox, mesh_count= mesh_count, object_url= obj_vox, obj_count= obj_count)
        except:
            return render_template("error-archivo.html")
    else:
        return render_template("error-archivo.html")

@app.route("/descargar-archivo")
def descargar_archivo():
    '''
    Lógica para descargar zip con todos los archvios:
        - Objeto voxelizado (.binvox)
        - Superficie envolvente voxelizada (.binvox)
        - Objeto voxelizado (.obj)
        - Superficie envolvente voxelizada (.obj)
        - Objeto voxelizado binario (.txt)
        - Superficie envolvente voxelizada (.txt)
    '''
    pass


if __name__ == "__main__":
    app.run(debug=True)
