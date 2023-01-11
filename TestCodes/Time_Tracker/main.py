import time

# currentTime = time.time()
# print(currentTime)
#
# print(160//60)

import time

t = 1

def countdown(t):

    while True:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t += 1
        print(timeformat)

        if t > 5:
            break


import threading


def print_cube(num):
    time.sleep(1)

    # function to print cube of given num
    print("Cube: {}".format(num * num * num))


def print_square(num):
    # function to print square of given num
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=countdown, args=(t,))
    # t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    # t2.start()
    # starting thread 2
    t1.start()



    # wait until thread 1 is completely executed
    t1.join()
    print("Main Thread")

    # wait until thread 2 is completely executed
    # t2.join()

    # both threads completely executed
    print("Done!")

