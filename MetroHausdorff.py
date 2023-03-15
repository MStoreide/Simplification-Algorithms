import pymeshlab as pym
import numpy as np

#Using pymeshlab, we apply the Huasdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

ms = pym.MeshSet() # Creates a container where we can load our meshes into.
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

baseline = pym.load_new_mesh('G:\Datasets\Paper_Simplification\Baseline\SM.obj')
simp1 = pym.load_new_mesh('G:\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj')

samples = face_number(baseline)
#Add all 16 meshes here.  

pym.get_hausdorff_distance(baseline, simp1, savesample=True, sampleface=True, samplenum= (samples), maxdist = 50)


# ms.save_current_mesh? ???
