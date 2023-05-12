import os
import threading
import pygame
import time

class MusicPlayer:
    
    def __init__(self, music_file_path):
        self.music_file_path = music_file_path
        self.play_music_continuously = False
        self.music_thread = None
        pygame.mixer.init()

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
