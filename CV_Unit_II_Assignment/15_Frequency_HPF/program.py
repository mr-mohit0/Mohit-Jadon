# Computer Vision Unit II - 15_Frequency_HPF
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

# Compute DFT
dft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low frequencies to the center
dft_shifted = np.fft.fftshift(dft)

# Create a high-pass mask
rows, cols = image.shape
center_row = rows // 2
center_col = cols // 2

mask = np.ones((rows, cols, 2), np.float32)

# Remove the central low-frequency region
radius = 50

y, x = np.ogrid[:rows, :cols]
distance = (x - center_col) ** 2 + (y - center_row) ** 2
mask[distance <= radius ** 2] = 0

# Apply the mask
filtered_dft = dft_shifted * mask

# Shift frequencies back
filtered_dft = np.fft.ifftshift(filtered_dft)

# Perform inverse DFT
result = cv2.idft(
    filtered_dft,
    flags=cv2.DFT_REAL_OUTPUT | cv2.DFT_SCALE
)

# Normalize the result for visualization
result = cv2.normalize(
    result,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

result = np.uint8(result)

# Save reconstructed HPF image
cv2.imwrite("output.png", result)

print("Frequency-domain HPF completed.")
print("Output saved as output.png")