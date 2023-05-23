import cv2
import datetime

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Set up video capture from default webcam
cap = cv2.VideoCapture(0)

# Define variables for tracking screen time
screen_on = False
start_time = None
total_screen_time = datetime.timedelta(0)

# Loop to capture video
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    # Convert the frame to grayscale for simplicity
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Check if the screen is on by detecting if there is at least one face in the image
    screen_is_on = len(faces) > 0
    
    # If the screen is on and was previously off, start tracking screen time
    if screen_is_on and not screen_on:
        start_time = datetime.datetime.now()
        print("Starting time: ", start_time)
    
    # If the screen is off and was previously on, stop tracking screen time and update total screen time
    if not screen_is_on and screen_on:
        end_time = datetime.datetime.now()
        screen_time = end_time - start_time
        total_screen_time += screen_time
        print("Ending time: ", end_time)
    
    # Update screen_on variable
    screen_on = screen_is_on
    
    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Show the video capture in a window
    cv2.imshow('frame', frame)
    
    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and destroy the window
cap.release()
cv2.destroyAllWindows()

# Calculate the final screen time if the screen is still on at the end
if screen_on:
    end_time = datetime.datetime.now()
    print("Ending time: ", end_time)
    screen_time = end_time - start_time
    total_screen_time += screen_time

# Print the total screen time
print("Total screen time:", total_screen_time)
