import pickle
import MyLesson   # just for the class skeleton

# load the instance of the class from the file
with open('my_lesson.pickle', 'rb') as f:
    std_lesson = pickle.load(f)

# use the instance of the class
std_lesson.show()
