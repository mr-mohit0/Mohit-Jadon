# Computer Vision Unit II - 09_Filter_Comparison
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.


import cv2

# Read the same noisy image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# Apply mean filter
mean_image = cv2.blur(image, (5, 5))

# Apply Gaussian filter
gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply median filter
median_image = cv2.medianBlur(image, 5)

# Save all three results
cv2.imwrite("output_mean.png", mean_image)
cv2.imwrite("output_gaussian.png", gaussian_image)
cv2.imwrite("output_median.png", median_image)

print("Mean filter result saved as output_mean.png")
print("Gaussian filter result saved as output_gaussian.png")
print("Median filter result saved as output_median.png")