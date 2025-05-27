import numpy as np
import trimesh
import trimesh.exchange
import trimesh.exchange.binvox

mesh = trimesh.load_mesh('./Public/OBJ/Armadillo.obj')

voxels= trimesh.exchange.binvox.voxelize_mesh(mesh)

file= open("./Public/matriz-texto.txt", "w")

for i in voxels.matrix:
  for j in i:
    for k in j:
      if k:
        file.write("1,")
      else:
        file.write("0,")
