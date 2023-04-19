from Frontend.src.Document_Formatter import *
from Backend.Database.lesson_db import lesson_data as ld
import os
import json
import shutil


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
        if(os.path.exists('Lessons/মডিউলসমূহ')): 
            moduleNames = os.listdir('Lessons/মডিউলসমূহ') 

            for folder in moduleNames:
                if 'মডিউল' in folder: 
                    items = os.listdir('Lessons/মডিউলসমূহ/' + folder)

                    for item in items:
                        if item == 'content.json':
                            with open('Lessons/মডিউলসমূহ/' + folder + '/' + item) as f:
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
            model = self.lesson_making_window.lsn_new_module_list_view.model()
            model.removeRow(selected_index.row())

    def make_lesson(self):
          
        # count the number of 'পাঠ' folders in the 'Lessons' folder
        sub_folders = os.listdir('Lessons/পাঠসমূহ')
        
        if len(sub_folders) == 0:
            lesson_serial_no = 0
        else:
            lesson_serial_no = 0
            tmp_serial = []
            
            for folder in sub_folders:
                serial = folder.split('_')[1]
                tmp_serial.append(serial)
                
            lesson_serial_no = int(max(tmp_serial))
                
        # create a new folder for the lesson
        folder_name = 'Lessons/পাঠসমূহ/পাঠ_' + str(lesson_serial_no + 1)
        os.path.exists(folder_name) or os.mkdir(folder_name) 
        
        # copy the selected modules into the new lesson folder
        model = self.lesson_making_window.lsn_new_module_list_view.model()
        for row in range(model.rowCount()):
            index = model.index(row, 0)
            item = model.data(index)
            if 'মডিউল' in item: 
                sub_folder_name = 'Lessons/পাঠসমূহ/পাঠ_' + str(lesson_serial_no + 1) + '/' + item
                os.mkdir(sub_folder_name)
                shutil.copytree('Lessons/মডিউলসমূহ/' + item, sub_folder_name, dirs_exist_ok=True)
            
        print('Lesson created successfully')	
        self.lesson_making_window.lsn_new_module_list_view.model().clear() 
        show_success_message('পাঠ তৈরি করা হয়েছে', 'পাঠ তৈরি করা হয়েছে। পাঠটি দেখতে পাঠ সমূহ ফোল্ডারটি দেখুন')
     
    def show_lessons(self):
        
        # open lesson folder  
        os.startfile('Lessons\পাঠসমূহ')
               
    
            
        
