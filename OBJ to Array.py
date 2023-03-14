import os
import shutil
import numpy as np
import pandas as pd
import  matplotlib as plt


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

objArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.txt", skiprows = (4), max_rows=(1687), usecols=(1,2,3)) #1687 are all the vertices. Code to only go this far, Index 0 = v
objDF = pd.DataFrame(objArray, columns = ['X','Y','Z'])
#vertexnum = len(objArray) # Function could be here

print(f"OBJ has {len(objArray)} vertices")

#For loop to print something?

#for value in (objArray):
#    if value >= int(1):
#        print(value)

#objArray.plot()
#plt.show()



