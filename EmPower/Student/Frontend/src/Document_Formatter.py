from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


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


def filter_data(text):
    
    print("DATA: ", text)
    
    # filter number to bengali
    bengali_numeral_map = {
        '0':'০',
        '1':'১', 
        '2':'২',
        '3':'৩',
        '4':'৪',
        '5':'৫',
        '6':'৬',
        '7':'৭',
        '8':'৮', 
        '9':'৯'
    }

    text = text.replace('_', ' ')
    text = text.translate(str.maketrans(bengali_numeral_map))
            
    return text 
