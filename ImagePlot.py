import matplotlib.pyplot as plt
import os
import random

# Set the directory containing the images
image_dir = "D:\Datasets\Paper - Simplification\Metro Snapshots\UNMEC"

# Get a list of all the image file names in the directory
image_files = os.listdir(image_dir)

# Select 16 random images from the directory
selected_images = random.sample(image_files, 16)

# Create a 4x4 grid of subplots
fig, axs = plt.subplots(4, 4, figsize=(8,8))

# Iterate over the subplots and plot each image
for i, ax in enumerate(axs.flat):
    # Load the image file and plot it in the current subplot
    image_file = os.path.join(image_dir, selected_images[i])
    image = plt.imread(image_file)
    ax.imshow(image)
    ax.axis('off')

# Show the plot
plt.show()
