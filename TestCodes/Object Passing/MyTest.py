import pickle
import MyClass   # just for the class skeleton

# load the instance of the class from the file
with open('my_object.pickle', 'rb') as f:
    my_object = pickle.load(f)

# use the instance of the class
print(my_object.add())  # Output: 3
my_object.show_image() # show image
