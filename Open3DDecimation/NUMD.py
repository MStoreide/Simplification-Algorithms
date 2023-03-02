import open3d as o3d

# Note that open3d requires version 3.10 of Python. 

# Mesh needs to be manifold and triangulated.
NUMbase = o3d.io.read_triangle_mesh(r"D:\Datasets\Paper_Simplification\Baselines\NUMB.obj") #NUMB is the baseline mesh for comparison. 
NUMbase.compute_vertex_normals()
print(NUMbase)

print("Before simplification:", NUMbase)

totaltris=522328

#Starting simplification. Going through 16 stages, reducing by 5,625% at each stage. 

mesh_smp1 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.94375))
)
print("Simplification Stage 1 (5.623% reduction): ", mesh_smp1)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD1.obj", mesh_smp1)


mesh_smp2 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.8875))
)
print("Simplification Stage 2 (5.623%*2 reduction): ", mesh_smp2)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD2.obj", mesh_smp2)


mesh_smp3 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.83125))
)
print("Simplification Stage 3 (5.623%*3 reduction): ", mesh_smp3)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD3.obj", mesh_smp3)


mesh_smp4 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.775))
) 
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD4.obj", mesh_smp4)


mesh_smp5 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.71875))
)
print("Simplification Stage 5 (5.623%*5 reduction): ", mesh_smp5)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD5.obj", mesh_smp5)


mesh_smp6 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.6625))
)
print("Simplification Stage 6 (5.623%*6 reduction): ", mesh_smp6)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD6.obj", mesh_smp6)


mesh_smp7 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.60625))
)
print("Simplification Stage 7 (5.623%*7 reduction): ", mesh_smp7)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD7.obj", mesh_smp7)


mesh_smp8 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.55))
)
print("Simplification Stage 8 (5.623%*8 reduction): ", mesh_smp8)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD8.obj", mesh_smp8)


mesh_smp9 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.49375))
)
print("Simplification Stage 9 (5.623%*9 reduction): ", mesh_smp9)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD9.obj", mesh_smp9)


mesh_smp10 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.4375))
)
print("Simplification Stage 10 (5.623%*10 reduction): ", mesh_smp10)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD10.obj", mesh_smp10)


mesh_smp11 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.38125))
)
print("Simplification Stage 11 (5.623%*11 reduction): ", mesh_smp11)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD11.obj", mesh_smp11)


mesh_smp12 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.325))
)
print("Simplification Stage 12 (5.623%*12 reduction): ", mesh_smp12)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD12.obj", mesh_smp12)


mesh_smp13 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.26875))
)
print("Simplification Stage 13 (5.623%*13 reduction): ", mesh_smp13)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD13.obj", mesh_smp13)


mesh_smp14 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.2125))
)
print("Simplification Stage 14 (5.623%*14 reduction): ", mesh_smp14)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD14.obj", mesh_smp14)


mesh_smp15 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.15625))
)   
print("Simplification Stage 15 (5.623%*15 reduction): ", mesh_smp15)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD15.obj", mesh_smp15)


mesh_smp16 = NUMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.1))
)
print("Simplification Stage 16 (5.623%*16 reduction): ", mesh_smp16)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\NUMD\NUMD16.obj", mesh_smp16)
