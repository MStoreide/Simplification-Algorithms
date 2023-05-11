import open3d as o3d
import pandas as pd
import numpy as np

pc1 = o3d.io.read_point_cloud("../../test_data/fragment.ply")
pc2 = o3d.io.read_point_cloud("../../test_data/fragment.ply")

dists = pc1.compute_point_cloud_distance(pc2)
dists_ar = np.asarray(dists)
ind = np.where(dists_ar > 0.01)[0]
print(ind)