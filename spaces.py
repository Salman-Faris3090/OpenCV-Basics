import cv2 as cv
img = cv.imread("Frozen Rose.jpg")
cv.imshow("Frozen Rose", img)

# BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image",gray)

# BGR to HSV
hsr = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image",hsr)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("L*a*b Image",lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB Image",rgb)
cv.waitKey(0)