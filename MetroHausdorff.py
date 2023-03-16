import pymeshlab as pym
import numpy as np
import matplotlib as plt

#Using pymeshlab, we apply the Hausdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

output_path = ('/home/markus/Pictures/')

ms = pym.MeshSet() # Creates a container where we can load our meshes into.
ms.load_new_mesh('SMD16.obj')
ms.load_new_mesh('SMB.obj')

baseline = ms.current_mesh() #Fix this

print("Current mesh is: ", (ms.current_mesh_id()))

samples = baseline.face_number()

print(f"Current mesh has", samples, "faces")

print(ms.get_hausdorff_distance(sampledmesh = 1, targetmesh = 0, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50)))

ms.save_filter_script(output_path + 'test_saved_script.csv')
