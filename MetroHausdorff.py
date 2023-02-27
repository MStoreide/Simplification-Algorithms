import pymeshlab as pym

#Hausdorff Distances for each mesh

#Using pymeshlab, we apply the Huasdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

ms =pymeshlab.Meshset()

#pym.load_new_mesh(r"D:\Datasets\Paper_Simplification\Blender_Topology_Deform\SM_Randomized.obj")

pym.get_hausdorff_distance



