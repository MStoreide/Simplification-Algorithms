import open3d as o3d
import pandas as pd

help(o3d)

#print("Reading Point Cloud")

#pc = o3d.io.read_point_cloud("Filepath")

# print(pc)

#What info do we want?
# - Bounding Box
# - RGB Values
# - List array for inspection
# - Different segments, taken either from xyz or rgb
# - Distance between selected points (min, max, mean)
# - Different clustering approaches 
# - Plane segmentation