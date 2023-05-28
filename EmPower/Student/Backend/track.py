import cv2
import datetime
from PyQt5.QtCore import QThread
from collections import defaultdict
import json


class FaceTracker(QThread):

    def __init__(self):
        super().__init__()
        self.old_lesson_id = None
        self.new_lesson_id = None
        self.old_module_id = None
        self.new_module_id = None
        self.total_screen_time = datetime.timedelta(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.is_running = True
        
        # Define variables for tracking screen time
        self.screen_on = False
        self.screen_is_on = False
        self.start_time = None

        #time dict
        self.lesson_time = defaultdict(dict)

    def run(self):

        # Set up video capture from default webcam
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Specify the CAP_DSHOW backend

        # Check if the video capture is successfully opened
        if not self.cap.isOpened():
            print("Failed to open video capture.")
            self.finished.emit()
            return

        # Loop to capture video
        while self.is_running:
            # Read a frame from the video capture
            ret, frame = self.cap.read()
            

            if not ret:
                print("Failed to read a frame from video capture.")
                break

            # Convert the frame to grayscale for simplicity
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale image
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            
            # draw green rectangle around face and show it
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.imshow('frame', frame)

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

            # check for lesson change
            if self.new_lesson_id != self.old_lesson_id:
                print("lesson_id changed")
                self.save_time()
                self.old_lesson_id = self.new_lesson_id

            # check for module change
            if self.new_module_id != self.old_module_id:
                print("module_id changed")
                self.save_time()
                self.old_module_id = self.new_module_id

            # Check for exit command
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release video capture and destroy the window
        self.cap.release()
        cv2.destroyAllWindows()
        self.finished.emit()


    def save_time(self):
        # Calculate the final screen time if the screen is still on at the end
        if self.screen_on:
            end_time = datetime.datetime.now()
            print("Ending time: ", end_time)
            screen_time = end_time - self.start_time
            self.total_screen_time += screen_time

        self.lesson_time[self.old_lesson_id][self.old_module_id] = self.total_screen_time
        self.total_screen_time = datetime.timedelta(0)

    def stop(self):
        self.is_running = False

        # print the final dict
        print(self.lesson_time)
        self.save_data_to_json()

    def set_lesson_id(self, lesson_id, module_id):
        self.new_lesson_id = lesson_id
        self.new_module_id = module_id

    def face_tracker_initialize(self, lsn_id):
        self.old_lesson_id = lsn_id
        self.new_lesson_id = lsn_id
        self.old_module_id = 0
        self.new_module_id = 0


    def save_data_to_json(self):
        # Convert timedelta to seconds
        def convert_timedelta_to_seconds(td):
            return td.total_seconds()

        # Create a new dictionary with modified values
        new_dictionary = {}
        for lesson_id, lesson_data in self.lesson_time.items():
            new_dictionary[f"lesson {lesson_id}"] = {
                f"module {module_id+1}": convert_timedelta_to_seconds(td)
                for module_id, td in lesson_data.items()
            }

        # Write the dictionary to a JSON file
        with open('surveillance_log.json', 'w') as file:
            json.dump(new_dictionary, file, indent=4)