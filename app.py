'''
Dependencias:
  pip install nu`mpy pillow "pyglet<2" trimesh scipy flask
'''

from flask import Flask, request, render_template, send_file, session
import trimesh
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
    extension= session["extension"]
    file= open(f"./static/mesh/exported-mesh.{extension}", "rb")
    return send_file(file, download_name=file.name.replace("./static/mesh/", ""))


if __name__ == "__main__":
    app.run(debug=True)
