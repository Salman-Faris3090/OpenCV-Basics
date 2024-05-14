import cv2 as cv
img = cv.imread("Lungs.jpg")
cv.imshow("Lungs",img)

# Converting Image to Grayscale Image
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey Image", grey)

# Blurring an Image
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT) # 3x3 kernal
cv.imshow("3x3 Blurred Image", blur)

blur = cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT) # 5x5 kernal
cv.imshow("5x5 Blurred Image", blur)

blur = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT) # 7x7 kernal
cv.imshow("7x7 Blurred Image", blur)


# Edge cascade
canny = cv.Canny(img, 125, 175,)
cv.imshow("Canny Edges", canny)

# Dilating Image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dialted",dilated)

# Eroding
Eroded= cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded",Eroded)

# Resizing the image
Resized = cv.resize(img, (500,500),interpolation = cv.INTER_AREA)
cv.imshow("Resized",Resized)

# Cropping the image
Cropped = img[50:200,200:500]
cv.imshow("cropped",Cropped)
cv.waitKey(0)
