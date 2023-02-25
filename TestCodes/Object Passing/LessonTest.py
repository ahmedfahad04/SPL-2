import dill
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication

class MyPyQtObject(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Click me')
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

app = QApplication([])
obj = MyPyQtObject()
# do something with the object

# serialize the object
serialized_obj = dill.dumps(obj, recurse=True)

# deserialize the object
deserialized_obj = dill.loads(serialized_obj)
# use the deserialized object

# show the deserialized object
deserialized_obj.show()
app.exec_()
