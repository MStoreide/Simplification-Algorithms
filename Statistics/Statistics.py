import os
import sys
import shutil
import numpy as np
import pandas as pd
import matplotlib as plt
import pymeshlab as pym
import open3d as o3d

## Introduction ##
#################################################################################################################


# This file includes code from several different scripts, utilizing all functions in the same environment. 
# I can then make changes to individual scripts without working in this environment
# - Hausdorff distances from MetroHausdorff.py
# - PLY Inspections from PLYInspection.py

# It also relies on data created from other scripts, primarily the simplification algorithms.
# Filepaths are currently hardcoded, meaning that the user must change the directories before running

## Checklist ##
#################################################################################################################
# To check that everything is done, we follow this checklist. All start as false, and 

checklist = {'Copy .objs as .txts' : 'False',
            'Convert .txts to Dataframes' : 'False',
            'Extract and Print General Object Info' : 'False',
            'Pearson Correlations' : 'False',
            'Spearman Correlations' : 'False',
            'Hausdorff for Decimation' : 'False',


            
}


## Converting OJBs to TXTs ##
#################################################################################################################

# Pandas does not allow us to work with *.OBJ files directly, but we can convert them to *.TXTs safely without loosing any information.
# These can be read as dataframes. 

# Copies *.obj's to *.txt directory
#src_dir = r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Vertex_Clustering\NUMVC"
dst_dir = r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT"
#shutil.copy2(src_dir, dst_dir)

# Converts copied *.obj's to *.txt's
for filename in os.listdir(dst_dir):
    infilename = os.path.join(dst_dir,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.obj', '.txt')
    output = os.rename(infilename, newname)





## ObjectLoading ##
#################################################################################################################

# Function for loading all txts to separate dataframes should be added

# Baseline object

# Need to find way to only load vertices. Can also load everyting, and then filter out everything else but vertices. Rows starting with ONLY 'v'

#Baseline
#objBaseArray = np.loadtxt(r"smb://forskning.it.ntnu.no/ntnu/ie/idi/colorlab/Personal/marksto/Paper_Simplification/OBJ_Arrays/NUMB.txt",
#                          skiprows = (4), 
#                          max_rows=(261174),
#                          usecols=(1,2,3))

obj_dataframes = []
objBaseArray = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT\NUMB.txt",
                        skiprows = (4), 
                        max_rows=(261174), 
                        usecols=(1,2,3))
objBaseDF = pd.DataFrame(objBaseArray, columns=['X', 'Y', 'Z'])

obj_dataframes.Append[objBaseDF]

print(f"Base OBJ has {len(objBaseArray)} vertices")

# Simplified object 1
objSimp1Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT\NUMEC1.txt", 
                        skiprows = (4),
                        max_rows=(246483), 
                        usecols=(1,2,3))
objSimp1DF = pd.DataFrame(objSimp1Array, columns = ['X','Y','Z'])

print(f"Simp1 OBJ has {len(objSimp1Array)} vertices")
obj_dataframes.Append(objSimp1DF)

# Simplified object 2
objSimp2Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT\NUMEC2.txt", 
                        skiprows = (4),
                        max_rows=(231793), 
                        usecols=(1,2,3))
objSimp2DF = pd.DataFrame(objSimp2Array, columns = ['X','Y','Z'])

print(f"Simp1 OBJ has {len(objSimp2Array)} vertices")
obj_dataframes.Append(objSimp2DF)

# Simplified object 3
objSimp3Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT\NUMEC3.txt", 
                        skiprows = (4),
                        max_rows=(217102), 
                        usecols=(1,2,3))
objSimp3DF = pd.DataFrame(objSimp3Array, columns = ['X','Y','Z'])

print(f"Simp1 OBJ has {len(objSimp3Array)} vertices")
obj_dataframes.Append(objSimp3DF)

# Simplified object 4
objSimp4Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT\NUMEC4.txt", 
                        skiprows = (4),
                        max_rows=(202412), 
                        usecols=(1,2,3))
objSimp4DF = pd.DataFrame(objSimp4Array, columns = ['X','Y','Z'])

print(f"Simp1 OBJ has {len(objSimp4Array)} vertices")
obj_dataframes.Append(objSim43DF)

# Simplified object 5
objSimp5Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT\NUMEC5.txt", 
                        skiprows = (4),
                        max_rows=(187721), 
                        usecols=(1,2,3))
objSimp5DF = pd.DataFrame(objSimp5Array, columns = ['X','Y','Z'])

print(f"Simp1 OBJ has {len(objSimp5Array)} vertices")
obj_dataframes.Append(objSimp5DF)

# Simplified object 6
objSimp6Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC_TXT\NUMEC6.txt", 
                        skiprows = (4),
                        max_rows=(173031), 
                        usecols=(1,2,3))
