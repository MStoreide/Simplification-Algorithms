import matplotlib.pyplot as plt
import os

# Set the directory containing the images. Remember to change this if on a different computer. Could also connect to server. 
#Can change this to taking it from the project folder instead. 
image_dir = r"H:\Datasets\Paper - Simplification\Metro Snapshots\RNMEC"

# List the image file names in the order you want to display them. 
image_files = [
    "RNMEC01.png",
    "RNMEC02.png",
    "RNMEC03.png",
    "RNMEC04.png",
    "RNMEC05.png",
    "RNMEC06.png",
    "RNMEC07.png",
    "RNMEC08.png",
    "RNMEC09.png",
    "RNMEC10.png",
    "RNMEC11.png",
    "RNMEC12.png",
    "RNMEC13.png",
    "RNMEC14.png",
    "RNMEC15.png",
    "RNMEC16.png",
]

# Create a 4x4 grid of subplots
fig, axs = plt.subplots(4, 4, figsize=(8,8))

# Iterate over the subplots and plot each image
for i, ax in enumerate(axs.flat):
    # Load the image file and plot it in the current subplot
    image_file = os.path.join(image_dir, image_files[i])
    image = plt.imread(image_file)
    ax.imshow(image)
    ax.axis('off')

# Show the plot
plt.show()
