import pymeshlab as pym
import numpy as np
import matplotlib as plt
import pandas as pd

#To change object, simply swap the file abbreviation with the correct filename

# Creates a container where we can load our meshes into
ms = pym.MeshSet()

# Load all meshes, with the baseline at the end
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD1.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD2.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD3.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD4.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD5.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD6.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD7.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD8.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD9.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD10.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD11.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD12.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD13.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD14.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD15.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj')
ms.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

baseline = ms.current_mesh()
print("Current mesh is: ", (ms.current_mesh_id()))

#Sample faces at the total triangle count of the original mesh.
samples = baseline.face_number()
print(f"Current mesh has", samples, "faces")

#Hausdorff Distances for each simplificaton stage
haus1 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 0, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus2 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 1, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus3 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 2, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus4 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 3, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus5 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 4, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus6 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 5, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus7 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 6, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus8 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 7, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus9 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 8, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus10 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 9, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus11 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 10, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus12 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 11, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus13 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 12, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus14 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 13, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus15 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 14, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))
haus16 = ms.get_hausdorff_distance(sampledmesh = 16, targetmesh = 15, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50))

#Hausdoff Dataframes for each simplification stage
haus1DF = pd.DataFrame.from_dict(haus1, orient='index', columns=['SMD1'])
haus2DF = pd.DataFrame.from_dict(haus2, orient='index', columns=['SMD2'])
haus3DF = pd.DataFrame.from_dict(haus3, orient='index', columns=['SMD3'])
haus4DF = pd.DataFrame.from_dict(haus4, orient='index', columns=['SMD4'])
haus5DF = pd.DataFrame.from_dict(haus5, orient='index', columns=['SMD5'])
haus6DF = pd.DataFrame.from_dict(haus6, orient='index', columns=['SMD6'])
haus7DF = pd.DataFrame.from_dict(haus7, orient='index', columns=['SMD7'])
haus8DF = pd.DataFrame.from_dict(haus8, orient='index', columns=['SMD8'])
haus9DF = pd.DataFrame.from_dict(haus9, orient='index', columns=['SMD9'])
haus10DF = pd.DataFrame.from_dict(haus10, orient='index', columns=['SMD10'])
haus11DF = pd.DataFrame.from_dict(haus11, orient='index', columns=['SMD11'])
haus12DF = pd.DataFrame.from_dict(haus12, orient='index', columns=['SMD12'])
haus13DF = pd.DataFrame.from_dict(haus13, orient='index', columns=['SMD13'])
haus14DF = pd.DataFrame.from_dict(haus14, orient='index', columns=['SMD14'])
haus15DF = pd.DataFrame.from_dict(haus15, orient='index', columns=['SMD15'])
haus16DF = pd.DataFrame.from_dict(haus16, orient='index', columns=['SMD16'])

# Append the values from each simplification stage to the same dataframe. 
haus1DF['SMD2'] = haus2DF['SMD2'].values
haus1DF['SMD3'] = haus3DF['SMD3'].values
haus1DF['SMD4'] = haus4DF['SMD4'].values
haus1DF['SMD5'] = haus5DF['SMD5'].values
haus1DF['SMD6'] = haus6DF['SMD6'].values
haus1DF['SMD7'] = haus7DF['SMD7'].values
haus1DF['SMD8'] = haus8DF['SMD8'].values
haus1DF['SMD9'] = haus9DF['SMD9'].values
haus1DF['SMD10'] = haus10DF['SMD10'].values
haus1DF['SMD11'] = haus11DF['SMD11'].values
haus1DF['SMD12'] = haus12DF['SMD12'].values
haus1DF['SMD13'] = haus13DF['SMD13'].values
haus1DF['SMD14'] = haus14DF['SMD14'].values
haus1DF['SMD15'] = haus15DF['SMD15'].values
haus1DF['SMD16'] = haus16DF['SMD16'].values

hausDF = haus1DF.T

hausDF.plot(legend=True, subplots=True, title='Hausdorff Values SMD')
#Fix for better plots