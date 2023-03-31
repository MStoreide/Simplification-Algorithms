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
pc = o3d.io.read_point_cloud(r"G:\Markus_Folder\Business_Backup\Datasets\Paper_Simplification\Metro Data\U PointClouds\UMD\UMD16.ply")
assert (pc.has_normals())

## Data Extraction ##

pc_array = pd.DataFrame(pc.points, columns = ['X','Y','Z'])
pc_colors = pd.DataFrame(pc.colors, columns = ['R','G','B'])

#   Visualization of whole point cloud

#o3d.visualization.draw_geometries([pc],
#                                  zoom=0.3412,
#                                  front=[0.4257, -0.2125, -0.8795],
#                                  lookat=[2.6172, 2.0475, 1.532],
#                                  up=[-0.0694, -0.9768, 0.2024])



## Calculate Chamfer Distance ##

def chamf_dist(pointcloud):
    dist = pointcloud.compute_point_cloud_distance()

#print(dist)


## Plane Segmentations ##

# Plane Segmentation using RANSAC
# Allows us to detect planes within given parameters. Can be used to detect very small curvatures

plane_model, inliers = pc.segment_plane(distance_threshold=0.35,  # Defines the maximum distance a point can have to an estimated plane to be considered an inlier
                                         ransac_n=100,            # Defines the number of points that are randomly sampled to estimate a plane
                                         num_iterations=1000)     # Defines how often a random plane is sampled and verified.
[a, b, c, d] = plane_model
print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")

inlier_cloud = pc.select_by_index(inliers)
inlier_cloud.paint_uniform_color([0, 0, 0]) # Colors the plane black, since point cloud already has RGB colors
outlier_cloud = pc.select_by_index(inliers, invert=True)
#o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
#                                  zoom=0.8,
#                                  front=[-0.4999, -0.1659, -0.8499],
#                                  lookat=[2.1813, 2.0619, 2.0999],
#                                  up=[0.1204, -0.9852, 0.1215])

# Approach that segments planes

#assert (pc.has_normals())

# using all defaults
#oboxes = pc.detect_planar_patches(
#    normal_variance_threshold_deg=30,
#    coplanarity_deg=75,
#    outlier_ratio=0.75,
#    min_plane_edge_length=0,
#    min_num_points=0,
#    search_param=o3d.geometry.KDTreeSearchParamKNN(knn=100))

#print("Detected {} patches".format(len(oboxes)))

#geometries = []
#for obox in oboxes:
#    mesh = o3d.geometry.TriangleMesh.create_from_oriented_bounding_box(obox, scale=[1, 1, 0.0001])
#    mesh.paint_uniform_color(obox.color)
#    geometries.append(mesh)
#    geometries.append(obox)
#geometries.append(pc)

#o3d.visualization.draw_geometries(geometries,
#                                  zoom=0.62,
#                                  front=[0.4361, -0.2632, -0.8605],
#                                  lookat=[2.4947, 1.7728, 1.5541],
#                                  up=[-0.1726, -0.9630, 0.2071])


## Calculate Chamfer Distance ##

#def chamf_dist(pointcloud):
#    dist = pointcloud.compute_point_cloud_distance()

#print(dist)
