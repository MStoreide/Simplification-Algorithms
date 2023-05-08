import pyransac3d as pyrsc
import open3d as o3d
import numpy as np
import pandas as pd

b_points = pd.read_csv((r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\SMB.txt'),
                        skiprows= (4),
                        usecols= (1,2,3))

#sph = pyrsc.Sphere()
#center, radius, inliers = sph.fit(b_points, thresh=0.4)
#print("Baseline: ", center, radius, inliers)