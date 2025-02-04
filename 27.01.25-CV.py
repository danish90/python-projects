import cv2
import numpy as np

# load image from file
image = cv2.imread('old_fashioned.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(image, (500, 300))

cv2.imshow('Lalala', resized_image)

cv2.rectangle(image, (0, 0), (700, 200), (100, 100, 100), 2)

cv2.circle(image, (500, 500), 50, (255, 0, 0), -1)

cv2.imshow('Drawing stuff', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""opening up the video feed"""

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""Trying different image effects"""

image = cv2.imread('old_fashioned.jpg')

blurred = cv2.blur(image, (4, 4))
gaussian_blurred = cv2.GaussianBlur(image, (5, 5), 0)
median_blurred = cv2.medianBlur(image, 5) #removes noise while preserving edges

cv2.imshow('Original', image)
cv2.imshow('Blurred', blurred)
cv2.imshow('Gaussian blurred', gaussian_blurred)
cv2.imshow('Median blur', median_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""Sharpening an image - subtract the blurred image from the original"""

image = cv2.imread('old_fashioned.jpg')

gauss_blur = cv2.GaussianBlur(image, (0, 0), 3)
sharpened = cv2.addWeighted(image, 1.5, gauss_blur, -0.5, 20)

cv2.imshow('Original', image)
cv2.imshow('Gaussian blur', gauss_blur)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""Edge detection using sobel filter"""

image = cv2.imread('assets/old_fashioned.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 5)

sobel_x_abs = np.absolute(sobel_x)
sobel_y_abs = np.absolute(sobel_y)

sobel_combined = cv2.magnitude(sobel_x_abs, sobel_y_abs)

sobel_combined = np.uint8(sobel_combined)

cv2.imshow('Original', image)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel X abs', sobel_x_abs)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Y abs', sobel_y_abs)
cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""Harris Corner Detection"""

import cv2
import numpy as np

image = cv2.imread('assets/022.jpg', 1)
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_gray = cv2.GaussianBlur(image_gray, (5, 5), 0)

gray_float = np.float32(image_gray)

dst = cv2.cornerHarris(gray_float, blockSize=5, ksize=5, k=0.05)

dst = cv2.dilate(dst, None)

# image_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

mask = dst > 0.01 * dst.max()

image[mask] = [0, 0, 255]

cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""Shi-Tomasi Corner Detection"""

import cv2
import numpy as np

image = cv2.imread('assets/022.JPG')
image = cv2.resize(image, (0,0), fx=0.25, fy=0.25)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(image_gray, maxCorners=100, qualityLevel=0.005, minDistance=0.5)

corners = corners.astype(np.int64)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

cv2.imshow('Shi-Tomasi', image)
cv2.waitKey(0)
cv2.destroyAllWindows()