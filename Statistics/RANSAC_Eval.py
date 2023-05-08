import pyransac3d as pyrsc 

points = np.loadtxt((r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\OBJ_Arrays\SMB.txt'),
                        skiprows = (4), 
                        max_rows = (16816),
                        usecols=(1,2,3))

sph = pyrsc.Sphere()
center, radius, inliers, = sph.fit(points, thresh=0.4)
print(center, radius, inliers)