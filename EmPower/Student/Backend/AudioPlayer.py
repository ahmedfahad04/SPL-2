import threading
import pygame
import time

class MusicPlayer:
    
    def __init__(self, music_file_path):
        self.music_file_path = music_file_path
        self.play_music_continuously = False
        self.music_thread = None

    def play_music(self):
        pygame.mixer.music.load(self.music_file_path)
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    def start_music(self):
        pygame.mixer.init()
        self.music_thread = threading.Thread(target=self.play_music)
        self.music_thread.start()

    def stop_music(self):
        self.play_music_continuously = False

        if self.music_thread is not None:
            self.music_thread.join()

        # Stop the music before quitting the mixer
        pygame.mixer.music.stop()

        pygame.mixer.quit()
        pygame.quit()
