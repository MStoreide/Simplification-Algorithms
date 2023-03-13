import open3d as o3d
import pandas as pd

print("Reading Point Cloud")

pc = o3d.io.read_point_cloud("Filepath")

print(pc)

