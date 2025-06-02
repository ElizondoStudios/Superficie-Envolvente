from flask import Flask, request, render_template, send_file, session, current_app
from voxeles import Voxelizar, ExportarTexto
from zipfile import ZipFile
import os
import io


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
            saved_file = f"./static/mesh/object.{extension}"

            # Guardar el objeto original
            archivo.save(saved_file)
            
            # Voxelizar el objeto original (sólido)
            obj_vox, obj_count= Voxelizar(saved_file)

            #Voxelizar extrayendo únicamente la superficie envolvente (hueco)
            mesh_vox, mesh_count= Voxelizar(saved_file, True)

            # Obtenemos el objeto como un txt que se puede visualizar en blender
            ExportarTexto(saved_file)

            return render_template("archivo-procesado.html", file_name=archivo.filename, mesh_url = mesh_vox, mesh_count= mesh_count, object_url= obj_vox, obj_count= obj_count)
        except:
            return render_template("error-archivo.html")
    else:
        return render_template("error-archivo.html")

@app.route("/descargar-archivo")
def descargar_archivo():
    files = ['object-vox-mesh.obj', 'object-vox.obj', 'object.obj', 'object.txt']
    zip_buffer = io.BytesIO()

    with ZipFile(zip_buffer, 'w') as zip_file:
        path = "./static/mesh"
        for file in files:
            file_path = path + "/" + file
            zip_file.write(file_path, arcname=file)  # arcname avoids full path

    zip_buffer.seek(0)

    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        download_name='mesh.zip'
    )

if __name__ == "__main__":
    app.run(debug=True)
