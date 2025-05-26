'''
Dependencias:
  pip install nu`mpy pillow "pyglet<2" trimesh scipy flask
'''

from flask import Flask, request, render_template, send_file
import numpy as np
import trimesh
import trimesh.exchange
import trimesh.exchange.binvox

app = Flask(__name__)
extension=""

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
            
            # Guardar el objeto original
            archivo.save(f"./static/mesh/object.{extension}")
            
            # Extraer la superficie envolvente y guardar
            mesh= trimesh.load_mesh(f"./static/mesh/object.{extension}", file_type= extension)
            mesh.export(f"./static/mesh/exported-mesh.{extension}")


            return render_template("archivo-procesado.html", file_name=archivo.filename, mesh_url = f"./static/mesh/exported-mesh.{extension}", object_url= f"./static/mesh/object.{extension}")
        except:
            return render_template("error-archivo.html")
    else:
        return render_template("error-archivo.html")

@app.route("/descargar-archivo")
def descargar_archivo():
    file= open(f"./static/mesh/exported-mesh.{extension}", "rb")
    return send_file(file, download_name=file.name.replace("./Public/", ""))


if __name__ == "__main__":
    app.run(debug=True)
