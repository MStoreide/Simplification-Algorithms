import numpy as np

Test = np.loadtxt(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\OBJ Arrays\SMEC16.txt", skiprows = (4), max_rows = (500), usecols=(1,2,3))

print(Test[3])



