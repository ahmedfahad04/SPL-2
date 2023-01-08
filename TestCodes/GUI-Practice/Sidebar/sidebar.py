# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_with_lbl_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_with_lbl_widget.setMinimumSize(QtCore.QSize(200, 803))
        self.icon_with_lbl_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.icon_with_lbl_widget.setObjectName("icon_with_lbl_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icon_with_lbl_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sidebar_lbl = QtWidgets.QLabel(self.icon_with_lbl_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sidebar_lbl.setFont(font)
        self.sidebar_lbl.setObjectName("sidebar_lbl")
        self.verticalLayout_4.addWidget(self.sidebar_lbl)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.home_large_btn = QtWidgets.QPushButton(self.icon_with_lbl_widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/home-outline.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_large_btn.setIcon(icon)
        self.home_large_btn.setCheckable(True)
        self.home_large_btn.setAutoExclusive(True)
        self.home_large_btn.setObjectName("home_large_btn")
        self.verticalLayout_3.addWidget(self.home_large_btn)
        self.files_large_btn = QtWidgets.QPushButton(self.icon_with_lbl_widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.files_large_btn.setIcon(icon1)
        self.files_large_btn.setCheckable(True)
        self.files_large_btn.setAutoExclusive(True)
        self.files_large_btn.setObjectName("files_large_btn")
        self.verticalLayout_3.addWidget(self.files_large_btn)
        self.people_large_btn = QtWidgets.QPushButton(self.icon_with_lbl_widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/people.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.people_large_btn.setIcon(icon2)
        self.people_large_btn.setCheckable(True)
        self.people_large_btn.setAutoExclusive(True)
        self.people_large_btn.setObjectName("people_large_btn")
        self.verticalLayout_3.addWidget(self.people_large_btn)
        self.records_large_btn = QtWidgets.QPushButton(self.icon_with_lbl_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/bookmark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.records_large_btn.setIcon(icon3)
        self.records_large_btn.setCheckable(True)
        self.records_large_btn.setObjectName("records_large_btn")
        self.verticalLayout_3.addWidget(self.records_large_btn)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 559, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.exit_large_btn = QtWidgets.QPushButton(self.icon_with_lbl_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resources/close-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_large_btn.setIcon(icon4)
        self.exit_large_btn.setObjectName("exit_large_btn")
        self.verticalLayout_4.addWidget(self.exit_large_btn)
        self.gridLayout.addWidget(self.icon_with_lbl_widget, 0, 1, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setMinimumSize(QtCore.QSize(845, 803))
        self.main_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main_widget.setObjectName("main_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_btn = QtWidgets.QPushButton(self.main_widget)
        self.menu_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/resources/ellipsis-vertical.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon5)
        self.menu_btn.setCheckable(True)
        self.menu_btn.setAutoExclusive(True)
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout.addWidget(self.menu_btn)
        self.prev_btn = QtWidgets.QPushButton(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_btn.sizePolicy().hasHeightForWidth())
        self.prev_btn.setSizePolicy(sizePolicy)
        self.prev_btn.setMinimumSize(QtCore.QSize(50, 28))
        self.prev_btn.setMaximumSize(QtCore.QSize(100, 28))
        self.prev_btn.setObjectName("prev_btn")
        self.horizontalLayout.addWidget(self.prev_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lesson_linedit = QtWidgets.QLineEdit(self.main_widget)
        self.lesson_linedit.setMinimumSize(QtCore.QSize(300, 35))
        self.lesson_linedit.setMaximumSize(QtCore.QSize(300, 28))
        self.lesson_linedit.setInputMask("")
        self.lesson_linedit.setCursorPosition(8)
        self.lesson_linedit.setAlignment(QtCore.Qt.AlignCenter)
        self.lesson_linedit.setReadOnly(True)
        self.lesson_linedit.setObjectName("lesson_linedit")
        self.horizontalLayout.addWidget(self.lesson_linedit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.next_btn = QtWidgets.QPushButton(self.main_widget)
        self.next_btn.setMinimumSize(QtCore.QSize(50, 28))
        self.next_btn.setMaximumSize(QtCore.QSize(100, 28))
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem3)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(820, 800))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page_0 = QtWidgets.QWidget()
        self.home_page_0.setObjectName("home_page_0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home_page_0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.home_lbl = QtWidgets.QLabel(self.home_page_0)
        self.home_lbl.setMinimumSize(QtCore.QSize(200, 50))
        self.home_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.home_lbl.setFont(font)
        self.home_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.home_lbl.setObjectName("home_lbl")
        self.gridLayout_2.addWidget(self.home_lbl, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.home_page_0)
        self.files__page_1 = QtWidgets.QWidget()
        self.files__page_1.setObjectName("files__page_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.files__page_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.file_lbl = QtWidgets.QLabel(self.files__page_1)
        self.file_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.file_lbl.setFont(font)
        self.file_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.file_lbl.setObjectName("file_lbl")
        self.gridLayout_3.addWidget(self.file_lbl, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.files__page_1)
        self.students_page_2 = QtWidgets.QWidget()
        self.students_page_2.setObjectName("students_page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.students_page_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.student_lbl = QtWidgets.QLabel(self.students_page_2)
        self.student_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.student_lbl.setFont(font)
        self.student_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.student_lbl.setObjectName("student_lbl")
        self.gridLayout_4.addWidget(self.student_lbl, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.students_page_2)
        self.records_page_3 = QtWidgets.QWidget()
        self.records_page_3.setObjectName("records_page_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.records_page_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.records_lbl = QtWidgets.QLabel(self.records_page_3)
        self.records_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.records_lbl.setFont(font)
        self.records_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.records_lbl.setObjectName("records_lbl")
        self.gridLayout_5.addWidget(self.records_lbl, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.records_page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.main_widget, 0, 2, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setMinimumSize(QtCore.QSize(50, 803))
        self.icon_only_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo_lbl = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_lbl.setMinimumSize(QtCore.QSize(60, 30))
        self.logo_lbl.setMaximumSize(QtCore.QSize(100, 30))
        self.logo_lbl.setStyleSheet("border-image: url(:/logo/resources/rsz_default.jpg);")
        self.logo_lbl.setText("")
        self.logo_lbl.setObjectName("logo_lbl")
        self.verticalLayout_2.addWidget(self.logo_lbl)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_small_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_small_btn.setText("")
        self.home_small_btn.setIcon(icon)
        self.home_small_btn.setCheckable(True)
        self.home_small_btn.setAutoExclusive(True)
        self.home_small_btn.setObjectName("home_small_btn")
        self.verticalLayout.addWidget(self.home_small_btn)
        self.files_small_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.files_small_btn.setText("")
        self.files_small_btn.setIcon(icon1)
        self.files_small_btn.setCheckable(True)
        self.files_small_btn.setAutoExclusive(True)
        self.files_small_btn.setObjectName("files_small_btn")
        self.verticalLayout.addWidget(self.files_small_btn)
        self.people_small_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.people_small_btn.setText("")
        self.people_small_btn.setIcon(icon2)
        self.people_small_btn.setCheckable(True)
        self.people_small_btn.setAutoExclusive(True)
        self.people_small_btn.setObjectName("people_small_btn")
        self.verticalLayout.addWidget(self.people_small_btn)
        self.record_small_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.record_small_btn.setText("")
        self.record_small_btn.setIcon(icon3)
        self.record_small_btn.setCheckable(True)
        self.record_small_btn.setAutoExclusive(True)
        self.record_small_btn.setObjectName("record_small_btn")
        self.verticalLayout.addWidget(self.record_small_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 559, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.exit_small_btn = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_small_btn.setText("")
        self.exit_small_btn.setIcon(icon4)
        self.exit_small_btn.setObjectName("exit_small_btn")
        self.verticalLayout_2.addWidget(self.exit_small_btn)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.home_small_btn.toggled['bool'].connect(self.home_large_btn.setChecked)
        self.files_small_btn.toggled['bool'].connect(self.files_large_btn.setChecked)
        self.people_small_btn.toggled['bool'].connect(self.people_large_btn.setChecked)
        self.home_large_btn.toggled['bool'].connect(self.home_small_btn.setChecked)
        self.files_large_btn.toggled['bool'].connect(self.files_small_btn.setChecked)
        self.people_large_btn.toggled['bool'].connect(self.people_small_btn.setChecked)
        self.exit_small_btn.clicked.connect(MainWindow.close)
        self.exit_large_btn.clicked.connect(MainWindow.close)
        self.record_small_btn.toggled['bool'].connect(self.records_large_btn.setChecked)
        self.records_large_btn.toggled['bool'].connect(self.record_small_btn.setChecked)
        self.menu_btn.toggled['bool'].connect(self.icon_with_lbl_widget.setVisible)
        self.menu_btn.toggled['bool'].connect(self.icon_only_widget.setHidden)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sidebar_lbl.setText(_translate("MainWindow", "Side Bar"))
        self.home_large_btn.setText(_translate("MainWindow", "Home"))
        self.files_large_btn.setText(_translate("MainWindow", "Files"))
        self.people_large_btn.setText(_translate("MainWindow", "Students"))
        self.records_large_btn.setText(_translate("MainWindow", "Records"))
        self.exit_large_btn.setText(_translate("MainWindow", "Exit"))
        self.prev_btn.setText(_translate("MainWindow", "<< Previous"))
        self.lesson_linedit.setText(_translate("MainWindow", "Lesson 1"))
        self.next_btn.setText(_translate("MainWindow", "Next >>"))
        self.home_lbl.setText(_translate("MainWindow", "Home"))
        self.file_lbl.setText(_translate("MainWindow", "Files"))
        self.student_lbl.setText(_translate("MainWindow", "Students"))
        self.records_lbl.setText(_translate("MainWindow", "Records"))
import files_rc
