import cv2
import numpy as np
from util import get_limits  # Ensure this function is correct

yellow = [0, 255, 255]  # Yellow in BGR color space
cap = cv2.VideoCapture(0)  # Use 0 for the primary camera

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)

    print("Lower HSV:", lowerLimit)
    print("Upper HSV:", upperLimit)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Debugging: Show the mask
    cv2.imshow('Mask', mask)

    # Bounding box detection
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Contours found:", len(contours))

    if contours:
        x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()