# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BI_ui.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(426, 511)
        font = QFont()
        font.setFamilies([u"KOTRA_BOLD"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color : rgb(255, 255, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Tab = QTabWidget(self.centralwidget)
        self.Tab.setObjectName(u"Tab")
        self.Tab.setGeometry(QRect(40, 120, 347, 341))
        font1 = QFont()
        font1.setFamilies([u"SUIT"])
        font1.setBold(True)
        self.Tab.setFont(font1)
        self.Tab.setCursor(QCursor(Qt.ArrowCursor))
        self.Tab.setMouseTracking(False)
        self.Tab.setFocusPolicy(Qt.TabFocus)
        self.Tab.setStyleSheet(u"		QTabWidget::pane {\n"
"border: 3px solid rgb(59, 108, 151);\n"
"border-bottom-left-radius : 10px;\n"
"border-bottom-right-radius : 10px;\n"
"border-top-left-radius : 5px;\n"
"border-top-right-radius : 5px;\n"
"         }\n"
"\n"
"         QTabWidget::tab-bar {\n"
"             left: 0px;\n"
"         }\n"
"\n"
"         QTabBar::tab {\n"
"             background: rgb(154, 180, 201);\n"
"color : white;\n"
"             border-top-left-radius: 5px;\n"
"             border-top-right-radius: 5px;\n"
"             min-width: 9ex;\n"
"             padding: 7px;\n"
"margin-left : 4px;\n"
"\n"
"         }\n"
"\n"
"         QTabBar::tab:selected, QTabBar::tab:hover {\n"
"             background: rgb(59, 108, 151);\n"
"			color : white;\n"
"             border-top-left-radius: 5px;\n"
"             border-top-right-radius: 5px;\n"
"         }\n"
"\n"
"         QTabBar::tab:selected {\n"
"             border-bottom-color: rgb(59, 108, 151);\n"
"         }\n"
"\n"
"         QTabBar::tab:!selected {\n"
"             marg"
                        "in-top: 4px; \n"
"         }\n"
"\n"
"\n"
"#EXCEL {\n"
"background : rgb(59, 108, 151);}\n"
"#TXT {\n"
"background : rgb(59, 108, 151);}")
        self.Tab.setUsesScrollButtons(False)
        self.Tab.setDocumentMode(False)
        self.Tab.setTabsClosable(False)
        self.Tab.setMovable(True)
        self.EXCEL = QWidget()
        self.EXCEL.setObjectName(u"EXCEL")
        self.xl_seq = QLineEdit(self.EXCEL)
        self.xl_seq.setObjectName(u"xl_seq")
        self.xl_seq.setGeometry(QRect(30, 180, 166, 41))
        font2 = QFont()
        font2.setFamilies([u"Roboto Flex"])
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.xl_seq.setFont(font2)
        self.xl_seq.setMouseTracking(True)
        self.xl_seq.setTabletTracking(False)
        self.xl_seq.setFocusPolicy(Qt.ClickFocus)
#if QT_CONFIG(tooltip)
        self.xl_seq.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.xl_seq.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.xl_seq.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.xl_seq.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.xl_seq.setAutoFillBackground(False)
        self.xl_seq.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(56, 103, 145);\n"
"border : 1px solid #FFFFFF;\n"
"color : white;\n"
"QLineEdit::PlaceholderText {\n"
"color : black; }")
        self.xl_seq.setInputMask(u"")
        self.xl_seq.setText(u"")
        self.xl_seq.setFrame(True)
        self.xl_seq.setAlignment(Qt.AlignCenter)
        self.xl_seq.setReadOnly(False)
        self.xl_seq.setPlaceholderText(u"SEQ ID")
        self.xl_seq.setClearButtonEnabled(False)
        self.done_xl = QLabel(self.EXCEL)
        self.done_xl.setObjectName(u"done_xl")
        self.done_xl.setGeometry(QRect(0, 260, 340, 31))
        font3 = QFont()
        font3.setFamilies([u"Roboto Flex"])
        self.done_xl.setFont(font3)
#if QT_CONFIG(tooltip)
        self.done_xl.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.done_xl.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.done_xl.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.done_xl.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.done_xl.setStyleSheet(u"color : rgb(169, 255, 71);\n"
"background : transparent;")
        self.done_xl.setAlignment(Qt.AlignCenter)
        self.xmlupload = QPushButton(self.EXCEL)
        self.xmlupload.setObjectName(u"xmlupload")
        self.xmlupload.setGeometry(QRect(230, 40, 81, 41))
        self.xmlupload.setFont(font1)
        self.xmlupload.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.xmlupload.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.xmlupload.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.xmlupload.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.xmlupload.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.xmlupload.setStyleSheet(u"QPushButton {\n"
"border-top-right-radius : 7px;\n"
"border-bottom-right-radius: 7px;\n"
"background : white;\n"
"color : rgb(59, 108, 151);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	color : rgb(154, 180, 201);\n"
"}")
        self.excel_upload = QPushButton(self.EXCEL)
        self.excel_upload.setObjectName(u"excel_upload")
        self.excel_upload.setGeometry(QRect(230, 110, 82, 41))
        self.excel_upload.setFont(font1)
        self.excel_upload.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.excel_upload.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.excel_upload.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.excel_upload.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.excel_upload.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.excel_upload.setStyleSheet(u"QPushButton {\n"
"border-top-right-radius : 7px;\n"
"border-bottom-right-radius: 7px;\n"
"background : white;\n"
"color : rgb(59, 108, 151);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	color : rgb(154, 180, 201);\n"
"}")
        self.xmlpath = QLineEdit(self.EXCEL)
        self.xmlpath.setObjectName(u"xmlpath")
        self.xmlpath.setGeometry(QRect(30, 40, 218, 41))
        self.xmlpath.setFont(font2)
        self.xmlpath.setMouseTracking(True)
        self.xmlpath.setTabletTracking(False)
#if QT_CONFIG(tooltip)
        self.xmlpath.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.xmlpath.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.xmlpath.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.xmlpath.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.xmlpath.setAutoFillBackground(False)
        self.xmlpath.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(59, 108, 151);\n"
"border : 1px solid #FFFFFF;\n"
"padding-left : 10px; \n"
"color : white;")
        self.xmlpath.setInputMask(u"")
        self.xmlpath.setText(u"")
        self.xmlpath.setFrame(True)
        self.xmlpath.setReadOnly(True)
        self.xmlpath.setPlaceholderText(u"fcpxml only (*.fcpxml)")
        self.xmlpath.setClearButtonEnabled(False)
        self.excelpath = QLineEdit(self.EXCEL)
        self.excelpath.setObjectName(u"excelpath")
        self.excelpath.setGeometry(QRect(30, 110, 208, 41))
        self.excelpath.setFont(font2)
        self.excelpath.setMouseTracking(True)
        self.excelpath.setTabletTracking(False)
#if QT_CONFIG(tooltip)
        self.excelpath.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.excelpath.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.excelpath.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.excelpath.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.excelpath.setAutoFillBackground(False)
        self.excelpath.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(56, 103, 145);\n"
"border : 1px solid #FFFFFF;\n"
"padding-left : 10px; \n"
"color : white;")
        self.excelpath.setInputMask(u"")
        self.excelpath.setText(u"")
        self.excelpath.setFrame(True)
        self.excelpath.setReadOnly(True)
        self.excelpath.setPlaceholderText(u"excel file only (*.xlsx)")
        self.excelpath.setClearButtonEnabled(False)
        self.start_xl = QPushButton(self.EXCEL)
        self.start_xl.setObjectName(u"start_xl")
        self.start_xl.setGeometry(QRect(210, 180, 101, 41))
        self.start_xl.setFont(font1)
        self.start_xl.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.start_xl.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.start_xl.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.start_xl.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.start_xl.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.start_xl.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(56, 103, 145);\n"
