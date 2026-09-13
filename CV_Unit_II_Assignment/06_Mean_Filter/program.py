# Computer Vision Unit II - 06_Mean_Filter
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.




import cv2

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# Run 1: smaller kernel
small_kernel = cv2.blur(image, (3, 3))
cv2.imwrite("output_3x3.png", small_kernel)

# Run 2: larger kernel
large_kernel = cv2.blur(image, (5, 5))

# Required final output uses the larger kernel
cv2.imwrite("output.png", large_kernel)

print("3x3 mean filter applied and saved as output_3x3.png")
print("5x5 mean filter applied and saved as output.png")