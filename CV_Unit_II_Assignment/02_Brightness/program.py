# Computer Vision Unit II - 02_Brightness
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.

#requirements :)

# 1.Read a dark image 
#2. increase its brightness by a chosen constant
#3. handle the valid pixel-intensity range correctly
#4. save the enhanced image
#5. and compare at least one pixel value before and after enhancement in the console.

import cv2

# Read the dark image
image = cv2.imread("input.jpg");

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read input.jpg");
    exit();

# Choose the brightness increase
brightness = 180;

# Increase brightness while keeping pixel values in the valid range 0-255
bright_image = cv2.add(image, brightness);

# Compare one pixel before and after enhancement
x = 100;
y = 100;

before = image[y, x];
after = bright_image[y, x];

print("Brightness constant:", brightness);
print("Pixel value before enhancement:", before);
print("Pixel value after enhancement:", after);

# Save the enhanced image
cv2.imwrite("output.png", bright_image);

print("Enhanced image saved successfully as output.png");