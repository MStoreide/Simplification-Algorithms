import open3d as o3d

#THis is the tutorial
if __name__ == "__main__":
    bunny = o3d.data.BunnyMesh()
    mesh_in = o3d.io.read_triangle_mesh(bunny.path)
    mesh_in.compute_vertex_normals()

    print("Before Simplification: ", mesh_in)
    o3d.visualization.draw_geometries([mesh_in])

    voxel_size = max(mesh_in.get_max_bound() - mesh_in.get_min_bound()) / 32
    mesh_smp = mesh_in.simplify_vertex_clustering(
        voxel_size=voxel_size,
        contraction=o3d.geometry.SimplificationContraction.Average)
    print("After Simplification with voxel size =", voxel_size, ":\n", mesh_smp)
    o3d.visualization.draw_geometries([mesh_smp])

#Mine comes here
if __name__ == "__main__":
    NUM = o3d.io.read_triangle_mesh((r"D:\Datasets\Paper_Simplification\Baselines\NUM.obj"))
    NUM.compute_vertex_normals()

    print("Before Simplification: ", NUM)

#    print(NUM.get_max_bound) #To check what it is.

#    print(NUM.get_min_bound) #To check what it is.

    voxel_size = max(NUM.get_max_bound() - NUM.get_min_bound()) / 32 #Fix the size here. What is 32?

    #print(voxel_size) ????

    mesh_smp = NUM.simplify_vertex_clustering(
        voxel_size=voxel_size,
        contraction=o3d.geometry.SimplificationContraction.Average)
    print("After Simplification with voxel size =", voxel_size, ":\n", NUM)
    o3d.io.write_triangle_mesh((r"D:\Datasets\Paper_Simplification\Vertex Clustering\NUMVC1.obj"))

    #Then repeat for all the other meshes. Same as with D