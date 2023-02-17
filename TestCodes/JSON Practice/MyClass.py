import json
from json import JSONEncoder


class MyClass:
    myName = "asif"
    myRoll = 1217

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


myClassObject = MyClass()
print(myClassObject.myName)
print(myClassObject.toJSON())
# wJsonMyClassObject = json.dumps(myClassObject)
MyEncoder().encode(myClassObject)
jsonMyClassObject = json.dumps(myClassObject, default=dumper,
                               sort_keys=True, indent=4)

# print(wJsonMyClassObject)
print(jsonMyClassObject)

print(json.dumps(name="asif"))
