import cv2
import numpy as np

# Load the image
image = cv2.imread('path_to_image.jpg')
if image is None:
    raise ValueError("Image not found. Please check the path to the image.")

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range for segmentation (example: blue color)
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

# Create a binary mask where the blue colors are white and the rest are black
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Bitwise-AND mask and original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original image
cv2.imshow('Original Image', image)

# Display the mask
cv2.imshow('Mask', mask)

# Display the segmented image
cv2.imshow('Segmented Image', segmented_image)

# Wait until a key is pressed and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
