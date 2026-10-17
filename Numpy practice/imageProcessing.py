import numpy as np
import random
image = np.random.randint(0, 255, (100, 100, 3))  # fake image

# Increase red channel brightness
adjustment = np.array([50, 0, 0])  # shape (3,)

brightened = image + adjustment
print(image)
print("after adjustment")
print(brightened)