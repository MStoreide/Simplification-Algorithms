import tempfile
import open3d as o3d
import pandas as pd
import numpy as np

#What info do we want?
# - Bounding Box
# - RGB Values
# - List array for inspection
# - Different segments, taken either from xyz or rgb
# - Distance between selected points (min, max, mean)
# - Different clustering approaches 
# - Plane segmentation

print("Reading Point Cloud")

#This could read automatically from where we save the Hausdorff PLYs in Statistics.py
pc = o3d.io.read_point_cloud(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Metro Data (Manual)\U PointClouds\UMD\UMD16.ply")
assert (pc.has_normals())






## Data Extraction ##

# Dataframes for XYZ and RGB
pc_array = pd.DataFrame(pc.points, columns = ['X','Y','Z'])
pc_colors = pd.DataFrame(pc.colors, columns = ['R','G','B'])

# Calculate convex hull #This does not use a PLY, so should probably be moved
SMBmesh = o3d.io.read_triangle_mesh(r'G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Baselines\SMB.obj')
SMBmesh.compute_vertex_normals()

pcl = SMBmesh.sample_points_poisson_disk(number_of_points=2000)
hull, _ = pcl.compute_convex_hull()
hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
hull_ls.paint_uniform_color((1, 0, 0))
o3d.visualization.draw_geometries([pcl, hull_ls],
                                   zoom=0.3412,
                                   front=[0.4257, -0.2125, -0.8795],
                                   lookat=[2.6172, 2.0475, 1.532],
                                   up=[-0.0694, -0.9768, 0.2024])

#   Visualization of whole point cloud

#o3d.visualization.draw_geometries([pc],
#                                  zoom=0.3412,
#                                  front=[0.4257, -0.2125, -0.8795],
#                                  lookat=[2.6172, 2.0475, 1.532],
#                                  up=[-0.0694, -0.9768, 0.2024])






## Segmentations ##
#################################################################################################################

# RGB Segmetation
# Based on Hausdorff RGB data, we segment the areas with most error


# Plane Segmentation

# Plane Segmentation using RANSAC
# Allows us to detect planes within given parameters. Can be used to detect surfaces with very small curvatures 

pc_planes = pc 
plane_model, inliers = pc_planes.segment_plane(distance_threshold=0.35,  # Defines the maximum distance a point can have to an estimated plane to be considered an inlier
                                         ransac_n=100,                   # Defines the number of points that are randomly sampled to estimate a plane
                                         num_iterations=1000)            # Defines how often a random plane is sampled and verified.
[a, b, c, d] = plane_model
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

inlier_cloud = pc_planes.select_by_index(inliers)
inlier_cloud.paint_uniform_color([0, 0, 0]) # Colors the plane black, since point cloud already has RGB colors
outlier_cloud = pc_planes.select_by_index(inliers, invert=True)
#o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
#                                  zoom=0.8,
#                                  front=[-0.4999, -0.1659, -0.8499],
#                                  lookat=[2.1813, 2.0619, 2.0999],
#                                  up=[0.1204, -0.9852, 0.1215])


## Calculate Chamfer Distance ##

#def chamf_dist(pointcloud):
#    dist = pointcloud.compute_point_cloud_distance()

#print(dist)

#o3d.visualization.draw_geometries([pc],
#                                  zoom=0.3412,
#                                  front=[0.4257, -0.2125, -0.8795],
#                                  lookat=[2.6172, 2.0475, 1.532],
#                                  up=[-0.0694, -0.9768, 0.2024])

