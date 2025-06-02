import trimesh
import trimesh.exchange
import trimesh.exchange.binvox

def ExportarTexto(file):
  voxels = ObtenerMatrizVoxeles(file)

  txt_file = f"./static/mesh/object.txt"

  file= open(txt_file, "w")
  for i in voxels.matrix:
    for j in i:
      for k in j:
        if k:
          file.write("1,")
        else:
          file.write("0,")
  file.close()

def Voxelizar(file: str, hollow= False):
  mesh = trimesh.load_mesh(file_obj=file)
  voxels= trimesh.exchange.binvox.voxelize_mesh(mesh)
  ext= file.split('.')[-1]
  save_as= ""
  count=0

  if not hollow:
    voxels.fill()
    count= voxels.filled_count
    save_as= file.replace(f".{ext}", f"-vox.{ext}")
  else:
    voxels.hollow()
    count= voxels.filled_count
    save_as= file.replace(f".{ext}", f"-vox-mesh.{ext}")
  
  voxels.as_boxes().export(file_obj=save_as, file_type=ext)
  return (save_as, count)

def ObtenerMatrizVoxeles(file: str):
  mesh = trimesh.load_mesh(file_obj=file)
  voxels= trimesh.exchange.binvox.voxelize_mesh(mesh)
  return voxels
