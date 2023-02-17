import json


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "method": self.my_method.__name__
        }

    def my_method(self):
        print("Hello, World!")


class MyClassEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MyClass):
            return obj.to_dict()
        if callable(obj):
            return obj.__name__
        return json.JSONEncoder.default(self, obj)


# Create an instance of MyClass
my_object = MyClass("John", 30)

# Convert the object to a JSON string
json_string = json.dumps(my_object, cls=MyClassEncoder)

# Print the JSON string
print(json_string)

############   WE can't convert method into JSON representation
#                   just can store method name      ############
