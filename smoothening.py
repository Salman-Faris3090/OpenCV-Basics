import cv2 as cv
img = cv.imread("Lungs.jpg")
cv.imshow("Original image", img)

# Applying Average Filter of kernal 7x7
average = cv.blur(img, (7,7))
cv.imshow("Average Filtered Image", average)

# Applying Gaussian Filter of kernal 7x7
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussain Filterd Image", gauss)

# Applying Medain Filter of kernal 7x7
medain  = cv.medianBlur(img, 7)
cv.imshow("Median Filtered Image", medain)

# Applying Bilateral Filter 
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow("bilateral Filtered Image", bilateral)

cv.waitKey(0)