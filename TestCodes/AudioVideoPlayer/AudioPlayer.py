import pygame

# setting up pygame
pygame.init()


def insert_into_playlist(playlist, music_file):
    # Adding songs file in our playlist
    playlist.append(music_file)


def start_playlist(playList):
    # Loading first audio file into our player
    pygame.mixer.music.load(playList[0])

    # Removing the loaded song from our playlist list
    playList.pop(0)

    # Playing our music
    pygame.mixer.music.play()

    # Queueing next song into our player
    pygame.mixer.music.queue(playList[0])
    playList.pop(0)

    # setting up an end event which host an event
    # after the end of every song
    pygame.mixer.music.set_endevent(pygame.MUSIC_END)

    # Playing the songs in the background
    running = True
    while running:

        # checking if any event has been
        # hosted at time of playing
        for event in pygame.event.get():

            # A event will be hosted
            # after the end of every song
            if event.type == pygame.MUSIC_END:
                print('Song Finished')

                # Checking our playList
                # that if any song exist or
                # it is empty
                if len(playList) > 0:
                    # if song available then load it in player
                    # and remove from the player
                    pygame.mixer.music.queue(playList[0])
                    playList.pop(0)

            # Checking whether the
            # player is still playing any song
            # if yes it will return true and false otherwise
            if not pygame.mixer.music.get_busy():
                print("Playlist completed")

                # When the playlist has
                # completed playing successfully
                # we'll go out of the
                # while-loop by using break
                running = False
                break


if __name__ == '__main__':
    # This list is going to be
    # our playlist as we can
    # only queue one song at a
    # time by using `.queue()` method
    # therefore we are using list
    # and will queue song one by one.
    playList = []

    insert_into_playlist(playList, 'FreeMP3.mp3')
    insert_into_playlist(playList, 'Free_Test_Data_1MB_OGG.ogg')
    insert_into_playlist(playList, 'mixkit-game-show-suspense-waiting-667.wav')

    start_playlist(playList)
