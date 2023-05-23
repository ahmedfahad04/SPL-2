import cv2
import datetime
from PyQt5.QtCore import QThread


class FaceTracker(QThread):

    def __init__(self, content_name=None):
        super().__init__()
        self.content_name = content_name
        self.total_screen_time = datetime.timedelta(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.is_running = True
        # Define variables for tracking screen time
        self.screen_on = False
        self.screen_is_on = False
        self.start_time = None

    def run(self):
        while self.is_running:
            # Set up video capture from default webcam
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Specify the CAP_DSHOW backend

            # Check if the video capture is successfully opened
            if not cap.isOpened():
                print("Failed to open video capture.")
                self.finished.emit()
                return

            # Loop to capture video
            while True:
                # Read a frame from the video capture
                ret, frame = cap.read()

                if not ret:
                    print("Failed to read a frame from video capture.")
                    break

                # Convert the frame to grayscale for simplicity
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces in the grayscale image
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                # Check if the screen is on by detecting if there is at least one face in the image
                self.screen_is_on = len(faces) > 0

                # If the screen is on and was previously off, start tracking screen time
                if self.screen_is_on and not self.screen_on:
                    self.start_time = datetime.datetime.now()
                    print("Starting time: ", self.start_time)

                # If the screen is off and was previously on, stop tracking screen time and update total screen time
                if not self.screen_is_on and self.screen_on:
                    end_time = datetime.datetime.now()
                    screen_time = end_time - self.start_time
                    self.total_screen_time += screen_time
                    print("Ending time: ", end_time)

                # Update screen_on variable
                self.screen_on = self.screen_is_on

                # Draw a rectangle around each detected face
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Show the video capture in a window
                # cv2.imshow('frame', frame)

                # Check for exit command
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


            # Release video capture and destroy the window
            cap.release()
            cv2.destroyAllWindows()
            self.finished.emit()

    def get_total_time(self):
        # Calculate the final screen time if the screen is still on at the end
        if self.screen_on:
            end_time = datetime.datetime.now()
            print("Ending time: ", end_time)
            screen_time = end_time - self.start_time
            self.total_screen_time += screen_time
        print(f"total time for current lesson {self.content_name}: ", self.total_screen_time)

    def stop(self):
        self.is_running = False



