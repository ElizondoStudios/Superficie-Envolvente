import trimesh
import trimesh.exchange
import trimesh.exchange.binvox
import numpy as np
import os

def ExportarTexto(file):
  voxels = ObtenerMatrizVoxeles(file)

  extension = file.split('.')[-1]

  txt_file = file.replace(f".{extension}", "-bits.txt")

  file= open(txt_file, "w")
  for i in voxels.matrix:
    for j in i:
      for k in j:
        if k:
          file.write("1,")
        else:
          file.write("0,")
  file.close()

def Voxelizar(file: str):
  mesh = trimesh.load_mesh(file_obj=file)
  voxels= trimesh.exchange.binvox.voxelize_mesh(mesh)
  ext= file.split('.')[-1]
  save_as= ""
  count=0

  count= len(voxels.as_boxes().faces)
  save_as= file.replace(f".{ext}", f"-vox.{ext}")
  
  voxels.as_boxes().export(file_obj=save_as, file_type=ext)
  return (save_as, count)

def ObtenerMatrizVoxeles(file: str):
  mesh = trimesh.load_mesh(file_obj=file)
  voxels= trimesh.exchange.binvox.voxelize_mesh(mesh)
  return voxels


def ExtraerSuperficieEnvolvente(file: str):
  mesh = trimesh.load_mesh(file_obj=file)

  # Usamos la mesh filled para quitar las caras internas de los voxeles exteriores
  voxels= trimesh.exchange.binvox.voxelize_mesh(mesh).fill()

  ext= file.split('.')[-1]
  save_as= file.replace(f".{ext}", f"-superficie-envolvente.{ext}")
  count=0

  data = voxels.matrix

  # Agregar padding a los datos para los bloques en los border
  padded_data = np.pad(data, 1, mode='constant')

  # Calcular la suma de los vecinos
  neighbor_sum = (
      np.roll(padded_data, 1, axis=0) + np.roll(padded_data, -1, axis=0)
      + np.roll(padded_data, 1, axis=1) + np.roll(padded_data, -1, axis=1)
      + np.roll(padded_data, 1, axis=2) + np.roll(padded_data, -1, axis=2)
  )

  # Marcar los voxeles de perímetro
  perimeter_voxels = (data == 1) & (neighbor_sum[1:-1, 1:-1, 1:-1] < 6)

  # Arreglo de caras y vértices solo para las caras
  vertices = []
  faces = []

  # Diccionario para reutilizar las caras de los vertices
  vertex_dict = {}

  # Posiciones de los vértices relativos a la posición de los voxeles
  vertex_offsets = [
      (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
      (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)
  ]

  # Caras definidas por los vértices de los índices
  face_definitions = {
      'abajo': (3, 2, 1, 0),
      'arriba': (4, 5, 6, 7),
      'adelante': (0, 1, 5, 4),
      'derecha': (1, 2, 6, 5),
      'atras': (2, 3, 7, 6),
      'izquierda': (3, 0, 4, 7)
  }

  # Offset de los vecinos para cada cara
  neighbor_offsets = {
      'abajo': (0, 0, -1),
      'arriba': (0, 0, 1),
      'adelante': (0, -1, 0),
      'derecha': (1, 0, 0),
      'atras': (0, 1, 0),
      'izquierda': (-1, 0, 0)
  }

  # Función para obtener o crear los índices de los vértices
  def get_vertex_index(pos):
      if pos not in vertex_dict:
          vertex_dict[pos] = len(vertices)
          vertices.append((pos[0], pos[1], pos[2]))
      return vertex_dict[pos]

  for i in range(perimeter_voxels.shape[0]):
      for j in range(perimeter_voxels.shape[1]):
          for k in range(perimeter_voxels.shape[2]):
              if perimeter_voxels[i, j, k]:
                  voxel_pos = (i, j, k)
                  # Calcular la posición actual con padding offset+1
                  pi, pj, pk = i+1, j+1, k+1

                  for face, vert_ids in face_definitions.items():
                      di, dj, dk = neighbor_offsets[face]
                      if padded_data[pi+di, pj+dj, pk+dk] == 0:
                          # Crear los vértices para las caras
                          face_vertex_indices = []
                          for vid in vert_ids:
                              vi, vj, vk = vertex_offsets[vid]
                              vertex_pos = (voxel_pos[0]+vi, voxel_pos[1]+vj, voxel_pos[2]+vk)
                              idx = get_vertex_index(vertex_pos)
                              face_vertex_indices.append(idx)
                          faces.append(tuple(face_vertex_indices))

  mesh= trimesh.Trimesh(vertices, faces)
  count= len(mesh.faces)
  mesh.export(file_obj=save_as, file_type=ext)
  return (save_as, count)

def EliminarArchivosMesh(path : str):
  path = './static/mesh'
  for filename in os.listdir(path):
      file_path = os.path.join(path, filename)
      if os.path.isfile(file_path):  # only delete files
          os.remove(file_path)