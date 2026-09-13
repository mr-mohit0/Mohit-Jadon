# Computer Vision Unit II - 13_Magnitude_Spectrum
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
image = np.float32(image)

# Compute 2D DFT
dft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low frequencies to the center
dft_shifted = np.fft.fftshift(dft)

# Calculate magnitude spectrum
magnitude = cv2.magnitude(
    dft_shifted[:, :, 0],
    dft_shifted[:, :, 1]
)

# Apply log scaling
magnitude = np.log(1 + magnitude)

# Normalize to 0-255 for visualization
magnitude = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

# Convert to 8-bit image
magnitude = np.uint8(magnitude)

# Save magnitude spectrum
cv2.imwrite("output.png", magnitude)

print("Magnitude spectrum saved as output.png")