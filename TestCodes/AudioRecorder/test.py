import sys
import pyaudio
import wave
import signal
from PyQt5.QtCore import Qt, QThread, QObject
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class AudioRecorder(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Audio Recorder')
        self.setGeometry(100, 100, 300, 200)

        self.recording = False
        self.frames = []

        self.label = QLabel('Press the button to start recording')
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_recording)

        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_recording)
        self.stop_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 44100
        self.chunk = 1024

        self.audio = pyaudio.PyAudio()

    def start_recording(self):
        self.recording = True
        self.frames = []

        self.stream = self.audio.open(format=self.audio_format,
                                      channels=self.channels,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)

        self.label.setText('Recording...')
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        self.worker = RecordWorker(self.stream, self.frames, self.chunk)
        self.worker.start()
        signal.signal(signal.SIGINT, self.on_worker_finished)

    def stop_recording(self):
        self.recording = False
        self.worker.stop()
        self.stream.stop_stream()
        self.stream.close()

        wf = wave.open('output.wav', 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        self.label.setText('Press the button to start recording')
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def on_worker_finished(self, *args):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()

        wf = wave.open('output.wav', 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        self.label.setText('Press the button to start recording')
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

class RecordWorker(QThread):
    def __init__(self, stream, frames, chunk):
        super().__init__()
        self.stream = stream
        self.frames = frames
        self.chunk = chunk
        self.is_running = True

    def run(self):
        while self.is_running:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def stop(self):
        self.is_running = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder = AudioRecorder()
    recorder.show()
    sys.exit(app.exec_())
