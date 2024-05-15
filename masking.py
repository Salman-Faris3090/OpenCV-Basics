### The masking can be performed by other shapes also
### If we are using a Rectangle as a mask then the parameters will change
### and the resultant masked image will also be different
import cv2 as cv
import numpy as np
img =cv.imread("frzn.png")
cv.imshow("Frozen", img)


blank = np.zeros(img.shape[:2], dtype = "uint8")
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2),200, 255, thickness=-1)
cv.imshow("mask", mask)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)


cv.waitKey(0)