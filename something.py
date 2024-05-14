import cv2 as cv
import numpy as np

# Reading image from path
img = cv.imread("Frozen Rose.jpg")
cv.imshow("Frozen Rose", img)

# creating a blank image and reading 
blank=np.zeros((500, 500), dtype = 'uint8')
cv.imshow("Blank", blank)

# Reading video
capture = cv.VideoCapture("me.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
capture.release()
cv.destroyAllWindows    

cv.waitKey(0)
