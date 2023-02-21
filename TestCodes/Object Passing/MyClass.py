import pickle
from PIL import Image

class MyClass:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_path = image_path
    
    def add(self):
        return self.x + self.y
    
    def show_image(self):
        img = Image.open(self.image_path)
        img.show()

# create an instance of the class and save it to a file
my_object = MyClass(1, 2, "nature.jfif")
with open('my_object.pickle', 'wb') as f:
    pickle.dump(my_object, f)
