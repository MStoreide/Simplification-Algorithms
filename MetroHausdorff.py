import pymeshlab as pym
import numpy as np
import matplotlib as plt

#Using pymeshlab, we apply the Hausdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

output_path = ('/home/markus/Pictures/')

ms = pym.MeshSet() # Creates a container where we can load our meshes into.

ms.load_new_mesh('SMD1.obj')
ms.load_new_mesh('SMD2.obj')
ms.load_new_mesh('SMD3.obj')
ms.load_new_mesh('SMD4.obj')
ms.load_new_mesh('SMD5.obj')
ms.load_new_mesh('SMD6.obj')
ms.load_new_mesh('SMD7.obj')
ms.load_new_mesh('SMD8.obj')
ms.load_new_mesh('SMD9.obj')
ms.load_new_mesh('SMD10.obj')
ms.load_new_mesh('SMD11.obj')
ms.load_new_mesh('SMD12.obj')
ms.load_new_mesh('SMD13.obj')
ms.load_new_mesh('SMD14.obj')
ms.load_new_mesh('SMD15.obj')
ms.load_new_mesh('SMD16.obj')
ms.load_new_mesh('SMB.obj')

baseline = ms.current_mesh() #Fix this

print("Current mesh is: ", (ms.current_mesh_id()))

samples = baseline.face_number()

print(f"Current mesh has", samples, "faces")

print(ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 15, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50)))

ms.save_filter_script(output_path + 'test_saved_script.csv')
