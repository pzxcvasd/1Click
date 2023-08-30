# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wswg_Edl_toolwOvBvx.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 291)
        font = QFont()
        font.setFamilies([u"KOTRA_BOLD"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color :rgb(32, 33, 32)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(150, 220, 101, 41))
        font1 = QFont()
        font1.setFamilies([u"Helvetica63-ExtendedMedium"])
        font1.setBold(True)
        self.start.setFont(font1)
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
        self.start.setStyleSheet(u"QPushButton {border-radius: 7px;\n"
"background : rgb(32, 33, 32);\n"
"border: 1px solid rgb(96, 96, 96);\n"
"color : gray; }\n"
"\n"
"QPushButton::hover {\n"
"   	background : rgb(32, 33, 32);\n"
"	border : 1px solid rgb(255, 107, 86);\n"
"color : rgb(255, 107, 86);\n"
"}")
        self.org_btn = QPushButton(self.centralwidget)
        self.org_btn.setObjectName(u"org_btn")
        self.org_btn.setGeometry(QRect(50, 130, 81, 41))
        self.org_btn.setFont(font1)
        self.org_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.org_btn.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.org_btn.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.org_btn.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.org_btn.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.org_btn.setStyleSheet(u"QPushButton {\n"
"\n"
"background : rgb(117, 117, 117);\n"
"color : rgb(32, 33, 32);\n"
"border-radius : 7px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background : rgb(150, 150, 150);\n"
"\n"
"}")
        self.SYSMADE = QLabel(self.centralwidget)
        self.SYSMADE.setObjectName(u"SYSMADE")
        self.SYSMADE.setGeometry(QRect(0, 0, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"HelveticaNeue MediumExt"])
        self.SYSMADE.setFont(font2)
#if QT_CONFIG(tooltip)
        self.SYSMADE.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.SYSMADE.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.SYSMADE.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.SYSMADE.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.SYSMADE.setStyleSheet(u"color : rgb(54, 55, 54)")
        self.SYSMADE.setAlignment(Qt.AlignCenter)
        self.new_btn = QPushButton(self.centralwidget)
        self.new_btn.setObjectName(u"new_btn")
        self.new_btn.setGeometry(QRect(270, 130, 81, 41))
        self.new_btn.setFont(font1)
        self.new_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.new_btn.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.new_btn.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.new_btn.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.new_btn.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.new_btn.setStyleSheet(u"QPushButton {\n"
"\n"
"background : rgb(117, 117, 117);\n"
"color : rgb(32, 33, 32);\n"
"border-radius : 7px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background : rgb(150, 150, 150);\n"
"\n"
"}")
        self.excel_btn = QPushButton(self.centralwidget)
        self.excel_btn.setObjectName(u"excel_btn")
        self.excel_btn.setGeometry(QRect(160, 60, 81, 41))
        self.excel_btn.setFont(font1)
        self.excel_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.excel_btn.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.excel_btn.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.excel_btn.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.excel_btn.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.excel_btn.setStyleSheet(u"QPushButton {\n"
"\n"
"background : rgb(117, 117, 117);\n"
"color : rgb(32, 33, 32);\n"
"border-radius : 7px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background : rgb(150, 150, 150);\n"
"\n"
"}")
        self.D = QLabel(self.centralwidget)
        self.D.setObjectName(u"D")
        self.D.setGeometry(QRect(10, 210, 381, 51))
        font3 = QFont()
        font3.setFamilies([u"UNDERRATED"])
        font3.setPointSize(54)
        self.D.setFont(font3)
#if QT_CONFIG(tooltip)
        self.D.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.D.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.D.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.D.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.D.setStyleSheet(u"color : rgba(78, 78, 78, 160)")
        self.D.setAlignment(Qt.AlignCenter)
        self.A = QLabel(self.centralwidget)
        self.A.setObjectName(u"A")
        self.A.setGeometry(QRect(10, 150, 381, 51))
        self.A.setFont(font3)
#if QT_CONFIG(tooltip)
        self.A.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.A.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.A.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.A.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.A.setStyleSheet(u"color : rgba(78, 78, 78, 160)")
        self.A.setAlignment(Qt.AlignCenter)
        self.B = QLabel(self.centralwidget)
        self.B.setObjectName(u"B")
        self.B.setGeometry(QRect(10, 90, 381, 51))
        self.B.setFont(font3)
#if QT_CONFIG(tooltip)
        self.B.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.B.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.B.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.B.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.B.setStyleSheet(u"color : rgba(78, 78, 78, 160)")
        self.B.setAlignment(Qt.AlignCenter)
        self.C = QLabel(self.centralwidget)
        self.C.setObjectName(u"C")
        self.C.setGeometry(QRect(10, 30, 381, 51))
        self.C.setFont(font3)
#if QT_CONFIG(tooltip)
        self.C.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.C.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.C.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.C.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.C.setStyleSheet(u"color : rgba(78, 78, 78, 160)")
        self.C.setAlignment(Qt.AlignCenter)
        self.excel_text = QLabel(self.centralwidget)
        self.excel_text.setObjectName(u"excel_text")
        self.excel_text.setGeometry(QRect(150, 40, 101, 21))
        font4 = QFont()
        font4.setFamilies([u"Helvetica"])
        font4.setPointSize(11)
        self.excel_text.setFont(font4)
#if QT_CONFIG(tooltip)
        self.excel_text.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.excel_text.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.excel_text.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.excel_text.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.excel_text.setStyleSheet(u"color : rgb(181, 201, 255);\n"
"background: transparent;")
        self.excel_text.setAlignment(Qt.AlignCenter)
        self.new_text = QLabel(self.centralwidget)
        self.new_text.setObjectName(u"new_text")
        self.new_text.setGeometry(QRect(260, 170, 101, 21))
        self.new_text.setFont(font4)
#if QT_CONFIG(tooltip)
        self.new_text.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.new_text.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.new_text.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.new_text.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.new_text.setStyleSheet(u"color : rgb(181, 201, 255);\n"
"background: transparent;")
        self.new_text.setAlignment(Qt.AlignCenter)
        self.org_text = QLabel(self.centralwidget)
        self.org_text.setObjectName(u"org_text")
        self.org_text.setGeometry(QRect(40, 170, 101, 21))
        self.org_text.setFont(font4)
#if QT_CONFIG(tooltip)
        self.org_text.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.org_text.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.org_text.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.org_text.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.org_text.setStyleSheet(u"color : rgb(181, 201, 255);\n"
"background: transparent;")
        self.org_text.setAlignment(Qt.AlignCenter)
        self.Done_btn = QPushButton(self.centralwidget)
        self.Done_btn.setObjectName(u"Done_btn")
        self.Done_btn.setGeometry(QRect(150, 130, 101, 41))
        font5 = QFont()
        font5.setFamilies([u"Helvetica83-ExtendedHeavy"])
        font5.setPointSize(25)
        font5.setBold(True)
        self.Done_btn.setFont(font5)
        self.Done_btn.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.Done_btn.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Done_btn.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Done_btn.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.Done_btn.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.Done_btn.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"color : rgb(203, 255, 173);\n"
"background : transparent;\n"
" }\n"
"\n"
"QPushButton::hover {\n"
"color : rgb(255, 107, 86);\n"
"background : transparent;\n"
"}")
        self.Done_text = QLabel(self.centralwidget)
        self.Done_text.setObjectName(u"Done_text")
        self.Done_text.setGeometry(QRect(150, 160, 101, 21))
        font6 = QFont()
        font6.setFamilies([u"Helvetica"])
        font6.setPointSize(12)
        self.Done_text.setFont(font6)
