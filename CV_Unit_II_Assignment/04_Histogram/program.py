# Computer Vision Unit II - 04_Histogram
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.

#Requirements :)

# Read a grayscale image
# Calculate its intensity histogram
# Plot the histogram
# Save the histogram as output.png
# Print the intensity value having the highest frequency


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Check image
if image is None:
    print("Error: input.jpg not found")
    exit()

# Calculate histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Find intensity with highest frequency
intensity = np.argmax(histogram)

print("Intensity with highest frequency:", intensity)

# Plot histogram
plt.plot(histogram)
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.title("Image Histogram")

# Save histogram
plt.savefig("output.png")
plt.close()

print("Histogram saved as output.png")

print("Histogram saved successfully as output.png")
