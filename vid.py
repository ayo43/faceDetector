import cv2
from random import randrange


#Load the classifier--
trained_face = 'haarcascade_frontalface_default.xml'
#smile = 'haarcascade_upperbody.xml'

trained_face_data = cv2.CascadeClassifier(trained_face)
#smile_data = cv2.CascadeClassifier(smile)

webcam = cv2.VideoCapture(0)

while True: 
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img )
    
  


    #Draw rectangles on faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
  
    cv2.imshow('Lets Detect', frame)
    key = cv2.waitKey(1)

    #Stop the app when Q is pressed
    if key==81 or key==113:
        break


#Release the camera object
webcam.release()


