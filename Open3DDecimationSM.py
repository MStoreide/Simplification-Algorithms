#Decimation of SM
import open3d as o3d

#Note that open3d requires version 3.10 of Python. 

#Can change this to taking it from the project folder instead. Mesh needs to be manifold and triangulated.
SMbase = o3d.io.read_triangle_mesh(r"D:\Datasets\Paper_Simplification\Blender_Topology_Deform\NUM_Randomized.obj")
SMbase.compute_vertex_normals()
print(SMbase)

print("Before simplification:", SMbase)
#o3d.visualization.draw_geometries([SMbase]) This can be added later. Visualizing all stages.

#Starting simplification, going through 16 stages. This should be written as a function or a loop to make the code cleaner and easier to use for other objects.
#This comes later perhaps.

mesh_smp1 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=242549
)
print("Simplification Stage 1 (5.623% reduction): ", mesh_smp1)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD1.obj", mesh_smp1)


mesh_smp2 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=228093
)
print("Simplification Stage 2 (5.623%*2 reduction): ", mesh_smp2)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD2.obj", mesh_smp2)


mesh_smp3 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=213636
)
print("Simplification Stage 3 (5.623%*3 reduction): ", mesh_smp3)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD3.obj", mesh_smp3)


mesh_smp4 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=199179
) 
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD4.obj", mesh_smp4)


mesh_smp5 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=184723
)
print("Simplification Stage 5 (5.623%*5 reduction): ", mesh_smp5)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD5.obj", mesh_smp5)


mesh_smp6 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=170266
)
print("Simplification Stage 6 (5.623%*6 reduction): ", mesh_smp6)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD6.obj", mesh_smp6)


mesh_smp7 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=155746
)
print("Simplification Stage 7 (5.623%*7 reduction): ", mesh_smp7)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD7.obj", mesh_smp7)


mesh_smp8 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=141353
)
print("Simplification Stage 8 (5.623%*8 reduction): ", mesh_smp8)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD8.obj", mesh_smp8)


mesh_smp9 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=126703
)
print("Simplification Stage 9 (5.623%*9 reduction): ", mesh_smp9)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD9.obj", mesh_smp9)


mesh_smp10 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=112312
)
print("Simplification Stage 10 (5.623%*10 reduction): ", mesh_smp10)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD10.obj", mesh_smp10)


mesh_smp11 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=97918
)
print("Simplification Stage 11 (5.623%*11 reduction): ", mesh_smp11)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD11.obj", mesh_smp11)


mesh_smp12 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=83527
)
print("Simplification Stage 12 (5.623%*12 reduction): ", mesh_smp12)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD12.obj", mesh_smp12)


mesh_smp13 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=68876
)
print("Simplification Stage 13 (5.623%*13 reduction): ", mesh_smp13)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD13.obj", mesh_smp13)


mesh_smp14 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=54484
)
print("Simplification Stage 14 (5.623%*14 reduction): ", mesh_smp14)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD14.obj", mesh_smp14)


mesh_smp15 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=40092
)   
print("Simplification Stage 15 (5.623%*15 reduction): ", mesh_smp15)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD15.obj", mesh_smp15)


mesh_smp16 = SMbase.simplify_quadric_decimation(
    target_number_of_triangles=25700
)
print("Simplification Stage 16 (5.623%*16 reduction): ", mesh_smp16)
o3d.io.write_triangle_mesh(r"D:\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj", mesh_smp16)

#Add a function that draws all the meshes side by side? Or at least gives images in a folder. 

# Add C++ binding to call Metro information directly in this code? With invoke. 
# Meshlab Hausdorff integration as well?
# Metro has a CLI alternative, so perhaps viable. Might be easier to extract data as well. See if one can export directly to csv. 
# Could then do all of the statistics here, with pandas, as well instead of excel.