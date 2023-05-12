import cv2
import numpy as np
import time

import win32api
import win32con

# Define the screen boundaries (adjust these values based on your screen size and position)
# Get the screen resolution
width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
# Calculate the screen boundaries
screen_top = int(height * 0.25)
screen_bottom = int(height * 0.75)
screen_left = int(width * 0.25)
screen_right = int(width * 0.75)

print("Screen top:", screen_top)
print("Screen bottom:", screen_bottom)
print("Screen left:", screen_left)
print("Screen right:", screen_right)

# Load the pre-trained iris detector
iris_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Define a function to detect the iris in a grayscale image and check if it is within the screen boundaries
def detect_iris(gray):
    # Apply a Gaussian blur to the image to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use the iris_cascade to detect the iris in the image
    irises = iris_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If an iris is detected, check if it is within the screen boundaries
    if len(irises) > 0:
        (x, y, w, h) = irises[0]
        iris_center = (x + w//2, y + h//2)
        if iris_center[0] >= screen_left and iris_center[0] <= screen_right and iris_center[1] >= screen_top and iris_center[1] <= screen_bottom:
            return iris_center
    return None

# Start capturing video from the default camera
video_capture = cv2.VideoCapture(0)

# Define variables to keep track of the last known iris position and the time spent looking at the screen
last_iris_pos = None
screen_time = 0

# Loop over frames from the video stream
while True:
    # Capture the next frame from the video stream
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the iris in the grayscale image and check if it is within the screen boundaries
    iris_pos = detect_iris(gray)

    # If the iris is on the screen, increment the screen time and print out the iris position
    if iris_pos is not None:
        if iris_pos[0] >= screen_left and iris_pos[0] <= screen_right and iris_pos[1] >= screen_top and iris_pos[1] <= screen_bottom:
            screen_time += 1
        print("Iris position:", iris_pos)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Print the screen time in seconds
print("Screen time:", screen_time, "seconds")
