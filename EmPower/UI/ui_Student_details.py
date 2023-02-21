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
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(1180, 81))
        self.top_frame.setStyleSheet(u"background-color: rgb(210, 145, 188);")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_back_to_home = QPushButton(self.top_frame)
        self.btn_back_to_home.setObjectName(u"btn_back_to_home")
        self.btn_back_to_home.setMaximumSize(QSize(100, 80))
        self.btn_back_to_home.setBaseSize(QSize(0, 4))
        font = QFont()
        font.setPointSize(11)
        self.btn_back_to_home.setFont(font)
        self.btn_back_to_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_to_home.setMouseTracking(True)
        self.btn_back_to_home.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(210, 145, 188);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"	background-color: rgb(191, 132, 171);\n"
"}")
        icon = QIcon()
        icon.addFile(u"back_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back_to_home.setIcon(icon)
        self.btn_back_to_home.setIconSize(QSize(150, 150))
        self.btn_back_to_home.setAutoDefault(False)
        self.btn_back_to_home.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_back_to_home)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(27)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #04253A")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(self.centralwidget)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setMinimumSize(QSize(1180, 610))
        self.mid_frame.setStyleSheet(u"")
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
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem19)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: rgb(149, 125, 173);\n"
"    color: rgb(3, 3, 3);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget {\n"
"	background-color: rgb(255, 220, 243);\n"
"	gridline-color: rgb(85, 0, 0);\n"
"}\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Raised)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(1180, 70))
        self.bottom_frame.setStyleSheet(u"background-color: rgb(210, 145, 188);")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add_new_student = QPushButton(self.bottom_frame)
        self.btn_add_new_student.setObjectName(u"btn_add_new_student")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(230)
        sizePolicy1.setVerticalStretch(40)
        sizePolicy1.setHeightForWidth(self.btn_add_new_student.sizePolicy().hasHeightForWidth())
        self.btn_add_new_student.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.btn_add_new_student.setFont(font4)
        self.btn_add_new_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_new_student.setStyleSheet(u"background-color: rgb(148, 125, 172);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.btn_add_new_student)

        self.btn_remove_student = QPushButton(self.bottom_frame)
        self.btn_remove_student.setObjectName(u"btn_remove_student")
        sizePolicy1.setHeightForWidth(self.btn_remove_student.sizePolicy().hasHeightForWidth())
        self.btn_remove_student.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(12)
        self.btn_remove_student.setFont(font5)
        self.btn_remove_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_student.setStyleSheet(u"background-color: rgb(149, 125, 173);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.btn_remove_student)


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

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u09e7", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0986\u0995\u09be\u09b6 ", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u09ed \u09ac\u099b\u09b0", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0986\u09ac\u09cd\u09a6\u09c1\u09b0 \u09b0\u09ab\u09bf\u0995 ", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u09e6\u09e7\u09ed\u09ec\u09ec\u09ec\u09e7\u09e6\u09e6\u09e7\u09ea", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u09e9", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0986\u09b8\u0997\u09b0", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u" \u09ef \u09ac\u099b\u09b0 ", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u09b0\u09c7\u09b9\u09be\u09a8\u09be", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u09e6\u09e7\u09ea\u09e7\u09ea\u09e7\u09ea\u09e7\u09e8\u09eb\u09ea\u09ee ", None));
        ___qtablewidgetitem15 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u09e8", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u09b2\u09a4\u09be ", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u09ed \u09ac\u099b\u09b0 ", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u0986\u09ac\u09cd\u09a6\u09c1\u09b0 \u09b0\u09b9\u09ae\u09be\u09a8 ", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u09e6\u09e7\u09ed\u09ea\u09ee\u09eb\u09ea\u09ed\u09ee\u09ef\u09ec ", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_add_new_student.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u09af\u09c1\u0995\u09cd\u09a4 \u0995\u09b0\u09c1\u09a8", None))
        self.btn_remove_student.setText(QCoreApplication.translate("MainWindow", u"\u09b6\u09bf\u0995\u09cd\u09b7\u09be\u09b0\u09cd\u09a5\u09c0 \u098f\u09a8\u09cd\u099f\u09cd\u09b0\u09bf \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09c1\u09a8", None))
    # retranslateUi

