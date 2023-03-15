import os
import shutil
import numpy as np
import pandas as pd
import matplotlib as plt


#objdir = ("Directory") #Directory for objs

#objdirlist os.listdir('objdir')

# for f in objdirlist:
#        base = os.path.splitext(f)[0]
#        os.rename(f, base + ".txt")


# Copy obj to "Copy" directory, Rename original to .txt

#  objFile = (r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.obj")
#dst = ("G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays")
#  base = os.path.splitext(objFile)[0]
#objCopy = shutil.copyfile(objFile, dst)
#copyfile = os.rename(objFile, base + "Copy.obj")
#  os.rename(objFile, base + ".txt")

# Baseline object

objBaseArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMB.txt", skiprows = (4), max_rows=(16816), usecols=(1,2,3))
objBaseDF = pd.DataFrame(objBaseArray, columns=['X', 'Y', 'Z'])

print(f"Base OBJ has {len(objBaseArray)} vertices")

objBaseDF['X'].mean

#Simplified

objSimpArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.txt", skiprows = (4), max_rows=(1687), usecols=(1,2,3)) #1687 are all the vertices. Code to only go this far, Index 0 = v
objSimpDF = pd.DataFrame(objSimpArray, columns = ['X','Y','Z'])
#vertexnum = len(objArray) # Function could be here

print(f"Simp OBJ has {len(objArray)} vertices")

print(f"Baseline: Mean of X coordinates =", {objBaseDF['X'].mean()})

print(f"Simplification 16: Mean of X coordinates", {objSimpDF["X"].mean()})


#For loop to print something?

#for value in (objArray):
#    if value >= int(1):
#        print(value)

#objArray.plot()
#plt.show()

objBaseDF[objBaseDF["X"] > 1]

# Not Working

def maxDiff(a):
    vmin = a[0]
    dmax = 0
    for i in range(len(a)):
        if (a[i] < vmin):
            vmin = a[i]
        elif (a[i] - vmin > dmax):
            dmax = a[i] - vmin
    return dmax

maxDiff(objBaseArray)


