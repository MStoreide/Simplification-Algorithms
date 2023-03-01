import open3d as o3d

NUMVC = o3d.io.read_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Baselines\NUMB.obj")
NUMVC.compute_vertex_normals()

print(
    f'Baseline mesh has {len(NUMVC.vertices)} vertices and {len(NUMVC.triangles)} triangles'
)

#14 is approximately dividing by 155
voxel_size = max(NUMVC.get_max_bound() - NUMVC.get_min_bound()) / 155
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp14 = NUMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 14 has {len(mesh_smp14.vertices)} vertices and {len(mesh_smp14.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\NUMVC\NUMVC14.obj", mesh_smp14)

#15 is approximately dividing by 139
voxel_size = max(NUMVC.get_max_bound() - NUMVC.get_min_bound()) / 139 #Document how this number is generated, and what it does. 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp15 = NUMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 15 has {len(mesh_smp15.vertices)} vertices and {len(mesh_smp15.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\NUMVC\NUMVC15.obj", mesh_smp15)



#16 is approximately dividing by 111
voxel_size = max(NUMVC.get_max_bound() - NUMVC.get_min_bound()) / 111 # This 32 number must be changed for each stage. How to best get this? (32 = 4234)
print(f'voxel_size = {voxel_size:e}')                                # Lowering the number, e.g 10, reduces the output triangles (401 Triangles)
mesh_smp16 = NUMVC.simplify_vertex_clustering(                        # 50 = 11289 triangles
    voxel_size=voxel_size,                                           # 500 = 433942 triangles
    contraction=o3d.geometry.SimplificationContraction.Average)      # 100 = 43288
print(
    f'Simplification stage 16 has {len(mesh_smp16.vertices)} vertices and {len(mesh_smp16.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\NUMVC\NUMVC16.obj", mesh_smp16)
