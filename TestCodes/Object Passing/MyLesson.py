import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
import sys
from Lesson import *


class MyLesson(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.LessonPage = Ui_MainWindow()
        self.LessonPage.setupUi(self)
        # class variables
        self.MyText = ""

        self.TextHandler()

    def TextHandler(self):
        self.LessonPage.SubmitButton.clicked.connect(self.inputText)
       # self.LessonPage.CreateLesson.clicked.connect(self.createNewLesson)

    def inputText(self):
        MyText = self.LessonPage.textEdit.toPlainText()
        print(MyText)
    # def createNewLesson(self):
    #     with open('my_lesson.pickle', 'wb') as f:
    #         pickle.dump(lesson, f)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    lesson = MyLesson()
    lesson.show()
    print(type(lesson))

    # Save the object to a file
    with open('myLesson_object.txt', 'w') as f:
        f.write(str(lesson))

    sys.exit(app.exec_())
