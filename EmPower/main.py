from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys 
from ui_home import Ui_MainWindow

class MainWindow(QMainWindow):        # Home extends QMainWindow
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.loadHomePage()
       
      
     
    def loadHomePage(self):
        """
            This function loads the home page.
        """ 
        # load & setup the HOME page
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # add additional code for home page
        self.setWindowIcon(QIcon("UI\only_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        
        self.ui.btn_lesson.clicked.connect(lambda: print("Lesson"))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())