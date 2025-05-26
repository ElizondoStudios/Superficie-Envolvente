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

@app.route("/")
def root():
    return render_template("solicitar-archivo.html")

@app.route("/extraer-superficie", methods=["POST"])
def extraer_superficie():
    archivo = request.files["archivo"]
    if archivo.filename != "":
        try:
            extension= archivo.filename.split('.')[-1]
            mesh= trimesh.load_mesh(file_obj= archivo, file_type= extension)
            mesh.export(f"./Public/exported-mesh.{extension}")
            mesh.export(f"./static/mesh/exported-mesh.{extension}")
            return render_template("archivo-procesado.html", file_name=archivo.filename, mesh_url = f"./static/mesh/exported-mesh.{extension}")
        except:
            return render_template("error-archivo.html")
    else:
        return render_template("error-archivo.html")

@app.route("/descargar-archivo")
def descargar_archivo():
    file= open("./Public/exported-mesh.obj", "rb")
    return send_file(file, download_name=file.name.replace("./Public/", ""))


if __name__ == "__main__":
    app.run(debug=True)
