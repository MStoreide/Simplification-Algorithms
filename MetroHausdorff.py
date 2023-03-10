import pymeshlab as pym
import numpy as np

#Hausdorff Distances for each mesh
#Make sure the pymeshlab conda environment is activated (for Python 3.7)

#Using pymeshlab, we apply the Huasdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

ms = pym.MeshSet() # Creates a container where we can load our meshes into.
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

#baseline = pym.load_new_mesh('G:\Datasets\Paper_Simplification\Baseline\SM.obj')
#simp1 = pym.load_new_mesh('G:\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj')
#Add all 16 meshes here.  

#pym.get_hausdorff_distance(baseline, simp1)
#savesample : bool = True
#sampleface : bool = True
#samplenum : int = (33620) #Total triangles of baseline
#maxdist : int = 50


# ms.save_current_mesh? ???

#Remeber to set current mesh to each simplification stage at each stage. Duplicate the baseline and simplify ut. 