"border : 1px solid #FFFFFF;\n"
"color : white;")
        self.Tab.addTab(self.EXCEL, "")
        self.xl_seq.raise_()
        self.done_xl.raise_()
        self.xmlpath.raise_()
        self.excelpath.raise_()
        self.start_xl.raise_()
        self.xmlupload.raise_()
        self.excel_upload.raise_()
        self.TXT = QWidget()
        self.TXT.setObjectName(u"TXT")
        self.txt_seq = QLineEdit(self.TXT)
        self.txt_seq.setObjectName(u"txt_seq")
        self.txt_seq.setGeometry(QRect(30, 180, 166, 41))
        self.txt_seq.setFont(font2)
        self.txt_seq.setMouseTracking(True)
        self.txt_seq.setTabletTracking(False)
        self.txt_seq.setFocusPolicy(Qt.ClickFocus)
#if QT_CONFIG(tooltip)
        self.txt_seq.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.txt_seq.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.txt_seq.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.txt_seq.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.txt_seq.setAutoFillBackground(False)
        self.txt_seq.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(56, 103, 145);\n"
"border : 1px solid #FFFFFF;\n"
"color : white;")
        self.txt_seq.setInputMask(u"")
        self.txt_seq.setText(u"")
        self.txt_seq.setFrame(True)
        self.txt_seq.setAlignment(Qt.AlignCenter)
        self.txt_seq.setReadOnly(False)
        self.txt_seq.setPlaceholderText(u"SEQ ID")
        self.txt_seq.setClearButtonEnabled(False)
        self.edlpath_11 = QLineEdit(self.TXT)
        self.edlpath_11.setObjectName(u"edlpath_11")
        self.edlpath_11.setGeometry(QRect(30, 110, 208, 41))
        self.edlpath_11.setFont(font2)
        self.edlpath_11.setMouseTracking(True)
        self.edlpath_11.setTabletTracking(False)