objSimp6DF = pd.DataFrame(objSimp6Array, columns = ['X','Y','Z'])

print(f"Simp6 OBJ has {len(objSimp6Array)} vertices")
obj_dataframes.Append(objSimp6DF)

# Simplified object 7
objSimp7Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC7.txt", 
                        skiprows = (4),
                        max_rows=(158340), 
                        usecols=(1,2,3))
objSimp7DF = pd.DataFrame(objSimp7Array, columns = ['X','Y','Z'])

print(f"Simp7 OBJ has {len(objSimp7Array)} vertices")
obj_dataframes.Append(objSimp7DF)

# Simplified object 16
objSimp16Array = np.loadtxt(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\NUMEC16.txt", 
                        skiprows = (4),
                        max_rows=(26126), 
                        usecols=(1,2,3))
objSimp16DF = pd.DataFrame(objSimp16Array, columns = ['X','Y','Z'])

print(f"Simp16 OBJ has {len(objSimp16Array)} vertices")
obj_dataframes.Append(objSimp16DF)


checklist['Convert .txts to Dataframes'] = 'True'



## General Object Information ##
#################################################################################################################
#- Mean Triangle size
#                        - Max Triangle size
#                        - Min Triangle size
#                        - Number of triangles
#Means and Medians

def means(DataFrame):
    for column in DataFrame:
        xmean = DataFrame["X"].mean()
        ymean = DataFrame["Y"].mean()
        zmean = DataFrame["Z"].mean()
    return xmean, ymean, zmean

def medians(DataFrame):
    for column in DataFrame:
        xmedian = DataFrame["X"].median()
        ymedian = DataFrame["Y"].median()
        zmedian = DataFrame["Z"].median()
    return xmedian, ymedian, zmedian

print("\n")
print("Means and Medians")

# Baseline object
print("Baseline Object:")
print("Means", means(objBaseDF))
print("Means", medians(objBaseDF))

# Simplified Object 1
print("Simplification Stage 1:")
print("Means", means(objSimp1DF))
print("Medians", medians(objSimp1DF))

# Simplified Object 7
print("Simplification Stage 7:")
print("Means", means(objSimp7DF))
print("Medians", medians(objSimp7DF))

# Simplified Object 16
print("Simplification Stage 16:")
print("Means", means(objSimp16DF))
print("Medians", medians(objSimp16DF))


# Pearson Correlations
def percor(DataFrame):
    for column in DataFrame:
        percorcof = objBaseDF.corrwith(DataFrame, method='pearson')
    return percorcof

percor1 = percor(objSimp1DF)
percor2 = percor(objSimp2DF)
percor3 = percor(objSimp3DF)
percor4 = percor(objSimp4DF)
percor5 = percor(objSimp5DF)
percor6 = percor(objSimp6DF)
percor7 = percor(objSimp7DF) #Add the rest
percor16 = percor(objSimp16DF)
print("Pearson Correlation Coefficients: ",
                                "1:", percor1,
                                "2:", percor2, 
                                "3:", percor3, 
                                "4:", percor4, 
                                "5:", percor5, 
                                "6:", percor6,  
                                "7:", percor7, 
                                "16:",percor16)

pearsonsDF = pd.concat([percor1, percor2, percor3, percor4, percor5, percor6, percor7, percor16], axis=1)
pearsonsXYZ = pearsonsDF.T
pearsonsXYZ.plot(legend=True, subplots=True, title='Pearson Correlation Coefficients') #Check size
#Should also be summarized in a final dataframe.


# Spearman Correlations
def sprcor(DataFrame):
    for column in DataFrame:
        sprcorcof = objBaseDF.corrwith(DataFrame, method='spearman')
    return sprcorcof

sprcor1 = sprcor(objSimp1DF)
sprcor2 = sprcor(objSimp2DF)
sprcor3 = sprcor(objSimp3DF)
sprcor4 = sprcor(objSimp4DF)
sprcor5 = sprcor(objSimp5DF)
sprcor6 = sprcor(objSimp6DF)
sprcor7 = sprcor(objSimp7DF) #Add the rest
sprcor16 = sprcor(objSimp16DF)
print("Spearman Correlation Coeffcients: ", 
                                "1:", sprcor1,
                                "2:", sprcor2,
                                "3:", sprcor3,
                                "4:", sprcor4,
                                "5:", sprcor5,
                                "6:", sprcor6, 
                                "7:", sprcor7,
                                "16:", sprcor16)

spearmansDF = pd.concat([sprcor1, sprcor2, sprcor3, sprcor4, sprcor5, sprcor6, sprcor7, sprcor16], axis=1)
spearmansXYZ = spearmansDF.T
spearmansXYZ.plot(legend=True, subplots=True, title="Spearman Correlation Coefficients") #Check size

#Should also be summarized in a final dataframe.







## Max Difference ##
#################################################################################################################

