# Computer Vision Unit II - 12_DFT
# TODO: Implement the assignment task for this program.
# Run this file from its own folder using the local input.jpg file.


import cv2
import numpy as np

# Read grayscale image
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

# Convert image to float32
image_float = np.float32(image)

# Compute 2D DFT using OpenCV
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low frequencies to the center
shifted_dft = np.fft.fftshift(dft)

# Print required shapes
print("Original image shape:", image.shape)
print("DFT result shape:", dft.shape)
print("Shifted DFT result shape:", shifted_dft.shape)

# Create magnitude for visualization
magnitude = cv2.magnitude(shifted_dft[:, :, 0],
                          shifted_dft[:, :, 1])

magnitude = np.log(1 + magnitude)

# Normalize magnitude for saving
magnitude = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)

# Save the frequency representation
cv2.imwrite("output.png", magnitude)

print("DFT result saved as output.png")