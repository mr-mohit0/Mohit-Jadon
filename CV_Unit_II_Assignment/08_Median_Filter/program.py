# Computer Vision Unit II - 08_Median_Filter
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.




import cv2

# Read the noisy image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# Apply median filtering
median_image = cv2.medianBlur(image, 5)

# Save the filtered image
cv2.imwrite("output.png", median_image)

print("Median filtering completed.")
print("Output saved as output.png")