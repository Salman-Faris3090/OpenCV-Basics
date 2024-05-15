import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3), dtype = "uint8")
rectangle = cv.rectangle(blank.copy(), (40,40), (460,460), (255,0,0),thickness=-1)
circle = cv.circle(blank.copy(), (250,250), 230,(0,0,255),thickness=-1)
cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

# Bitwise And

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise And",bitwise_and)

# Bitwise OR

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise Or", bitwise_or)

# Bitwise XOR

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise Xor", bitwise_xor)

# Bitwise NOT

bitwise_not = cv.bitwise_not(rectangle, circle)
cv.imshow("bitwise Not", bitwise_not)
cv.waitKey(0)

