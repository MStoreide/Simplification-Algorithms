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

# 

# It also relies on data created from other scripts, primarily the simplification algorithms.
# Filepaths are currently hardcoded, meaning that the user must change the directories before running



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


# Spearman Correlations (Want to add a different method for getting the sprcor between each stage and its previous)
def sprcor_baseline(DataFrame):
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