# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '230209.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 345)
        font = QFont()
        font.setFamilies([u"KOTRA_BOLD"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color :rgb(251, 243, 218)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.edlPath = QLineEdit(self.centralwidget)
        self.edlPath.setObjectName(u"edlPath")
        self.edlPath.setGeometry(QRect(60, 160, 321, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 216))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(1, 1, 1, 216))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(65, 65, 65, 63))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 63))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.edlPath.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Roboto Flex"])
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.edlPath.setFont(font1)
        self.edlPath.setMouseTracking(True)
        self.edlPath.setTabletTracking(False)
#if QT_CONFIG(tooltip)
        self.edlPath.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.edlPath.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.edlPath.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.edlPath.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.edlPath.setAutoFillBackground(False)
        self.edlPath.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(255, 255, 255);\n"
"border : 1px solid rgb(114, 96, 68);\n"
"padding-left : 10px; ")
        self.edlPath.setInputMask(u"")
        self.edlPath.setText(u"")
        self.edlPath.setFrame(True)
        self.edlPath.setDragEnabled(False)
        self.edlPath.setReadOnly(True)
        self.edlPath.setPlaceholderText(u"upload EDL file plz")
        self.edlPath.setClearButtonEnabled(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 120, 71, 51))
        font2 = QFont()
        font2.setFamilies([u"Roboto Flex"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label.setFont(font2)
#if QT_CONFIG(tooltip)
        self.label.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label.setStyleSheet(u"font-weight : 600;\n"
"color : rgb(106, 88, 60);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 40, 511, 41))
        font3 = QFont()
        font3.setFamilies([u"Roboto Flex"])
        font3.setPointSize(32)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_6.setFont(font3)
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_6.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_6.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_6.setStyleSheet(u"font-weight : 900;\n"
"color : rgb(85, 127, 107)")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 69, 511, 41))
        font4 = QFont()
        font4.setFamilies([u"Roboto Flex"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.label_8.setFont(font4)
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_8.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_8.setStyleSheet(u"color : rgb(85, 127, 107);\n"
"font-weight : 300;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.edlupload = QPushButton(self.centralwidget)
        self.edlupload.setObjectName(u"edlupload")
        self.edlupload.setGeometry(QRect(370, 160, 81, 41))
        font5 = QFont()
        font5.setBold(True)
        self.edlupload.setFont(font5)
        self.edlupload.setCursor(QCursor(Qt.PointingHandCursor))
        self.edlupload.setStyleSheet(u"QPushButton {\n"
"border-top-right-radius : 7px;\n"
"border-bottom-right-radius: 7px;\n"
"background : rgb(232, 179, 99);\n"
"border : 1.3px solid rgb(106, 88, 60);\n"
"color : rgb(106, 88, 60); \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	color : rgb(106, 88, 60);\n"
"	border :1.3px solid rgb(106, 88, 60);\n"
"	background : rgb(251, 243, 218);\n"
"}")
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(200, 270, 101, 41))
        font6 = QFont()
        font6.setFamilies([u"SUIT"])
        font6.setBold(True)
        self.start.setFont(font6)
        self.start.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.start.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.start.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.start.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.start.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.start.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"background : rgb(82, 123, 104);\n"
"color : rgb(251, 243, 218);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background : rgb(251, 243, 218);\n"
"	border : 2px solid rgb(82, 123, 104);\n"
"	color :  rgb(82, 123, 104);\n"
"}")
        self.Done = QLabel(self.centralwidget)
        self.Done.setObjectName(u"Done")
        self.Done.setGeometry(QRect(0, 240, 511, 31))
        font7 = QFont()
        font7.setFamilies([u"Roboto Flex"])
        self.Done.setFont(font7)
#if QT_CONFIG(tooltip)
        self.Done.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Done.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Done.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.Done.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.Done.setStyleSheet(u"color : green")
        self.Done.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(430, 0, 81, 21))
        self.label_9.setFont(font4)
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_9.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_9.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_9.setStyleSheet(u"color : rgb(223, 216, 195);\n"
"")
        self.label_9.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.edlPath.raise_()
        self.label_8.raise_()
        self.edlupload.raise_()
        self.Done.raise_()
        self.label_6.raise_()
        self.start.raise_()
        self.label_9.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EDL CONVERTER", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"INPUT", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"EDL CONVERTER", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TC in / out & Reel ID ONLY !!", None))
        self.edlupload.setText(QCoreApplication.translate("MainWindow", u"select", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.Done.setText(QCoreApplication.translate("MainWindow", u"DONE : 'edl2xlsx_filename.xlsx'", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SYS MADE", None))
    # retranslateUi

