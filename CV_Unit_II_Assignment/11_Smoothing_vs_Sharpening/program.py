# Computer Vision Unit II - 11_Smoothing_vs_Sharpening
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.



import cv2
import numpy as np

# Read the same input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# Apply smoothing
smooth_image = cv2.GaussianBlur(image, (5, 5), 0)

# Create a sharpening kernel
kernel = np.array([
    [0, -1,  0],
    [-1, 5, -1],
    [0, -1,  0]
])

# Apply sharpening
sharp_image = cv2.filter2D(image, -1, kernel)

# Save both results
cv2.imwrite("output_smooth.png", smooth_image)
cv2.imwrite("output_sharp.png", sharp_image)

print("Smoothed image saved as output_smooth.png")
print("Sharpened image saved as output_sharp.png")