import open3d as o3d

#    voxel_size = max(NUMVC.get_max_bound() - NUMVC.get_min_bound()) / 32
#     mesh_smp = NUMVC.simplify_vertex_clustering(
#         voxel_size=voxel_size,
#         contraction=o3d.geometry.SimplificationContraction.Average)
#     print("After Simplification with voxel size =", voxel_size, ":\n", mesh_smp)
#     o3d.visualization.draw_geometries([mesh_smp])

# bunny = o3d.data.BunnyMesh()
NUMVC = o3d.io.read_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Baselines\NUMB.obj")
NUMVC.compute_vertex_normals()

print(
    f'Input mesh has {len(NUMVC.vertices)} vertices and {len(NUMVC.triangles)} triangles'
)

voxel_size = max(NUMVC.get_max_bound() - NUMVC.get_min_bound()) / 32 #This 32 number must be changed for each. 
print(f'voxel_size = {voxel_size:e}')
mesh_smp1 = NUMVC.simplify_vertex_clustering(
    voxel_size=voxel_size,
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\NUMVC\NUMVC1.obj", mesh_smp1)

#Repeat 15 more times when it works.
