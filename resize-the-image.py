import cv2  # OpenCV for image processing
import imutils  # Utility library for image resizing

# Read the image
img = cv2.imread('burger.jpg')

# Resize the image to a width of 400 pixels while maintaining aspect ratio
resizedImg = imutils.resize(img, width=300)

# Display the original and resized images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resizedImg)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
