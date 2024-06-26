import cv2 as cv
import numpy as np
import os

# Load the haar cascade
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# List of people
people = ['Chris Hemsworth', 'Jackie Chan', 'Johnny Depp', 'Robert Downey Junior', 'Shah Rukh Khan']

# Directory paths for training data
DIR = r'D:\Salman\OpenCV\Pics\train'

# Initialize lists to hold training data
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# Save features and labels
np.save("features.npy", features)
np.save("labels.npy", labels)

# Create and train the recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

# Save the trained model
face_recognizer.save("face_trained.yml")
print('Model training and saving done.')
