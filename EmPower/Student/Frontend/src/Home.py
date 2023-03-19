from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *

class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.lesson_list = ''
        self.home_page()

    def home_page(self):
        
        # load & set up the HOME page
        self.home = ui_home.Ui_MainWindow()
        self.home.setupUi(self)
        
        # set window icon and title
        # TODO: Show the window at the middle of the screen
        # self.setGeometry(480, 270, 0, 0)
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        set_drop_shadow(self.home.btn_lesson)
        set_drop_shadow(self.home.btn_evaluation)
        self.home.edit_lesson_list.setReadOnly(True)
        
        # Navigate between pages
        self.home.stackedWidget.setCurrentWidget(self.home.home_page)
        self.home.btn_lesson.clicked.connect(self.upload_lesson_page)
        
    def upload_lesson_page(self):
        
        # TODO: should view from unfinished lesson
        
        self.home.btn_select_folder.clicked.connect(self.upload_lesson)
        
        # Navigate between pages
        self.home.btn_back_to_home.clicked.connect(self.home_page)
        self.home.bnt_start_lesson.clicked.connect(self.lesson_page)
        self.home.stackedWidget.setCurrentWidget(self.home.upload_lesson_page)
        
    def lesson_page(self):
        
        # Navigate between pages
        self.home.btn_back_to_home_2.clicked.connect(self.upload_lesson_page)
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_page)
        
    def upload_lesson(self):
                
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        file_view = file_dialog.findChild(QListView, 'listView')

        # to make it possible to select multiple directories:
        if file_view:
            file_view.setSelectionMode(QAbstractItemView.MultiSelection)
            
        f_tree_view = file_dialog.findChild(QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QAbstractItemView.MultiSelection)

        if file_dialog.exec():
            paths = file_dialog.selectedFiles()
            
        
        for path in paths:
            if '_' not in path: continue
            path = path.split('/')[-1]
            self.lesson_list += path + '\n'
            
                        
        self.home.edit_lesson_list.setText(self.lesson_list)
        self.home.bnt_start_lesson.setEnabled(True)