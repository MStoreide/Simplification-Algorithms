import pymeshlab as pym
import numpy as np
import matplotlib as plt

#Using pymeshlab, we apply the Hausdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

output_path = (r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Hausdorff_CSV\Hausdorff_CSV')

ms = pym.MeshSet() # Creates a container where we can load our meshes into.

ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD1.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD2.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD3.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD4.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD5.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD6.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD7.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD8.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD9.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD10.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD11.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD12.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD13.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD14.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD15.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

baseline = ms.current_mesh() #Fix this if creating a function
print("Current mesh is: ", (ms.current_mesh_id()))


samples = baseline.face_number()
print(f"Current mesh has", samples, "faces")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 0, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD1.csv')
print("Applied Hausdorff Filter to SMD1.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 1, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD2.csv')
print("Applied Hausdorff Filter to SMD2.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 2, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD3.csv')
print("Applied Hausdorff Filter to SMD3.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 3, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD4.csv')
print("Applied Hausdorff Filter to SMD4.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 4, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD5.csv')
print("Applied Hausdorff Filter to SMD5.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 5, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD6.csv')
print("Applied Hausdorff Filter to SMD6.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 6, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD7.csv')
print("Applied Hausdorff Filter to SMD7.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 7, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD8.csv')
print("Applied Hausdorff Filter to SMD8.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 8, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD9.csv')
print("Applied Hausdorff Filter to SMD9.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 9, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD10.csv')
print("Applied Hausdorff Filter to SMD10.obj")

#Hausdorff 1

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 10, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD11.csv')
print("Applied Hausdorff Filter to SMD11.obj")

#Hausdorff 12

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 11, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD12.csv')
print("Applied Hausdorff Filter to SMD12.obj")

#Hausdorff 13

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 12, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD13.csv')
print("Applied Hausdorff Filter to SMD13.obj")

#Hausdorff 14

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 13, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD14.csv')
print("Applied Hausdorff Filter to SMD14.obj")

#Hausdorff 15

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 14, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD15.csv')
print("Applied Hausdorff Filter to SMD15.obj")


#Hausdorff 16

ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 15, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
ms.save_filter_script(output_path + '_SMD16.csv')
print("Applied Hausdorff Filter to SMD16.obj")
