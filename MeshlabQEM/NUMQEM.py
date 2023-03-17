import pymeshlab as pym

output_path = (r"'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Quadric Error Metrics\NUMQEM")

ms = pym.MeshSet()

ms.load_new_mesh('SMB.obj')
baseline = ms.current_mesh()
baselinetris = baseline.face_number()

ms.show_polyscope()

print(ms.current_mesh)

#Duplicate baseline

#ms.meshing_decimation_quadric_edge_collapse(targetfacenum = (baselinetris*PERCENTAGE), )