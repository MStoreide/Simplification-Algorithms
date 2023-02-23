import matplotlib.pyplot as plt
import numpy as np

# Create a 4x4 array of random images
images = (np.random.rand(4, 4, 32, 32, 3))

# Create a figure with a 4x4 grid of subplots
fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(8, 8))

# Iterate over the subplots and display each image
for i in range(4):
    for j in range(4):
        ax[i, j].imshow(images[i, j])
        ax[i, j].axis('off')

# Show the figure
plt.show()
