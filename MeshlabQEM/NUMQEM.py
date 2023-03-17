import pymeshlab as pym

output_path = (r"'G:\Markus_Folder\Business Backup\Datasets\Paper_Simplification\Quadric Error Metrics\NUMQEM")

ms = pym.MeshSet()

ms.load_new_mesh('SMB.obj')
baseline = ms.current_mesh()
baselinetris = baseline.face_number()

#Duplicate baseline
ms.add_mesh(baseline, mesh_name='SMBQEM1')
print("Current mesh is ", ms.current_mesh_id()) #Needs to be the duplicated mesh at this point

ms.meshing_decimation_quadric_edge_collapse(targetfacenum = (int(baselinetris*0.975)))

QEM1faces = ms[1].face_number()
print("QEM1 has", QEM1faces, "faces")

ms.save_current_mesh(file_name='SMBQEM1.obj') #Select a filepath for this

# Simp Stage 2

ms.add_mesh(baseline, mesh_name='SMBQEM2')
print("Current mesh is ", ms.current_mesh_id()) #Needs to be the duplicated mesh at this point

ms.meshing_decimation_quadric_edge_collapse(targetfacenum = (int(baselinetris*0.5))) # Fix correct number

QEM2faces = ms[2].face_number()
print("QEM2 has", QEM2faces, "faces")

ms.save_current_mesh(file_name='SMBQEM2.obj') #Select a filepath for this


#Add remaining 14 stages

ms.__str__()