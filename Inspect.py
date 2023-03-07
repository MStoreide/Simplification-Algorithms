import inspect
import open3d as o3d
import pymeshlab as pym

source_D = inspect.getsource(o3d.simplify_quadric_decimation)
print("Source Code for Decimation")
print(source_D)

source_VC = inspect.getsource(o3d.simplify_vertex_clustering)
print("Source Code for Vertex Clustering")
print(source_VC)

source_QEM = inspect.getsource(pym.QuadricSimplification)
print("Sourcecode for QEM")
print(source_QEM)