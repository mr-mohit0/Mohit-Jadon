# Computer Vision Unit II - 07_Gaussian_Filter
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.



#requirements :)
# Use a noisy image as input.
# Apply Gaussian smoothing.
# Select an appropriate odd kernel size.
# Add a short code comment explaining why that kernel size was selected.
# Save the smoothed result.

import cv2

# Read the noisy image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()



# 5x5 is an odd-sized kernel and provides good smoothing of noise
gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)

# Save the smoothed image
cv2.imwrite("output.png", gaussian_image)

print("Gaussian smoothing completed.")
print("Output saved as output.png")