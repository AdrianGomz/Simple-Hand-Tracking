import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)



hands_ms=mp.solutions.hands
# Hands() objects only uses RGB images
hand_object=mp.solutions.hands.Hands()
# solutions.drawing_utils is used to draw the lines and points of the hands_mp detected on the image
mpDraw=mp.solutions.drawing_utils



while True:
    suc, frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    processed_image=hand_object.process(imgRGB)
    print(processed_image.multi_hand_landmarks)

    # If we detect a hand we will draw the lines and points for each and detected
    if processed_image.multi_hand_landmarks:
        for hand_in_image in processed_image.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand_in_image, hands_ms.HAND_CONNECTIONS)


    cv2.imshow('Webcam',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break