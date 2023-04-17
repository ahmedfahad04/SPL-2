from Frontend.src.Document_Formatter import *
from Backend.Database.lesson_db import lesson_data as ld
import os 
import json 


class Lesson_Making_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()
        
        # window
        self.lesson_making_window = ui_object
        self.form = None
        
        
        self.populate_module_data()
        
        
    
    def getFolderDetails(self):
        
        moduleNames = []
        moduleDescriptsions = []
        table_data = []
        
        # read the folders
        if(os.path.exists('Lessons')):
            moduleNames = os.listdir('Lessons')
            
            for folder in moduleNames:
                items = os.listdir('Lessons/' + folder)
                
                for item in items:
                    if item == 'content.json':
                        with open('Lessons/' + folder + '/' + item) as f:
                            data = json.load(f)
                            moduleDescriptsions.append(data['module_topic']) 
                            break
                        
        for col1, col2 in zip(moduleNames, moduleDescriptsions):
            table_data.append([col1, col2])
                        
        return table_data        
        
    def populate_module_data(self):
        
        tableRowContent = self.getFolderDetails()
        
        rows = len(tableRowContent)
        columns = self.lesson_making_window.lsn_module_table_widget.columnCount()
        self.lesson_making_window.lsn_module_table_widget.setRowCount(rows)

        # store the reloaded value into the PyQt_UI
        for row in range(rows):
            for col in range(columns):
                self.lesson_making_window.lsn_module_table_widget.setItem(
                    row, col, QTableWidgetItem(str(tableRowContent[row][col])))
            
    
    def remove_list_item(self):
        
        selected_indexes = self.lesson_making_window.lsn_new_module_list_view.selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            print(selected_index.row())
            model = self.lesson_making_window.lsn_new_module_list_view.model()
            model.removeRow(selected_index.row())
        
        
         