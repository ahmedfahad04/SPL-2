import sys
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class Timer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 250, 100)

        # Create a vertical layout for the window
        layout = QVBoxLayout()

        # Create a label to display the timer
        self.timer_label = QLabel()
        self.timer_label.setText("00:00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)

        # Add the label to the layout
        layout.addWidget(self.timer_label)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Create the start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        button_layout.addWidget(self.start_button)

        # Create the end button
        self.end_button = QPushButton("End")
        self.end_button.setEnabled(False)
        self.end_button.clicked.connect(self.end_timer)
        button_layout.addWidget(self.end_button)

        # Add the button layout to the vertical layout
        layout.addLayout(button_layout)

        # Set the layout for the window
        self.setLayout(layout)

        # Set the initial time to 0
        self.time = QTime(0, 0, 0)

        # Create a timer that updates every second
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

    def start_timer(self):
        # Start the timer
        self.timer.start()

        # Disable the start button and enable the end button
        self.start_button.setEnabled(False)
        self.end_button.setEnabled(True)

    def end_timer(self):
        # Stop the timer
        self.timer.stop()

        # Enable the start button and disable the end button
        self.start_button.setEnabled(True)
        self.end_button.setEnabled(False)

    def update_timer(self):
        # Increment the time by one second
        self.time = self.time.addSecs(1)

        # Update the label with the new time
        self.timer_label.setText(self.time.toString("hh:mm:ss"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec_())
