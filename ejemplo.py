import numpy as np
import trimesh
import trimesh.exchange
import trimesh.exchange.binvox

# attach to logger so trimesh messages will be printed to console
# trimesh.util.attach_to_log()

# mesh objects can be created from existing faces and vertex data
mesh = trimesh.load_mesh('./Turtle.obj')
# mesh.export(file_obj='./Turtle-mesh.obj')
mesh.show()
# voxels= trimesh.exchange.binvox.voxelize_mesh(mesh)
# voxels.export(file_obj='./Turtle-voxels.binvox')
# voxels.show()

# vertices = np.array([
#     [0, 0, 0],  # Vértice 0
#     [1, 0, 0],  # Vértice 1
#     [1, 1, 0],  # Vértice 2
#     [0, 1, 0],  # Vértice 3
#     [0.5, 0.5, 1]  # Vértice 4 (punta)
# ])

# faces = np.array([
#     [0, 1, 4],  # Cara 0
#     [1, 2, 4],  # Cara 1
#     [2, 3, 4],  # Cara 2
#     [3, 0, 4],  # Cara 3
#     [0, 1, 2],  # Base (cara 4, lado 1)
#     [0, 2, 3]   # Base (cara 5, lado 2)
# ])

# mesh= trimesh.Trimesh(vertices, faces)

# mesh.show()

# mesh.export(file_obj='/home/jose-luis/Downloads/ted-bear/ted-mesh.stl')