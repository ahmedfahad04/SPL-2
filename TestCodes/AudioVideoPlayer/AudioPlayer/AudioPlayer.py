import pygame


pygame.mixer.init()  # Initialize the mixer module.
sound1 = pygame.mixer.Sound('musics/FreeMP3.mp3')  # Load a sound.

while True:
    try:
        inpt = input('Press enter to play the sound: ')
        sound1.play()  # Play the sound.
        print('Playing sound')
    except KeyboardInterrupt:
        break

