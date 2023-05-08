import pymeshlab as pym
import numpy as np
import pandas as pd


## Introduction ##
#################################################################################################################

# This script calculates the Hausdorff distances between each simplification stage and its baseline, using the Metro tool from Meshlab.
# All values are put into a Pandas dataframe, and are then joined in a single Pandas Dataframe. 
# Filepaths are currently hardcoded, meaning that the user must change the directories before running

# Load Meshes
#################################################################################################################

#To change object, simply swap the file abbreviation with the correct filename. E.g SM -> RM
# MeshSet creates a container where we can load our meshes into.

ms_D = pym.MeshSet() # Decimation Meshset
ms_EC = pym.MeshSet() # Edge Collapse Meshset
ms_QEM = pym.MeshSet() # Quadric Error Metrics Meshset
ms_VC = pym.MeshSet() # Vertex Clustering Meshset
ms_CFM = pym.MeshSet() # Coplanar Facets Merging Meshset

# Load all Decimation meshes, with the baseline at the end
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD1.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD2.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD3.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD4.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD5.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD6.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD7.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD8.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD9.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD10.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD11.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD12.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD13.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD14.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD15.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Decimation\SMD\SMD16.obj')
ms_D.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

#Load all Edge Collapse meshes, with the baseline at the end
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC1.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC2.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC3.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC4.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC5.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC6.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC7.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC8.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC9.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC10.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC11.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC12.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC13.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC14.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC15.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\EdgeCollapse\SMEC\SMEC16.obj')
# ms_EC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

#Load all Quadric Error Metrics meshes, with the baseline at the end
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM1.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM2.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM3.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM4.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM5.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM6.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM7.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM8.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM9.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM10.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM11.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM12.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM13.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM14.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM15.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\QuadricErrorMetrics\SMQEM\SMQEM16.obj')
# ms_QEM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

#Load all Vertex Clustering meshes, with the baseline at the end
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC1.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC2.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC3.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC4.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC5.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC6.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC7.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC8.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC9.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC10.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC11.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC12.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC13.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC14.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC15.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\VertexClustering\SMVC\SMVC16.obj')
# ms_VC.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')

#Load all Coplanar Facets Merging meshes, with the baseline at the end
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM1.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM2.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM3.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM4.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM5.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM6.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM7.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM8.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM9.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM10.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM11.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM12.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM13.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM14.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM15.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\CoplanarFacetsMerging\SMCFM\SMCFM16.obj')
# ms_CFM.load_new_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')




# Calculate Hausdorff Distances
#################################################################################################################

## Decimation Meshset ##
baseline = ms_D.current_mesh()
print("Current mesh is: ", (ms_D.current_mesh_id())) # Make sure that this is the baseline

#Sample faces at the total triangle count of the original mesh.
SMD_samples = baseline.face_number()
print(f"Baseline mesh has", SMD_samples, "faces")

#Hausdorff Distances for each simplificaton stage. (Could be written as a For loop)
SMD_haus1 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 0, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus2 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 1, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus3 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 2, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus4 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 3, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus5 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 4, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus6 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 5, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus7 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 6, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus8 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 7, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus9 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 8, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus10 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 9, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus11 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 10, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus12 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 11, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus13 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 12, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus14 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 13, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus15 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 14, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))
SMD_haus16 = ms_D.get_hausdorff_distance(sampledmesh = 16, targetmesh = 15, savesample=True, sampleface=True, samplenum = (SMD_samples), maxdist = pym.Percentage(50))

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
hausDF = SMD_haus1DF.T

#hausDF.plot(legend=True, subplots=True, title='Hausdorff Values SMD')
#Fix for better plots

ms_D.set_current_mesh(18) #This works, just need to figure out the damn names






# Export Distances as Point Clouds
#################################################################################################################
# Need to figure out which mesh is which, and then export everything
ms_D.save_current_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Hausdorff_Script\HausSMD1.ply', binary=False)

# Look at this again? How does it work?
def vertexinfo(pointcloud):
    for pointcloud in range(len(ms_D)):
        vsa = ms_D.mesh(pointcloud).vertex_scalar_array()
        vca = ms_D.mesh(pointcloud).vertex_color_array()
        print('Vertex Scalar Array:', vsa)
        print('Vertex Color Array:', vca)
    return (vsa, vca)


#vq18s = ms_D.mesh(18).vertex_scalar_array()
#vq18c = ms_D.mesh(18).vertex_color_array()

ms_D.set_verbosity(True)
print(ms_D.print_status())

ms_D.show_polyscope()

# Loading PLYs again

# HausPLY1 = pd.read(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Hausdorff_Script\HausSMD1.ply', 
#                        columns = ['X','Y','Z', 'R', 'G' 'B', 'Alpha', 'Quality']
#                        )
ms_D.__str__