from io import BufferedReader
import trimesh
import trimesh.exchange
import trimesh.exchange.binvox

def Voxelizar(file: str, hollow= False):
  mesh = trimesh.load_mesh(file_obj=file)
  voxels= trimesh.exchange.binvox.voxelize_mesh(mesh)
  ext= file.split('.')[-1]
  save_as= ""

  if not hollow:
    voxels.fill()
    save_as= file.replace(f".{ext}", f"-vox.{ext}")
  else:
    voxels.hollow()
    save_as= file.replace(f".{ext}", f"-vox-mesh.{ext}")
  
  voxels.as_boxes().export(file_obj=save_as, file_type=ext)
  return save_as