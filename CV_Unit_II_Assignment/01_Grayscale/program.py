# Computer Vision Unit II - 01_Grayscale
# This program converts a color image to grayscale.
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.

# Requirements 
# Read a color image
# Convert it to grayscale
# Save the grayscale result
# Print the original image shape
# Print the grayscale image shape
# Print the height
# Print the width

import cv2

# Read the color image
image = cv2.imread("input.jpg");

# Check if image is loaded
if image is None:
    print("Error: Could not read input.jpg");
    exit();

# Convert color image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);

# Get height and width
height, width = gray_image.shape;

# Print required information
print("Original image shape:", image.shape)
print("Grayscale image shape:", gray_image.shape)
print("Height:", height)
print("Width:", width)

# Save grayscale image
cv2.imwrite("output.png", gray_image)

print("Grayscale image saved successfully.")