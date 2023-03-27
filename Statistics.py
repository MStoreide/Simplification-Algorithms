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
meanBaseX = objBaseDF['X'].mean()
meanBaseY = objBaseDF['Y'].mean()
meanBaseZ = objBaseDF['Z'].mean()
print(f"Baseline: Mean of X coordinates =", meanBaseX)
print(f"Baseline: Mean of Y coordinates =", meanBaseY)
print(f"Baseline: Mean of Z coordinates =", meanBaseZ)

medianBaseX = objBaseDF['X'].median()
medianBaseY = objBaseDF['Y'].median()
medianBaseZ = objBaseDF['Z'].median()
print(f"Baseline: Median of x coordinates=", medianBaseX)
print(f"Baseline: Median of Y coordinates=", medianBaseY)
print(f"Baseline: Median of Z coordinates=", medianBaseZ)

# Simplified Object
meanSimpX = objSimpDF['X'].mean()
meanSimpY = objSimpDF['Y'].mean()
meanSimpZ = objSimpDF['Z'].mean()
medianSimpX = objSimpDF['X'].median()
medianSimpY = objSimpDF['Y'].median()
medianSimpZ = objSimpDF['Z'].median()
print(f"Simplification 16: Mean of X coordinates", meanSimpX)
print(f"Simplification 16: Mean of Y coordinates", meanSimpY)
print(f"Simplification 16: Mean of Z coordinates", meanSimpZ)

medianSimpX = objSimpDF['X'].median()
medianSimpY = objSimpDF['Y'].median()
medianSimpZ = objSimpDF['Z'].median()
print(f"Simplification 16: Median of X coordinates", medianSimpX)
print(f"Simplification 16: Median of Y coordinates", medianSimpY)
print(f"Simplification 16: Median of Z coordinates", medianSimpZ)

# Pearson Correlations
percorX = objBaseDF.corrwith(objSimpDF, axis=0, method="pearson")
percorY = objBaseDF.corrwith(objSimpDF, axis=1, method="pearson")
percorZ = objBaseDF.corrwith(objSimpDF, axis=2, method="pearson")

# Spearman Correlations
sprcorX = objBaseDF.corrwith(objSimpDF, axis=0, method="spearman")
sprcorY = objBaseDF.corrwith(objSimpDF, axis=1, method="spearman")
sprcorZ = objBaseDF.corrwith(objSimpDF, axis=2, method="spearman")


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

#objBaseDF.boxplot()
#objSimpDF.boxplot()

#objBaseDF.plot(x='X', y='Y', style='o', markersize=0.5)
#objSimpDF.plot(x='X', y='Y', style='o', markersize=0.5)

#objBaseDF.plot(x='Y', y='Z', style='o', markersize=0.5 )
#objSimpDF.plot(x='Y', y='Z', style='o', markersize=0.5 )