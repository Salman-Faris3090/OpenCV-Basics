import cv2 as cv
import numpy as np

img  = cv.imread("Frozen Rose.jpg")
cv.imshow("Original Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale Image", gray)


# Applying Laplacian Filter
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian Filtered Image", lap)


# Applying Sobel Filter
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("combined Sobel", combined_sobel)
cv.waitKey(0)
