# Computer Vision Unit II - 03_Contrast_Stretching
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.


#Requirements:
# Read a low-contrast grayscale image
# Determine the minimum intensity value
# Determine the maximum intensity value
# Perform contrast stretching
# Expand the useful intensity range
# Save the enhanced image
# Do NOT simply use histogram equalization



# 📐 Mathematical Formula

# The standard contrast-stretching formula is:

# $$ I_{new} = \frac{I-I_{min}} {I_{max}-I_{min}} \times255 $$

# Where:

# \(I\) = original pixel intensity
# \(I_{min}\) = minimum intensity in the image
# \(I_{max}\) = maximum intensity in the image
# \(I_{new}\) = new stretched intensity
# Example

# Suppose:

# Minimum = 80
# Maximum = 170

# For a pixel having intensity:

# I = 125

# Then:

# $$ I_{new} = \frac{125-80}{170-80}\times255 $$ $$ =\frac{45}{90}\times255 $$ $$ =127.5 $$

# So approximately:

# 125 → 128



import cv2
import numpy as np

# Read the low-contrast grayscale image
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE);

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read input.jpg");
    exit();

# Find minimum and maximum intensity values
min_intensity = np.min(image);
max_intensity = np.max(image);

print("Minimum intensity:", min_intensity);
print("Maximum intensity:", max_intensity);

# Perform contrast stretching
if max_intensity == min_intensity:
    print("Error: Image has no intensity variation.");
    exit();

stretched_image = (
    (image.astype(np.float32) - min_intensity)
    / (max_intensity - min_intensity)
    * 255
);

# Convert the result to 8-bit image
stretched_image = np.uint8(stretched_image);

# Save the enhanced image
cv2.imwrite("output.png", stretched_image);

print("Contrast-stretched image saved successfully as output.png");