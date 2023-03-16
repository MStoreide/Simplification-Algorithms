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

# Baseline object

objBaseArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMB.txt", skiprows = (4), max_rows=(16816), usecols=(1,2,3))
objBaseDF = pd.DataFrame(objBaseArray, columns=['X', 'Y', 'Z'])

print(f"Base OBJ has {len(objBaseArray)} vertices")

objBaseDF['X'].mean

#Simplified

objSimpArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.txt", skiprows = (4), max_rows=(1687), usecols=(1,2,3)) #1687 are all the vertices. Code to only go this far, Index 0 = v
objSimpDF = pd.DataFrame(objSimpArray, columns = ['X','Y','Z'])
#vertexnum = len(objArray) # Function could be here

print(f"Simp OBJ has {len(objSimpArray)} vertices")

print(f"Baseline: Mean of X coordinates =", {objBaseDF['X'].mean()})

print(f"Simplification 16: Mean of X coordinates", {objSimpDF["X"].mean()})

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
print("X max base = ", X_maxdiff)
print("Y max base = ", Y_maxdiff)
print("Z max base = ", Z_maxdiff)

X_maxdiffsimp = maxDiff(objSimpDF['X'])
Y_maxdiffsimp = maxDiff(objSimpDF['Y'])
Z_maxdiffsimp = maxDiff(objSimpDF['Z'])
print("X max simp = ", X_maxdiff)
print("Y max simp = ", Y_maxdiff)
print("Z max simp = ", Z_maxdiff)

#Check differences in maxDiff

if (X_maxdiffbase) == (X_maxdiffsimp):
    print("Max difference in X coordinates is equal to the baseline")
else:
    print("Max difference in X coordinates from baseline =", X_maxdiffbase - X_maxdiffsimp)
    X_diff = X_maxdiffbase - X_maxdiffsimp

if (Y_maxdiffbase) == (Y_maxdiffsimp):
    print("Max difference in Y coordinates is equal to the baseline")
else:
    print("Max difference in Y coordinates from baseline =", Y_maxdiffbase - Y_maxdiffsimp)
    Y_diff = Y_maxdiffbase - Y_maxdiffsimp

if (Z_maxdiffbase) == (Z_maxdiffsimp):
    print("Max difference in Z coordinates is equal to the baseline")
else:
    print("Max difference in Z coordinates from baseline =", Z_maxdiffbase - Z_maxdiffsimp)
    Z_diff = Z_maxdiffbase - Z_maxdiffsimp
