import open3d as o3d

RMVC = o3d.io.read_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Baselines\RMB.obj")
RMVC.compute_vertex_normals()

print(
    f'Baseline mesh has {len(RMVC.vertices)} vertices and {len(RMVC.triangles)} triangles'
)

#1 is approximately dividing by 800
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 800 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp1 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                        
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 1 has {len(mesh_smp1.vertices)} vertices and {len(mesh_smp1.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC1.obj", mesh_smp1)

#2 is approximately dividing by 600
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 600 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp2 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                       
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 2 has {len(mesh_smp2.vertices)} vertices and {len(mesh_smp2.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC2.obj", mesh_smp2)

#3 is approximately dividing by 500
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 500 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp3 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                      
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 3 has {len(mesh_smp3.vertices)} vertices and {len(mesh_smp3.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC3.obj", mesh_smp3)


#4 is approximately dividing by 404
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 404 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp4 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                         
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 4 has {len(mesh_smp4.vertices)} vertices and {len(mesh_smp4.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC4.obj", mesh_smp4)


#5 is approximately dividing by 350
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 350 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp5 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                       
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 5 has {len(mesh_smp5.vertices)} vertices and {len(mesh_smp5.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC5.obj", mesh_smp5)


#6 is approximately dividing by 308
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 308 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp6 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                        
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 6 has {len(mesh_smp6.vertices)} vertices and {len(mesh_smp6.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC6.obj", mesh_smp6)

#7 is approximately dividing by 288
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 288 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp7 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                       
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 7 has {len(mesh_smp7.vertices)} vertices and {len(mesh_smp7.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC7.obj", mesh_smp7)

#8 is approximately dividing by 249
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 249 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp8 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                     
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 8 has {len(mesh_smp8.vertices)} vertices and {len(mesh_smp8.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC8.obj", mesh_smp8)

#9 is approximately dividing by 228
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 228 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp9 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                        
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 9 has {len(mesh_smp9.vertices)} vertices and {len(mesh_smp9.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC9.obj", mesh_smp9)


#10 is approximately dividing by 214
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 214 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp10 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 10 has {len(mesh_smp10.vertices)} vertices and {len(mesh_smp10.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC10.obj", mesh_smp10)


#11 is approximately dividing by 197
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 197 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp11 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 11 has {len(mesh_smp11.vertices)} vertices and {len(mesh_smp11.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC11.obj", mesh_smp11)


#12 is approximately dividing by 183
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 183 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp12 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 12 has {len(mesh_smp12.vertices)} vertices and {len(mesh_smp12.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC12.obj", mesh_smp12)


#13 is approximately dividing by 170
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 170 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp13 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 13 has {len(mesh_smp13.vertices)} vertices and {len(mesh_smp13.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC13.obj", mesh_smp13)

#14 is approximately dividing by 155
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 155
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp14 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 14 has {len(mesh_smp14.vertices)} vertices and {len(mesh_smp14.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC14.obj", mesh_smp14)

#15 is approximately dividing by 139
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 139 
print(f'voxel_size = {voxel_size:e}')                                
mesh_smp15 = RMVC.simplify_vertex_clustering(                        
    voxel_size=voxel_size,                                          
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 15 has {len(mesh_smp15.vertices)} vertices and {len(mesh_smp15.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC15.obj", mesh_smp15)



#16 is approximately dividing by 111
voxel_size = max(RMVC.get_max_bound() - RMVC.get_min_bound()) / 111
print(f'voxel_size = {voxel_size:e}')
mesh_smp16 = RMVC.simplify_vertex_clustering(
    voxel_size=voxel_size,
    contraction=o3d.geometry.SimplificationContraction.Average)
print(
    f'Simplification stage 16 has {len(mesh_smp16.vertices)} vertices and {len(mesh_smp16.triangles)} triangles'
)

o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC16.obj", mesh_smp16)

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
#    o3d.io.write_triangle_mesh(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Vertex Clustering\RMVC\RMVC16.obj", mesh_smp)