#if QT_CONFIG(tooltip)
        self.edlpath_11.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.edlpath_11.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.edlpath_11.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.edlpath_11.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.edlpath_11.setAutoFillBackground(False)
        self.edlpath_11.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(56, 103, 145);\n"
"border : 1px solid #FFFFFF;\n"
"padding-left : 10px; \n"
"color : white;")
        self.edlpath_11.setInputMask(u"")
        self.edlpath_11.setText(u"")
        self.edlpath_11.setFrame(True)
        self.edlpath_11.setReadOnly(True)
        self.edlpath_11.setPlaceholderText(u"file only (*.txt)")
        self.edlpath_11.setClearButtonEnabled(False)
        self.txtupload = QPushButton(self.TXT)
        self.txtupload.setObjectName(u"txtupload")
        self.txtupload.setGeometry(QRect(230, 110, 82, 41))
        self.txtupload.setFont(font1)
        self.txtupload.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.txtupload.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.txtupload.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.txtupload.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.txtupload.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.txtupload.setStyleSheet(u"QPushButton {\n"
"border-top-right-radius : 7px;\n"
"border-bottom-right-radius: 7px;\n"
"background : white;\n"
"color : rgb(59, 108, 151);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	color : rgb(154, 180, 201);\n"
"}")
        self.xmlpath_2 = QLineEdit(self.TXT)
        self.xmlpath_2.setObjectName(u"xmlpath_2")
        self.xmlpath_2.setGeometry(QRect(30, 40, 218, 41))
        self.xmlpath_2.setFont(font2)
        self.xmlpath_2.setMouseTracking(True)
        self.xmlpath_2.setTabletTracking(False)
#if QT_CONFIG(tooltip)
        self.xmlpath_2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.xmlpath_2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.xmlpath_2.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.xmlpath_2.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.xmlpath_2.setAutoFillBackground(False)
        self.xmlpath_2.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(59, 108, 151);\n"
