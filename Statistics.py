import os
import shutil
import numpy as np
import pandas as pd
import matplotlib as plt
import pymeshlab as pym


#objdir = ("Directory") #Directory for objs

#objdirlist os.listdir('objdir')

# Copy obj to "Copy" directory, Rename original to .txt

#objFile = (r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.obj")
#dst = ("G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays")
#base = os.path.splitext(objFile)[0]
#objCopy = shutil.copyfile(objFile, dst)
#copyfile = os.rename(objFile, base + "Copy.obj")
#os.rename(objFile, base + ".txt")

## Object Information ##

# Baseline object

objBaseArray = np.loadtxt(r"smb://forskning.it.ntnu.no/ntnu/ie/idi/colorlab/Personal/marksto/Paper_Simplification/OBJ_Arrays/NUMB.txt", skiprows = (4), max_rows=(261174), usecols=(1,2,3))
objBaseArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\NUMB.txt",
                        skiprows = (4), 
                        max_rows=(261174), 
                        usecols=(1,2,3))
objBaseDF = pd.DataFrame(objBaseArray, columns=['X', 'Y', 'Z'])

print(f"Base OBJ has {len(objBaseArray)} vertices")

objBaseDF['X'].mean

# Simplified object

objSimpArray = np.loadtxt(r"smb://forskning.it.ntnu.no/ntnu/ie/idi/colorlab/Personal/marksto/Paper_Simplification/OBJ_Arrays/NUMEC16.txt", skiprows = (4), max_rows=(26126), usecols=(1,2,3)) #1687 are all the vertices. Code to only go this far, Index 0 = v
objSimpArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\NUMEC16.txt", 
                        skiprows = (4),
                        max_rows=(26126), 
                        usecols=(1,2,3)) #1687 are all the vertices. Code to only go this far, Index 0 = v
objSimpDF = pd.DataFrame(objSimpArray, columns = ['X','Y','Z'])
#vertexnum = len(objArray) # Function could be here
print(f"Simp OBJ has {len(objSimpArray)} vertices")

#haus = pd.read_csv(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\RDH.csv", usecols=(1,2,3))
#print(haus) 

## General Information ##

# Baseline object
print(f"Baseline: Mean of X coordinates =", {objBaseDF['X'].mean()})
print(f"Baseline: Mean of Y coordinates =", {objBaseDF['Y'].mean()})
print(f"Baseline: Mean of Z coordinates =", {objBaseDF['Z'].mean()})

print(f"Baseline: Median of x coordinates=", {objBaseDF['X'].median()})
print(f"Baseline: Median of Y coordinates=", {objBaseDF['Y'].median()})
print(f"Baseline: Median of Z coordinates=", {objBaseDF['Z'].median()})

# Simplified Object
print(f"Simplification 16: Mean of X coordinates", {objSimpDF["X"].mean()})
print(f"Simplification 16: Mean of Y coordinates", {objSimpDF["Y"].mean()})
print(f"Simplification 16: Mean of Z coordinates", {objSimpDF["Z"].mean()})

print(f"Simplification 16: Median of X coordinates", {objSimpDF["X"].median()})
print(f"Simplification 16: Median of Y coordinates", {objSimpDF["Y"].median()})
print(f"Simplification 16: Median of Z coordinates", {objSimpDF["Z"].median()})

# Pearson Correlations


## Max Difference ##

print("Max Distances of the extremes for a coordinate within an object")

#This function searches for the distance of the extremes for a coordinate within an object.
def maxDiff(a):
    dmin = a[0]
    dmax = 0
    for i in range(len(a)):
        if (a[i] < dmin):
            dmin = a[i]
        elif (a[i] - dmin > dmax):
            dmax = a[i] - dmin
    return dmax

X_maxdiffbase = maxDiff(objBaseDF['X'])
Y_maxdiffbase = maxDiff(objBaseDF['Y'])
Z_maxdiffbase = maxDiff(objBaseDF['Z'])
print("X difference max : base = ", X_maxdiffbase)
print("Y difference max : base = ", Y_maxdiffbase)
print("Z difference max : base = ", Z_maxdiffbase)

X_maxdiffsimp = maxDiff(objSimpDF['X'])
Y_maxdiffsimp = maxDiff(objSimpDF['Y'])
Z_maxdiffsimp = maxDiff(objSimpDF['Z'])
print("X max difference : simp = ", X_maxdiffsimp)
print("Y max difference : simp = ", Y_maxdiffsimp)
print("Z max difference : simp = ", Z_maxdiffsimp)

if (X_maxdiffbase) == (X_maxdiffsimp):
    print("Max difference in X coordinates is equal to the baseline")
else:
    print("Difference in max difference of X coordinates from baseline =", abs(X_maxdiffbase - X_maxdiffsimp))
    X_diff = abs(X_maxdiffbase - X_maxdiffsimp)

if (Y_maxdiffbase) == (Y_maxdiffsimp):
    print("Max difference in Y coordinates is equal to the baseline")
else:
    print("Difference in max difference of Y coordinates from baseline =", abs(Y_maxdiffbase - Y_maxdiffsimp))
    Y_diff = abs(Y_maxdiffbase - Y_maxdiffsimp)

if (Z_maxdiffbase) == (Z_maxdiffsimp):
    print("Max difference in Z coordinates is equal to the baseline")
else:
    print("Difference in max difference of Z coordinates from baseline =", abs(Z_maxdiffbase - Z_maxdiffsimp))
    Z_diff = abs(Z_maxdiffbase - Z_maxdiffsimp)



## Min Difference ##

#Similar to maxDiff, but returns the smallest distance. Usually 0.




## Segmentation ##

#o3d has some solutions for both objs and plys
#pymeshlab has solutions for plys
#plot them into segmented dataframes

# XYZ Difference Segmentation

# XYZ Similarity Segmentation

# RGB Segmentation from Hausdorff. Segments areas of high error.


# Plotting

objBaseDF.boxplot()
objSimpDF.boxplot()

objBaseDF.plot(x='X', y='Y', style='o', markersize=0.5)
objSimpDF.plot(x='X', y='Y', style='o', markersize=0.5)

objBaseDF.plot(x='Y', y='Z', style='o', markersize=0.5 )
objSimpDF.plot(x='Y', y='Z', style='o', markersize=0.5 )