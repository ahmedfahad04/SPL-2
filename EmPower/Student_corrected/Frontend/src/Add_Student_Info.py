import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Frontend.Student_UI.ui_student_info import Ui_Student_Info


class Add_Student_info:
    
    def __init__(self) -> None:
        
        self.std_name = None
        self.std_id = None
        self.img_url = None 
        self.ui = None
        
        self.initUI()
        
    def initUI(self):
         
        Form = QWidget()
        ui = Ui_Student_Info()
        ui.setupUi(Form)
        
    def add_details(self):
            
        # create form
    
        
        
        # connect button
        self.ui.btn_submit.clicked.connect(self.save_info)
        
        # sys.exit(app.exec_()) 
        
    def save_info(self):
        
        # get values
        self.std_name = self.ui.lbl_std_name.text()
        self.std_id = self.ui.lbl_std_id.text()
        
        