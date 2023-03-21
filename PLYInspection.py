import open3d as o3d
import pandas as pd
import numpy as np

print("Reading Point Cloud")

pc = o3d.io.read_point_cloud(r"G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Metro Data\U PointClouds\UMD\UMD16.ply")

print(pc)
print(np.asarray(pc.points))

pcdf = pd.DataFrame(pc, columns=['X', 'Y', 'Z', 'R', 'G', 'B'])

#   Visualization of whole point cloud

#o3d.visualization.draw_geometries([pc],
#                                  zoom=0.3412,
#                                  front=[0.4257, -0.2125, -0.8795],
#                                  lookat=[2.6172, 2.0475, 1.532],
#                                  up=[-0.0694, -0.9768, 0.2024])

#What info do we want?
# - Bounding Box
# - RGB Values
# - List array for inspection
# - Different segments, taken either from xyz or rgb
# - Distance between selected points (min, max, mean)
# - Different clustering approaches 
# - Plane segmentation


# Calculate Chamfer Distance

def chamf_dist():


    dist = pc.compute_point_cloud_distance()

#print(dist)