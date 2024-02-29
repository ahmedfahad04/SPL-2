import os
import threading
import pygame
import time

import pyaudio

class MusicPlayer:

    def __init__(self, music_file_path):
        self.music_file_path = music_file_path
        self.play_music_continuously = False
        self.music_thread = None
        if self.check_audio_devices():
            print("audio device found")
            pygame.mixer.init()
        else:
            print("no audio device")

    def check_audio_devices(self):
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')

        output_devices = []
        for i in range(num_devices):
            device_info = p.get_device_info_by_host_api_device_index(0, i)
            if device_info.get('maxOutputChannels') > 0:
                output_devices.append(device_info.get('name'))

        if output_devices:
            print("Audio output device found.")
            return True
        else:
            print("No audio output device found. Connect an audio device and try again.")
            return False

    def play_music(self):
        pygame.mixer.init()

        self.play_music_continuously = True
        pygame.mixer.music.load(self.music_file_path)

        try:
            while self.play_music_continuously:
                pygame.mixer.init()
                pygame.mixer.music.play()

                # Wait for the music to finish playing
                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                # Wait for 2 seconds before playing the music again
                time.sleep(2)
        except Exception as e:
            print(e)

    def start_music(self):
        self.music_thread = threading.Thread(target=self.play_music, daemon=True)
        self.music_thread.start()

    def stop_music(self):
        self.play_music_continuously = False

        # if self.music_thread is not None:
        #     self.music_thread.join()

        # Stop the music before quitting the mixer
        pygame.mixer.init()
        pygame.mixer.music.pause()
        pygame.mixer.music.stop()

        pygame.mixer.quit()
        pygame.quit()
