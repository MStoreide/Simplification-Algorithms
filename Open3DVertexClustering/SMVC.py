import open3d as o3d

SMVC = o3d.io.read_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Baselines\SMB.obj")
SMVC.compute_vertex_normals()

print(
    f'Baseline mesh has {len(SMVC.vertices)} vertices and {len(SMVC.triangles)} triangles'
)

#1 is approximately dividing by 800
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 75 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp1 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                        
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 1 has {len(mesh_smp1.vertices)} vertices and {len(mesh_smp1.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC1.obj", mesh_smp1)

#2 is approximately dividing by 600
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 69 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp2 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                       
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 2 has {len(mesh_smp2.vertices)} vertices and {len(mesh_smp2.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC2.obj", mesh_smp2)

#3 is approximately dividing by 500
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 66 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp3 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                      
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 3 has {len(mesh_smp3.vertices)} vertices and {len(mesh_smp3.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC3.obj", mesh_smp3)


#4 is approximately dividing by 404
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 62 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp4 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                         
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 4 has {len(mesh_smp4.vertices)} vertices and {len(mesh_smp4.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC4.obj", mesh_smp4)


#5 is approximately dividing by 350
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 59 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp5 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                       
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 5 has {len(mesh_smp5.vertices)} vertices and {len(mesh_smp5.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC5.obj", mesh_smp5)


#6 is approximately dividing by 308
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 56
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp6 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                        
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 6 has {len(mesh_smp6.vertices)} vertices and {len(mesh_smp6.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC6.obj", mesh_smp6)

#7 is approximately dividing by 288
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 52 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp7 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                       
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 7 has {len(mesh_smp7.vertices)} vertices and {len(mesh_smp7.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC7.obj", mesh_smp7)

#8 is approximately dividing by 249
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 50 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp8 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                     
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 8 has {len(mesh_smp8.vertices)} vertices and {len(mesh_smp8.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC8.obj", mesh_smp8)

#9 is approximately dividing by 228
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 46 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp9 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                        
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 9 has {len(mesh_smp9.vertices)} vertices and {len(mesh_smp9.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC9.obj", mesh_smp9)


#10 is approximately dividing by 214
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 43 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp10 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 10 has {len(mesh_smp10.vertices)} vertices and {len(mesh_smp10.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC10.obj", mesh_smp10)


#11 is approximately dividing by 197
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 40 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp11 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 11 has {len(mesh_smp11.vertices)} vertices and {len(mesh_smp11.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC11.obj", mesh_smp11)


#12 is approximately dividing by 183
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 35 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp12 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 12 has {len(mesh_smp12.vertices)} vertices and {len(mesh_smp12.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC12.obj", mesh_smp12)


#13 is approximately dividing by 170
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 33 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp13 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 13 has {len(mesh_smp13.vertices)} vertices and {len(mesh_smp13.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC13.obj", mesh_smp13)

#14 is approximately dividing by 155
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 29
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp14 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 14 has {len(mesh_smp14.vertices)} vertices and {len(mesh_smp14.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC14.obj", mesh_smp14)

#15 is approximately dividing by 139
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 24 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp15 = SMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 15 has {len(mesh_smp15.vertices)} vertices and {len(mesh_smp15.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC15.obj", mesh_smp15)



#16 is approximately dividing by 111
voxel_size = max(SMVC.get_max_bound() - SMVC.get_min_bound()) / 20
print(f'voxel_size = {voxel_size:e}')
mesh_smp16 = SMVC.simplify_vertex_clustering(
    voxel_size=voxel_size,
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 16 has {len(mesh_smp16.vertices)} vertices and {len(mesh_smp16.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\SMVC\SMVC16.obj", mesh_smp16)

print("Simplification Finished")