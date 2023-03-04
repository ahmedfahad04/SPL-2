import signal

import pyaudio
import wave

from PyQt5.QtCore import QThread


class AudioRecorder:
    def __init__(self):
        # Define the default audio settings
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.frames = []
        self.quitCommandFlag = False
        self.fileName = ""
        self.audio = pyaudio.PyAudio()

    def set_format(self, format):
        self.FORMAT = format

    def set_channels(self, channels):
        self.CHANNELS = channels

    def set_rate(self, rate):
        self.RATE = rate

    def set_chunk(self, chunk):
        self.CHUNK = chunk

    def set_quitCommandFlag(self):
        self.quitCommandFlag = True

    def set_fileName(self, fileName):
        self.fileName = fileName

    def start_recording(self):
        self.recording = True
        self.frames = []

        self.stream = self.audio.open(format=self.audio_format,
                                      channels=self.channels,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)

        self.worker = RecordWorker(self.stream, self.frames, self.chunk)
        self.worker.start()
        signal.signal(signal.SIGINT, self.on_worker_finished)

    def stop_recording(self):
        self.recording = False
        self.worker.stop()
        self.stream.stop_stream()
        self.stream.close()
        self.save_file()

    def on_worker_finished(self, *args):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.save_file()

    def save_file(self):
        wf = wave.open(self.fileName + '.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

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




# Example usage:
# recorder = AudioRecorder()
#
# recorder.start_recording()  # for now this will go to infinite loop
#                             # because i have reorganized the code to user's perspective
#                             # when the user click stop button the recorder.set_quitCommandFlag will
#                             # be set true and this will stop
# recorder.set_quitCommandFlag()
# fileName = input()
# recorder.stop_recording(fileName + ".wav")
