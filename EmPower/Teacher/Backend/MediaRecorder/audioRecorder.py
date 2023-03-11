import signal
import wave

import pyaudio
from PyQt5.QtCore import QThread


class AudioRecorder:
    def __init__(self):
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 44100
        self.chunk = 1024
        self.audio_location = "Backend/MediaRecorder/audio.wav"
        self.audio = pyaudio.PyAudio()

    def start_recording(self):
        self.recording = True
        self.frames = []

        self.stream = self.audio.open(format=self.audio_format,
                                      channels=self.channels,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk)

        print("recording")
        self.worker = RecordWorker(self.stream, self.frames, self.chunk)
        self.worker.start()
        signal.signal(signal.SIGINT, self.on_worker_finished)

    def stop_recording(self):
        self.recording = False
        self.worker.stop()
        self.stream.stop_stream()
        self.stream.close()

        wf = wave.open('Backend/MediaRecorder/audio.wav', 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print("recording stopped>... filed saved")

    def on_worker_finished(self):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()

        wf = wave.open('Backend/MediaRecorder/audio.wav', 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
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
