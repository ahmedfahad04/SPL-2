# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Student_details.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setMinimumSize(QtCore.QSize(1180, 80))
        self.top_frame.setStyleSheet("background-color: #2B4865;\n"
"border-radius: 20px;")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back_to_home = QtWidgets.QPushButton(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back_to_home.sizePolicy().hasHeightForWidth())
        self.btn_back_to_home.setSizePolicy(sizePolicy)
        self.btn_back_to_home.setMinimumSize(QtCore.QSize(0, 60))
        self.btn_back_to_home.setMaximumSize(QtCore.QSize(60, 60))
        self.btn_back_to_home.setBaseSize(QtCore.QSize(0, 4))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_back_to_home.setFont(font)
        self.btn_back_to_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back_to_home.setMouseTracking(True)
        self.btn_back_to_home.setStyleSheet("QPushButton {\n"
"    background-color: #2B4865 #256D85;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"    background-color:  #256D85;\n"
"    border-radius: 30px;\n"
"}")
        self.btn_back_to_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\back_48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back_to_home.setIcon(icon)
        self.btn_back_to_home.setIconSize(QtCore.QSize(200, 200))
        self.btn_back_to_home.setAutoDefault(False)
        self.btn_back_to_home.setDefault(False)
        self.btn_back_to_home.setFlat(False)
        self.btn_back_to_home.setObjectName("btn_back_to_home")
        self.horizontalLayout.addWidget(self.btn_back_to_home)
        self.label = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #8FE3CF")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.top_frame)
        self.mid_frame = QtWidgets.QFrame(self.centralwidget)
        self.mid_frame.setMinimumSize(QtCore.QSize(1180, 610))
        self.mid_frame.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 220, 243);")
        self.mid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mid_frame.setObjectName("mid_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mid_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.mid_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"    background-color: #002B5B;\n"
"    color: rgb(143, 227, 207);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {\n"
"    background-color: #256D85;\n"
"    gridline-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"    color: #fff;\n"
"}\n"
"\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(13)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(13)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget.verticalHeader().setMinimumSectionSize(29)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.mid_frame)
        self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
        self.bottom_frame.setMinimumSize(QtCore.QSize(1180, 70))
        self.bottom_frame.setStyleSheet("background-color: rgb(42, 70, 98);\n"
"border-radius: 20px;")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_add_new_student = QtWidgets.QPushButton(self.bottom_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(230)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.btn_add_new_student.sizePolicy().hasHeightForWidth())
        self.btn_add_new_student.setSizePolicy(sizePolicy)
        self.btn_add_new_student.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_add_new_student.setFont(font)
        self.btn_add_new_student.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_new_student.setStyleSheet("QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    \n"
"    background-color: rgb(143, 227, 207);\n"
"    color: #2B4865;\n"
"\n"
"}")
        self.btn_add_new_student.setObjectName("btn_add_new_student")
        self.horizontalLayout_3.addWidget(self.btn_add_new_student)
        spacerItem1 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_remove_student = QtWidgets.QPushButton(self.bottom_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(230)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.btn_remove_student.sizePolicy().hasHeightForWidth())
        self.btn_remove_student.setSizePolicy(sizePolicy)
        self.btn_remove_student.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Hind Siliguri Medium")
        font.setPointSize(12)
        self.btn_remove_student.setFont(font)
        self.btn_remove_student.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_remove_student.setStyleSheet("QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    \n"
"    background-color: rgb(143, 227, 207);\n"
"    color: #2B4865;\n"
"\n"
"}")
        self.btn_remove_student.setObjectName("btn_remove_student")
        self.horizontalLayout_3.addWidget(self.btn_remove_student)
        spacerItem2 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.bottom_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "শিক্ষার্থীর তথ্যসমূহ "))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "শিক্ষার্থীর আইডি"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "শিক্ষার্থীর নাম"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "শিক্ষার্থীর বয়স "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "অভিভাবকের নাম"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "অভিভাবকের মোবাইল নম্বর"))
        self.btn_add_new_student.setText(_translate("MainWindow", "নতুন শিক্ষার্থী যুক্ত করুন"))
        self.btn_remove_student.setText(_translate("MainWindow", "শিক্ষার্থী এন্ট্রি বাতিল করুন"))
