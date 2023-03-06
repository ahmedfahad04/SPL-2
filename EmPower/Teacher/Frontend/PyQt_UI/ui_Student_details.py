# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student_details.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(1180, 80))
        self.top_frame.setStyleSheet(u"background-color: #2B4865;\n"
"border-radius: 20px;")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_back_to_home = QPushButton(self.top_frame)
        self.btn_back_to_home.setObjectName(u"btn_back_to_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_back_to_home.sizePolicy().hasHeightForWidth())
        self.btn_back_to_home.setSizePolicy(sizePolicy2)
        self.btn_back_to_home.setMinimumSize(QSize(0, 60))
        self.btn_back_to_home.setMaximumSize(QSize(60, 60))
        self.btn_back_to_home.setBaseSize(QSize(0, 4))
        font = QFont()
        font.setPointSize(11)
        self.btn_back_to_home.setFont(font)
        self.btn_back_to_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_to_home.setMouseTracking(True)
        self.btn_back_to_home.setStyleSheet(u"QPushButton {\n"
"	background-color: #2B4865 #256D85;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color:  #256D85;\n"
"	border-radius: 30px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Images/back_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back_to_home.setIcon(icon)
        self.btn_back_to_home.setIconSize(QSize(200, 200))
        self.btn_back_to_home.setAutoDefault(False)
        self.btn_back_to_home.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_back_to_home)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Hind Siliguri Medium"])
        font1.setPointSize(27)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #8FE3CF")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(self.centralwidget)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setMinimumSize(QSize(1180, 610))
        self.mid_frame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(255, 220, 243);")
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mid_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.mid_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font2 = QFont()
        font2.setFamilies([u"Hind Siliguri Medium"])
        font2.setPointSize(13)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font3 = QFont()
        font3.setFamilies([u"Hind Siliguri Medium"])
        font3.setPointSize(13)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: #002B5B;\n"
"    color: rgb(143, 227, 207);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {\n"
"	background-color: #256D85;\n"
"	gridline-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(29)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)

        self.horizontalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(1180, 70))
        self.bottom_frame.setStyleSheet(u"background-color: rgb(42, 70, 98);\n"
"border-radius: 20px;")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btn_add_new_student = QPushButton(self.bottom_frame)
        self.btn_add_new_student.setObjectName(u"btn_add_new_student")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(230)
        sizePolicy3.setVerticalStretch(40)
        sizePolicy3.setHeightForWidth(self.btn_add_new_student.sizePolicy().hasHeightForWidth())
        self.btn_add_new_student.setSizePolicy(sizePolicy3)
        self.btn_add_new_student.setMinimumSize(QSize(250, 40))
        font4 = QFont()
        font4.setFamilies([u"Hind Siliguri Medium"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.btn_add_new_student.setFont(font4)
        self.btn_add_new_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_new_student.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../Images/add_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_new_student.setIcon(icon1)
        self.btn_add_new_student.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.btn_add_new_student)

        self.horizontalSpacer = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_update_student_info = QPushButton(self.bottom_frame)
        self.btn_update_student_info.setObjectName(u"btn_update_student_info")
        sizePolicy3.setHeightForWidth(self.btn_update_student_info.sizePolicy().hasHeightForWidth())
        self.btn_update_student_info.setSizePolicy(sizePolicy3)
        self.btn_update_student_info.setMinimumSize(QSize(250, 40))
        self.btn_update_student_info.setFont(font4)
        self.btn_update_student_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_student_info.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../Images/edit_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update_student_info.setIcon(icon2)
        self.btn_update_student_info.setIconSize(QSize(20, 25))

        self.horizontalLayout_3.addWidget(self.btn_update_student_info)

        self.horizontalSpacer_2 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_remove_student = QPushButton(self.bottom_frame)
        self.btn_remove_student.setObjectName(u"btn_remove_student")
        sizePolicy3.setHeightForWidth(self.btn_remove_student.sizePolicy().hasHeightForWidth())
        self.btn_remove_student.setSizePolicy(sizePolicy3)
        self.btn_remove_student.setMinimumSize(QSize(250, 40))
        font5 = QFont()
        font5.setFamilies([u"Hind Siliguri Medium"])
        font5.setPointSize(12)
        self.btn_remove_student.setFont(font5)
        self.btn_remove_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_student.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(160, 253, 230);\n"
"color:  #256D85 ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(143, 227, 207);\n"
"	color: #2B4865;\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../Images/trash_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_student.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.btn_remove_student)

        self.horizontalSpacer_3 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_back_to_home.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_back_to_home.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a4\u09a5\u09cd\u09af\u09b8\u09ae\u09c2\u09b9 ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u0986\u0987\u09a1\u09bf", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09ac\u09df\u09b8 ", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0985\u09ad\u09bf\u09ad\u09be\u09ac\u0995\u09c7\u09b0 \u09ae\u09cb\u09ac\u09be\u0987\u09b2 \u09a8\u09ae\u09cd\u09ac\u09b0", None));
        self.btn_add_new_student.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.btn_update_student_info.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0\u09b0 \u09a4\u09a5\u09cd\u09af \u0986\u09aa\u09a1\u09c7\u099f \u0995\u09b0\u09c1\u09a8", None))
        self.btn_remove_student.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u098f\u09a8\u09cd\u099f\u09cd\u09b0\u09bf \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09c1\u09a8", None))
    # retranslateUi