#if QT_CONFIG(tooltip)
        self.Done_text.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Done_text.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Done_text.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.Done_text.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.Done_text.setStyleSheet(u"color : rgb(203, 255, 173);\n"
"background : transparent;")
        self.Done_text.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.A.raise_()
        self.D.raise_()
        self.C.raise_()
        self.B.raise_()
        self.start.raise_()
        self.org_btn.raise_()
        self.SYSMADE.raise_()
        self.new_btn.raise_()
        self.excel_btn.raise_()
        self.excel_text.raise_()
        self.new_text.raise_()
        self.org_text.raise_()
        self.Done_btn.raise_()
        self.Done_text.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DELIVERY", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.org_btn.setText(QCoreApplication.translate("MainWindow", u"ORG", None))
        self.SYSMADE.setText(QCoreApplication.translate("MainWindow", u"SYS MADE", None))
        self.new_btn.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.excel_btn.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.D.setText(QCoreApplication.translate("MainWindow", u"DELIVERY", None))
        self.A.setText(QCoreApplication.translate("MainWindow", u"DELIVERY", None))
        self.B.setText(QCoreApplication.translate("MainWindow", u"DELIVERY", None))
        self.C.setText(QCoreApplication.translate("MainWindow", u"DELIVERY", None))
        self.excel_text.setText(QCoreApplication.translate("MainWindow", u"SYS MADE", None))
        self.new_text.setText(QCoreApplication.translate("MainWindow", u"SYS MADE", None))
        self.org_text.setText(QCoreApplication.translate("MainWindow", u"SYS MADE", None))
        self.Done_btn.setText(QCoreApplication.translate("MainWindow", u"FIN", None))
        self.Done_text.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub9ad\ud574\uc11c \ub85c\uadf8\ubcf4\uae30", None))
    # retranslateUi

