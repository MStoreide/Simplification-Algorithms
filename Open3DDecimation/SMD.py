#Decimation of SM and Calculation of Hausdorff Distance
import open3d as o3d
import pymeshlab as pym

#Note that open3d requires version 3.10 of Python. 

#Can change this to taking it from the project folder instead. Mesh needs to be manifold and triangulated.
SMbase = o3d.io.read_triangle_mesh(r"D:\Datasets\Paper_Simplification\Baselines\SMB.obj")
SMbase.compute_vertex_normals()
print(SMbase)

totaltris=33620

print("Before simplification:", SMbase)
#o3d.visualization.draw_geometries([SMbase]) This can be added later. Visualizing all stages.

#Starting simplification, going through 16 stages.

mesh_smp1 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.94375))
)
print("Simplification Stage 1 (5.623% reduction): ", mesh_smp1)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD1.obj", mesh_smp1)


mesh_smp2 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.8875))
)
print("Simplification Stage 2 (5.623%*2 reduction): ", mesh_smp2)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD2.obj", mesh_smp2)


mesh_smp3 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.83125))
)
print("Simplification Stage 3 (5.623%*3 reduction): ", mesh_smp3)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD3.obj", mesh_smp3)


mesh_smp4 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.775))
) 
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD4.obj", mesh_smp4)


mesh_smp5 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.71875))
)
print("Simplification Stage 5 (5.623%*5 reduction): ", mesh_smp5)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD5.obj", mesh_smp5)


mesh_smp6 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.6625))
)
print("Simplification Stage 6 (5.623%*6 reduction): ", mesh_smp6)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD6.obj", mesh_smp6)


mesh_smp7 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.60625))
)
print("Simplification Stage 7 (5.623%*7 reduction): ", mesh_smp7)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD7.obj", mesh_smp7)


mesh_smp8 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.55))
)
print("Simplification Stage 8 (5.623%*8 reduction): ", mesh_smp8)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD8.obj", mesh_smp8)


mesh_smp9 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.49375))
)
print("Simplification Stage 9 (5.623%*9 reduction): ", mesh_smp9)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD9.obj", mesh_smp9)


mesh_smp10 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.4375))
)
print("Simplification Stage 10 (5.623%*10 reduction): ", mesh_smp10)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD10.obj", mesh_smp10)


mesh_smp11 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.38125))
)
print("Simplification Stage 11 (5.623%*11 reduction): ", mesh_smp11)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD11.obj", mesh_smp11)


mesh_smp12 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.325))
)
print("Simplification Stage 12 (5.623%*12 reduction): ", mesh_smp12)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD12.obj", mesh_smp12)


mesh_smp13 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.26875))
)
print("Simplification Stage 13 (5.623%*13 reduction): ", mesh_smp13)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD13.obj", mesh_smp13)


mesh_smp14 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.2125))
)
print("Simplification Stage 14 (5.623%*14 reduction): ", mesh_smp14)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD14.obj", mesh_smp14)


mesh_smp15 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.15625))
)   
print("Simplification Stage 15 (5.623%*15 reduction): ", mesh_smp15)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD15.obj", mesh_smp15)


mesh_smp16 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=(int(totaltris*0.1))
)
print("Simplification Stage 16 (5.623%*16 reduction): ", mesh_smp16)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj", mesh_smp16)