print("\n")
print("Max Distances of the extremes for a coordinate within an object")

#This function searches for the distance of the extremes for a coordinate within an object.
def maxDiff(a):
    dmin = a[0] # Need negative values for this
    dmax = 0
    for i in range(len(a)):
        if (a[i] < dmin):
            dmin = a[i]
        elif (a[i] - dmin > dmax):
            dmax = a[i] - dmin
    return dmax

# Baseline Distances
X_maxdiffbase = maxDiff(objBaseDF['X'])
Y_maxdiffbase = maxDiff(objBaseDF['Y'])
Z_maxdiffbase = maxDiff(objBaseDF['Z'])
print("X difference max : base = ", X_maxdiffbase)
print("Y difference max : base = ", Y_maxdiffbase)
print("Z difference max : base = ", Z_maxdiffbase)


print("\n")
# Simplification Stage 1 Distances
X_maxdiffsimp = maxDiff(objSimp1DF['X'])
Y_maxdiffsimp = maxDiff(objSimp1DF['Y'])
Z_maxdiffsimp = maxDiff(objSimp1DF['Z'])
print("X max difference : simp = ", X_maxdiffsimp)
print("Y max difference : simp = ", Y_maxdiffsimp)
print("Z max difference : simp = ", Z_maxdiffsimp)

if (X_maxdiffbase) == (X_maxdiffsimp):
    print("Max difference in X coordinates in objSimp1 is equal to the baseline")
else:
    print("Difference in max difference of X coordinates in objSimp1 from baseline =", abs(X_maxdiffbase - X_maxdiffsimp))
    X_diff = abs(X_maxdiffbase - X_maxdiffsimp)

if (Y_maxdiffbase) == (Y_maxdiffsimp):
    print("Max difference in Y coordinates in objSimp1 is equal to the baseline")
else:
    print("Difference in max difference of Y coordinates in objSimp1 from baseline =", abs(Y_maxdiffbase - Y_maxdiffsimp))
    Y_diff = abs(Y_maxdiffbase - Y_maxdiffsimp)

if (Z_maxdiffbase) == (Z_maxdiffsimp):
    print(f"Max difference in Z coordinates in objSimp1 is equal to the baseline")
else:
    print("Difference in max difference of Z coordinates in objSimp1 from baseline =", abs(Z_maxdiffbase - Z_maxdiffsimp))
    Z_diff = abs(Z_maxdiffbase - Z_maxdiffsimp)





## Min Difference ##
#################################################################################################################

#Similar to maxDiff, but returns the smallest distance. Usually 0.
def minDiff(a):
    dmin = a[0]
    for i in range(len(a)): # See if it returns negative values. IF not, it does not work. 
        if (a[i] < dmin):
            dmin = a[i]
    return dmin

print("\n")
print("Minimum Distances of the extremes for a coordinate within an object")

X_mindiffbase = minDiff(objBaseDF['X'])
Y_mindiffbase = minDiff(objBaseDF['Y'])
Z_mindiffbase = minDiff(objBaseDF['Z'])
print(X_mindiffbase, Y_mindiffbase, Z_mindiffbase)









## Hausdorff Distances ##
#################################################################################################################

# PyMeshLab uses a different framework for loading objects and applying filters, requiring us to load them as *.OBJs instead of *.TXT
# This is why we copied the *.OBJs before converting them to *.TXTs

print("\n")
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

#Transpose the dataframe
hausDF = haus1DF.T
print(hausDF)
hausDF.plot(legend=True, subplots=True, title='Hausdorff Values SMD')

#Fix for better plots








## PLY Inspection ##
#################################################################################################################










## Segmentation ##
#################################################################################################################

#o3d has some solutions for both objs and plys
#pymeshlab has solutions for plys
#plot them into segmented dataframes

# XYZ Difference Segmentation

#Google segmentation algorithms

# XYZ Similarity Segmentation

# RGB Segmentation from Hausdorff. Segments areas of high error.
#haus = pd.read_csv(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\RDH.csv", usecols=(1,2,3))
#print(haus) 

#Select the bluest vertex(the one witht the most error), and iterate outwards.
#Can set threshold from there. Get colors from Meshlab slider. 
#Overlap this data with the other segmentations to see similarities. 




# Plotting

#objBaseDF.boxplot()
#objSimpDF.boxplot()

#objBaseDF.plot(x='X', y='Y', style='o', markersize=0.5)
#objSimpDF.plot(x='X', y='Y', style='o', markersize=0.5)

#objBaseDF.plot(x='Y', y='Z', style='o', markersize=0.5 )
#objSimp1DF.plot(x='Y', y='Z', style='o', markersize=0.5 )




## Finalized Dataframes ##
#Final dataframe for each object, listing all information. PDF format?


print(checklist)
# Separately print things that are still false in the checklist