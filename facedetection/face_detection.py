import cv2 as cv
img = cv.imread("grp1.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gropu Photo", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)  #Adjust the minNeighbour if  
                                                                                   #needed to get more precise result
print(f"Nmber of faces detected = {len(faces_rect)}")

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    
cv.imshow("Detected Face", img)
cv.waitKey(0)