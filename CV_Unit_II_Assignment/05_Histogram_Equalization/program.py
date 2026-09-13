# Computer Vision Unit II - 05_Histogram_Equalization
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.


#Requirements :)
# perform histogram equalization on a grayscale image, save the equalized image, and save one comparison plot containing both the before and after histograms.


import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# Save equalized image
cv2.imwrite("output.png", equalized_image)

# Calculate histograms before and after equalization
hist_before = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_after = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Plot both histograms in a single comparison plot
plt.plot(hist_before, label="Before Equalization")
plt.plot(hist_after, label="After Equalization")

plt.title("Histogram Before and After Equalization")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.legend()

# Save comparison plot
plt.savefig("histogram_comparison.png")
plt.close()

print("Histogram equalization completed.")
print("Equalized image saved as output.png")
print("Comparison histogram saved as histogram_comparison.png")