from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# ==> Helper functions: Align the elements in the table
def align_elements(ui_object):
    rows = ui_object.tableWidget.rowCount()
    columns = ui_object.tableWidget.columnCount()

    for row in range(rows):
        for column in range(columns):
            item = ui_object.tableWidget.item(row, column)
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
