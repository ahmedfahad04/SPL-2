import pickle
import MyLesson   # just for the class skeleton

# # load the instance of the class from the file
# with open('my_lesson.pickle', 'rb') as f:
#     std_lesson = pickle.load(f)
#
# # use the instance of the class
# std_lesson.show()


# Load the object from the file
with open('myLesson_object.txt', 'r') as f:
    data = f.read()

# Deserialize the data into a PyQt object
my_object = eval(data)

print(my_object.MyText)