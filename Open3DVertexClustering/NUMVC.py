import open3d as o3d

NUMVC = o3d.io.read_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Baselines\NUMB.obj")
NUMVC.compute_vertex_normals()

print(
    f'Baseline mesh has {len(NUMVC.vertices)} vertices and {len(NUMVC.triangles)} triangles'
)

voxel_size = max(NUMVC.get_max_bound() - NUMVC.get_min_bound()) / 100 # This 32 number must be changed for each stage. How to best get this? (32 = 4234)
print(f'voxel_size = {voxel_size:e}')                                # Lowering the number, e.g 10, reduces the output triangles (401 Triangles)
mesh_smp1 = NUMVC.simplify_vertex_clustering(                        # 50 = 11289 triangles
    voxel_size=voxel_size,                                           # 500 = 433942 triangles
    contraction=o3d.geometry.SimplificationContraction.Average)      # 100 = 43288
print(
    f'Simplification stage 1 has {len(mesh_smp1.vertices)} vertices and {len(mesh_smp1.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\NUMVC\NUMVC1.obj", mesh_smp1) # Iterate up to 16

#Repeat 15 more times when it works.
