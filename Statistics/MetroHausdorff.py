import pymeshlab as pym
import numpy as np
import matplotlib as plt
import pandas as pd

#To change object, simply swap the file abbreviation with the correct filename

# Creates a container where we can load our meshes into
ms_SMD = pym.MeshSet()
ms_SMEC = pym.MeshSet()
ms_SMQEM = pym.MeshSet()
ms_SMVC = pym.MeshSet()
ms_SMCFM = pym.MeshSet()

# Load all SMD meshes, with the baseline at the end
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD1.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD2.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD3.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD4.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD5.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD6.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD7.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD8.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD9.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD10.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD11.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD12.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD13.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD14.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD15.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj')
ms_SMD.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')


baseline = ms_SMD.current_mesh()
print("Current mesh is: ", (ms_SMD.current_mesh_id()))

#Sample faces at the total triangle count of the original mesh.
SMD_samples = baseline.face_number()
print(f"Current mesh has", SMD_samples, "faces")

#Hausdorff Distances for each simplificaton stage
SMD_haus1 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 0, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus2 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 1, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus3 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 2, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus4 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 3, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus5 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 4, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus6 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 5, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus7 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 6, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus8 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 7, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus9 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 8, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus10 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 9, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus11 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 10, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus12 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 11, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus13 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 12, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus14 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 13, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus15 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 14, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus16 = ms_SMD.get_hausdorff_distance(sampledmesh = 16, targetmesh = 15, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))

#Hausdoff Dataframes for each simplification stage
SMD_haus1DF = pd.DataFrame.from_dict(SMD_haus1, orient='index', columns=['SMD1'])
SMD_haus2DF = pd.DataFrame.from_dict(SMD_haus2, orient='index', columns=['SMD2'])
SMD_haus3DF = pd.DataFrame.from_dict(SMD_haus3, orient='index', columns=['SMD3'])
SMD_haus4DF = pd.DataFrame.from_dict(SMD_haus4, orient='index', columns=['SMD4'])
SMD_haus5DF = pd.DataFrame.from_dict(SMD_haus5, orient='index', columns=['SMD5'])
SMD_haus6DF = pd.DataFrame.from_dict(SMD_haus6, orient='index', columns=['SMD6'])
SMD_haus7DF = pd.DataFrame.from_dict(SMD_haus7, orient='index', columns=['SMD7'])
SMD_haus8DF = pd.DataFrame.from_dict(SMD_haus8, orient='index', columns=['SMD8'])
SMD_haus9DF = pd.DataFrame.from_dict(SMD_haus9, orient='index', columns=['SMD9'])
SMD_haus10DF = pd.DataFrame.from_dict(SMD_haus10, orient='index', columns=['SMD10'])
SMD_haus11DF = pd.DataFrame.from_dict(SMD_haus11, orient='index', columns=['SMD11'])
SMD_haus12DF = pd.DataFrame.from_dict(SMD_haus12, orient='index', columns=['SMD12'])
SMD_haus13DF = pd.DataFrame.from_dict(SMD_haus13, orient='index', columns=['SMD13'])
SMD_haus14DF = pd.DataFrame.from_dict(SMD_haus14, orient='index', columns=['SMD14'])
SMD_haus15DF = pd.DataFrame.from_dict(SMD_haus15, orient='index', columns=['SMD15'])
SMD_haus16DF = pd.DataFrame.from_dict(SMD_haus16, orient='index', columns=['SMD16'])

# Append the values from each simplification stage to the same dataframe. 
SMD_haus1DF['SMD2'] = SMD_haus2DF['SMD2'].values
SMD_haus1DF['SMD3'] = SMD_haus3DF['SMD3'].values
SMD_haus1DF['SMD4'] = SMD_haus4DF['SMD4'].values
SMD_haus1DF['SMD5'] = SMD_haus5DF['SMD5'].values
SMD_haus1DF['SMD6'] = SMD_haus6DF['SMD6'].values
SMD_haus1DF['SMD7'] = SMD_haus7DF['SMD7'].values
SMD_haus1DF['SMD8'] = SMD_haus8DF['SMD8'].values
SMD_haus1DF['SMD9'] = SMD_haus9DF['SMD9'].values
SMD_haus1DF['SMD10'] = SMD_haus10DF['SMD10'].values
SMD_haus1DF['SMD11'] = SMD_haus11DF['SMD11'].values
SMD_haus1DF['SMD12'] = SMD_haus12DF['SMD12'].values
SMD_haus1DF['SMD13'] = SMD_haus13DF['SMD13'].values
SMD_haus1DF['SMD14'] = SMD_haus14DF['SMD14'].values
SMD_haus1DF['SMD15'] = SMD_haus15DF['SMD15'].values
SMD_haus1DF['SMD16'] = SMD_haus16DF['SMD16'].values

#Copy and Transpose the data into a new Dataframe
hausDF = haus1DF.T

#hausDF.plot(legend=True, subplots=True, title='Hausdorff Values SMD')
#Fix for better plots

ms_SMD.set_current_mesh(18) #This works, just need to figure out the damn names
ms_SMD.save_current_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Hausdorff_Script\HausSMD1.ply', binary=False)

def vertexinfo(pointcloud):
    for pointcloud in range(len(ms_SMD)):
        vsa = ms_SMD.mesh(pointcloud).vertex_scalar_array()
        vca = ms_SMD.mesh(pointcloud).vertex_color_array()
        print('Vertex Scalar Array:', vsa)
        print('Vertex Color Array:', vca)
    return (vsa, vca)

vertexinfo(ms_SMD)

# can we make it into a dataframe?

MeshSet = pd.DataFrame(ms_SMD) #Does not give object names


#vertexinfo(17)

#vq18s = ms_SMD.mesh(18).vertex_scalar_array()
#vq18c = ms_SMD.mesh(18).vertex_color_array()

ms_SMD.set_verbosity(True)
print(ms_SMD.print_status())

ms_SMD.show_polyscope()

# Loading PLYs again

# HausPLY1 = pd.read(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Hausdorff_Script\HausSMD1.ply', 
#                        columns = ['X','Y','Z', 'R', 'G' 'B', 'Alpha', 'Quality']
#                        )
