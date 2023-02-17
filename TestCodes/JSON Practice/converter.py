import json


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create an instance of MyClass
my_object = MyClass("John", 30)

# Convert the object to a JSON string
json_string = json.dumps(my_object.__dict__)

# Print the JSON string
print(json_string)
