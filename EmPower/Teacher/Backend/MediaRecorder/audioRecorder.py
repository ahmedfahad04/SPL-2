import pyaudio
import wave


class AudioRecorder:
    def __init__(self):
        
        # Define the default audio settings
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.frames = []
        self.quitCommandFlag = False

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

    def start_recording(self):
        self.p = pyaudio.PyAudio()  # Initialize the PyAudio object

        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE,
                                  input=True, frames_per_buffer=self.CHUNK)

        print("Recording... Press stop button to stop recording.")
        self.frames = []
        while True:
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)

            if self.quitCommandFlag:
                break

    def stop_recording(self, fileName):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(fileName, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        print("Finished recording.")


# Example usage:
recorder = AudioRecorder()

recorder.start_recording()  # for now this will go to infinite loop
                            # because i have reorganized the code to user's perspective
                            # when the user click stop button the recorder.set_quitCommandFlag will
                            # be set true and this will stop
recorder.set_quitCommandFlag()
fileName = input()
recorder.stop_recording(fileName + ".wav")
