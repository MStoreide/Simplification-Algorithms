import pymeshlab

#Hausdorff Distances for each mesh

#Using pymeshlab, we apply the Huasdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

#   ms = pymeshlab.MeshSet() # Check what this does. 

#baseline = pym.load_new_mesh('D:\Datasets\Paper_Simplification\Baseline\SM.obj')
#simp.1 = pym.load_new_mesh('D:\Datasets\Paper_Simplification\Decimation\SMD.obj') #This is with Decimation. Change to others.
#Add all 16 meshes here.  

#pym.get_hausdorff_distance(
#   baseline : int = 5050050 (Total triangles in THIS mesh) ?
#   simp.1 = int = 40404040 (Total triangles in THIS mesh) ?
#   savesample : bool = True
#   samplevert : bool = False
#   sampleedge : bool = False
#   samplefauxedge : bool = False
#   sampleface : bool = True
#   samplenum : int = (Total triangles in baseline)
#   maxdist : int = 50%
# )

# ms.save_current_mesh? ???


pymeshlab.print_filter_list()



