from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys 


# ==> Helper functions: Align the elements in the table
def align_elements(ui_object):
    rows = ui_object.rowCount()
    columns = ui_object.columnCount()

    for row in range(rows):
        for column in range(columns):
            item = ui_object.item(row, column)
            if item is not None:
                item.setTextAlignment(Qt.AlignCenter)


# ==> Helper functions: Apply drop shadow effect to the buttons
def set_drop_shadow(ui_object):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setXOffset(5)
    shadow.setYOffset(7)
    shadow.setColor(QColor(255, 255, 255, 55))
    ui_object.setGraphicsEffect(shadow)
    
def show_warning_message(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.setWindowIcon(QIcon("Frontend\Images\warning_icon.png"))
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    msg.exec_()
    
    if msg.clickedButton() == msg.button(QMessageBox.StandardButton.Ok):
        return True
    else: 
        return False
    
def show_success_message(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.setWindowIcon(QIcon("Frontend\Images\done.png"))
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    msg.exec_()
    
    if msg.clickedButton() == msg.button(QMessageBox.StandardButton.Ok):
        return True
    else: 
        return False
    
def show_confirmation_message(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.setWindowIcon(QIcon("Frontend\Images\question_icon.png"))
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    msg.exec_()
    
    if msg.clickedButton() == msg.button(QMessageBox.StandardButton.Ok):
        return True 
    else: 
        return False

def restart():
    QCoreApplication.quit()
    status = QProcess.startDetached(sys.executable, sys.argv)
    print(status)
    
def align_lineEdit_elements(text_edit):
    text_option = QTextOption()
    text_option.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    text_edit.document().setDefaultTextOption(text_option)