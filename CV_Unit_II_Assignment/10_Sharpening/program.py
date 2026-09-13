# Computer Vision Unit II - 10_Sharpening
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.



import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# Custom sharpening kernel
kernel = np.array([
    [0, -1,  0],
    [-1, 5, -1],
    [0, -1,  0]
])

# Apply the sharpening kernel
sharpened_image = cv2.filter2D(image, -1, kernel)

# Save the sharpened image
cv2.imwrite("output.png", sharpened_image)

print("Sharpening completed.")
print("Output saved as output.png")