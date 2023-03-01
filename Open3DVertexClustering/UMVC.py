import open3d as o3d

UMVC = o3d.io.read_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Baselines\UMB.obj")
UMVC.compute_vertex_normals()

print(
    f'Baseline mesh has {len(UMVC.vertices)} vertices and {len(UMVC.triangles)} triangles'
)

#I cannot use the same division number for every object

#10 is approximately dividing by 197
voxel_size = max(UMVC.get_max_bound() - UMVC.get_min_bound()) / 214 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp10 = UMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 10 has {len(mesh_smp10.vertices)} vertices and {len(mesh_smp10.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC10.obj", mesh_smp10)


#11 is approximately dividing by 197
voxel_size = max(UMVC.get_max_bound() - UMVC.get_min_bound()) / 197 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp11 = UMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 11 has {len(mesh_smp11.vertices)} vertices and {len(mesh_smp11.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC11.obj", mesh_smp11)


#12 is approximately dividing by 183
voxel_size = max(UMVC.get_max_bound() - UMVC.get_min_bound()) / 183 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp12 = UMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 12 has {len(mesh_smp12.vertices)} vertices and {len(mesh_smp12.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC12.obj", mesh_smp12)


#13 is approximately dividing by 170
voxel_size = max(UMVC.get_max_bound() - UMVC.get_min_bound()) / 170 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp13 = UMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 13 has {len(mesh_smp13.vertices)} vertices and {len(mesh_smp13.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC13.obj", mesh_smp13)

#14 is approximately dividing by 155
voxel_size = max(UMVC.get_max_bound() - UMVC.get_min_bound()) / 155
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp14 = UMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 14 has {len(mesh_smp14.vertices)} vertices and {len(mesh_smp14.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC14.obj", mesh_smp14)

#15 is approximately dividing by 139
voxel_size = max(UMVC.get_max_bound() - UMVC.get_min_bound()) / 139 #Document how this number is generated, and what it does. 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp15 = UMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 15 has {len(mesh_smp15.vertices)} vertices and {len(mesh_smp15.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC15.obj", mesh_smp15)



#16 is approximately dividing by 111
voxel_size = max(UMVC.get_max_bound() - UMVC.get_min_bound()) / 111 # This 32 number must be changed for each stage. How to best get this? (32 = 4234)
print(f'voxel_size = {voxel_size:e}')                                # Lowering the number, e.g 10, reduces the output triangles (401 Triangles)
mesh_smp16 = UMVC.simplify_vertex_clustering(                        # 50 = 11289 triangles
    voxel_size=voxel_size,                                           # 500 = 433942 triangles
    contraction=o3d.geometry.SimplificationContraction.Average)      # 100 = 43288
print(
    f'Simplification stage 16 has {len(mesh_smp16.vertices)} vertices and {len(mesh_smp16.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC16.obj", mesh_smp16)

#Function version 
#def vertex.clustering(mesh):
#    mesh = o3d.io.read_triangle_mesh()
#    voxel_size = max(mesh.get_max_bound() - mesh.get_min_bound()) / 111 
#    print(f'voxel_size = {voxel_size:e}')                                
#    mesh_smp = mesh.simplify_vertex_clustering(                        
#    voxel_size=voxel_size,                                           
#    contraction=o3d.geometry.SimplificationContraction.Average)      
#    print(
#    f'Simplification stage 16 has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
#    o3d.io.write_triangle_mesh(r"G:\Markus' Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\UMVC\UMVC16.obj", mesh_smp)