"border : 1px solid #FFFFFF;\n"
"padding-left : 10px; \n"
"color : white;")
        self.xmlpath_2.setInputMask(u"")
        self.xmlpath_2.setText(u"")
        self.xmlpath_2.setFrame(True)
        self.xmlpath_2.setReadOnly(True)
        self.xmlpath_2.setPlaceholderText(u"fcpxml only (*.fcpxml)")
        self.xmlpath_2.setClearButtonEnabled(False)
        self.start_txt = QPushButton(self.TXT)
        self.start_txt.setObjectName(u"start_txt")
        self.start_txt.setGeometry(QRect(210, 180, 101, 41))
        self.start_txt.setFont(font1)
        self.start_txt.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.start_txt.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.start_txt.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.start_txt.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.start_txt.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.start_txt.setStyleSheet(u"border-radius : 7px;\n"
"background : rgb(56, 103, 145);\n"
"border : 1px solid #FFFFFF;\n"
"color : white;")
        self.xmlupload_2 = QPushButton(self.TXT)
        self.xmlupload_2.setObjectName(u"xmlupload_2")
        self.xmlupload_2.setGeometry(QRect(230, 40, 81, 41))
        self.xmlupload_2.setFont(font1)
        self.xmlupload_2.setCursor(QCursor(Qt.PointingHandCursor))
#if QT_CONFIG(tooltip)
        self.xmlupload_2.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.xmlupload_2.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.xmlupload_2.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.xmlupload_2.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.xmlupload_2.setStyleSheet(u"QPushButton {\n"
"border-top-right-radius : 7px;\n"
"border-bottom-right-radius: 7px;\n"
"background : white;\n"
"color : rgb(59, 108, 151);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	color : rgb(154, 180, 201);\n"
"}")
        self.Done_txt = QLabel(self.TXT)
        self.Done_txt.setObjectName(u"Done_txt")
        self.Done_txt.setGeometry(QRect(0, 260, 340, 31))
        self.Done_txt.setFont(font3)
#if QT_CONFIG(tooltip)
        self.Done_txt.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Done_txt.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Done_txt.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.Done_txt.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.Done_txt.setStyleSheet(u"color : rgb(169, 255, 71);\n"
"background : transparent;")
        self.Done_txt.setAlignment(Qt.AlignCenter)
        self.Tab.addTab(self.TXT, "")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 30, 426, 51))
        font4 = QFont()
        font4.setFamilies([u"Roboto Flex"])
        font4.setPointSize(24)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_7.setFont(font4)
        self.label_7.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_7.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_7.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_7.setStyleSheet(u"font-weight : 900;\n"
"color : rgb(59, 108, 151);\n"
"background : transparent;")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1, 69, 424, 24))
        font5 = QFont()
        font5.setFamilies([u"Helvetica-Light"])
        font5.setPointSize(13)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_9.setFont(font5)
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
        self.label_9.setStyleSheet(u"\n"
"color : rgb(59, 108, 151);\n"
"background : transparent;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 449, 426, 53))
        self.label_18.setFont(font5)
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_18.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_18.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_18.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.label_18.setStyleSheet(u"\n"
"color : rgb(229, 229, 229);\n"
"background : transparent;")
        self.label_18.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tool Archives", None))
        self.done_xl.setText(QCoreApplication.translate("MainWindow", u"* File Name : BI_{filename}", None))
        self.xmlupload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.excel_upload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.start_xl.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Tab.setTabText(self.Tab.indexOf(self.EXCEL), QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.txtupload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.start_txt.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.xmlupload_2.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.Done_txt.setText(QCoreApplication.translate("MainWindow", u"* File Name : BI_{filename}", None))
        self.Tab.setTabText(self.Tab.indexOf(self.TXT), QCoreApplication.translate("MainWindow", u"TXT", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"BURN IN TOOL", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"NO MORE UPDATE (latest. 23/04/11)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"SEO YEON SU", None))
    # retranslateUi

