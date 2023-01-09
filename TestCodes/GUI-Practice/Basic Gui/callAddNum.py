import sys
from PyQt5.QtWidgets import QDialog, QApplication

from addNum import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.display_sum)
        self.show()

    def display_sum(self):
        num1 = int(self.ui.firstNumBox.text())
        num2 = int(self.ui.secondNumBox.text())
        self.ui.sumBox.setText(str(num1 + num2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myForm = MyForm()
    myForm.show()
    sys.exit(app.exec_())
