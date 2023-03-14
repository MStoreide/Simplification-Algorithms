import os
import numpy as np

#objdir = ("Directory") #Directory for objs

#objdirlist os.listdir('objdir')

# for f in objdirlist:
#        base = os.path.splitext(f)[0]
#        os.rename(f, base + ".txt")


objFile = (r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.obj")
base = os.path.splitext(objFile)[0]
os.rename(objFile, base + ".txt")

objArray = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.txt", skiprows = (4), usecols=(1,2,3))
print(len(objArray))

# value : int

#For loop to print something?

#for value in (objArray):
#    if value >= int(1):
#        print(value)



