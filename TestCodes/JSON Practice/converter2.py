import json


class MyClass:
    def __init__(self, name, age, image_path):
        self.name = name
        self.age = age
        self.image_path = image_path


# Create an instance of MyClass
my_object = MyClass("John", 30, "TestCodes/JSON Practice/img.png")

# Convert the object to a JSON string
json_string = json.dumps(my_object.__dict__)

# Print the JSON string
print(json_string)

