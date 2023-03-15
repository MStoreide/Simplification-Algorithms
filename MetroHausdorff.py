import pymeshlab as pym
import numpy as np
import matplotlib as plt

#Using pymeshlab, we apply the Huasdorff distance filter to all meshes compared to the original (SM_Randomized).
#Sample faces at the total triangle count of the original mesh.

output_path = ('/home/markus/Pictures/')

ms = pym.MeshSet() # Creates a container where we can load our meshes into.
ms.load_new_mesh('SMD16.obj')
ms.load_new_mesh('SMB.obj')

baseline = ms.current_mesh()

print("Current mesh is: ", (ms.current_mesh_id()))

samples = baseline.face_number()
print(f"Current mesh has", samples, "faces")

print(ms.get_hausdorff_distance(sampledmesh = 1, targetmesh = 0, savesample=True, sampleface=True, samplenum = (samples), maxdist = pym.Percentage(50)))



ms.save_filter_script(output_path + 'test_saved_script.csv')

vq = ms.mesh(2).face_quality_array()


# Stolen code to plot


# This is  the colormap I'd like to use.
cm = plt.cm.get_cmap('jet')

# Plot histogram.
n, bins, patches = plt.histogram(vq, 256, density = True)
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# scale values to interval [0,1]
col = bin_centers - min(bin_centers)
col /= max(col)

for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', cm(c))

plt.xticks(np.linspace(float(format(min(vq), '.1f')),
               float(format(max(vq), '.1f')),
               num = 21,
               endpoint = True))
plt.tick_params(axis ='x', rotation = -90)

path = 'Some_path_in_your_drive'
output_file = path + "/HD_histogram.svg" # I save them in .svg format so later I can edit them on inkscape
plt.savefig(output_file,
        bbox_inches ="tight",
        transparent = True,
        facecolor ="w",
        edgecolor ='w',
        orientation ='landscape')    
    

