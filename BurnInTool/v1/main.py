from PySide6.QtWidgets import *
from ui_0926 import Ui_MainWindow
import re
import os
from openpyxl import load_workbook


class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.xml_upload.clicked.connect(self.XML_btn)
        self.li_upload.clicked.connect(self.list_btn)
        self.start.clicked.connect(self.rename)
        self.Done.hide()

    def XML_btn(self):
        self.Done.hide()
        self.xmlPath.clear()
        self.linePath.clear()
        self.shot_name.clear()
        global xmlFile
        xmlFile = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; xml File(*.fcpxml)')[0]
        self.xmlPath.setText(xmlFile.split("/")[-1])

    def list_btn(self):
        global listFile
        listFile = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; Excel File(*.xlsx)')[0]
        self.linePath.setText(listFile.split("/")[-1])

    def rename(self):
        edited_lines = []
        shotName = self.shot_name.text()
        rename_wb = load_workbook(listFile, data_only=True)
        rename_ws = rename_wb.active
        new_lines = []
        for cell in rename_ws['A']:
            new_lines.append(cell.value)
        pattern = shotName + "_?\d{0,4}"
        print(len(new_lines))
        with open(xmlFile) as f:
            lines = f.readlines()
            i = 1
            for line in lines:
                if shotName in line and re.compile("ts\d{0,4}").search(line):
                    new_str = re.sub(pattern, new_lines[i], line)
                    edited_lines.append(new_str)
                    i += 1
                else:
                    edited_lines.append(line)

        user_name = os.path.expanduser('~')
        user_name = user_name + '/Desktop/burn_in_xml.xml'

        with open(user_name, 'w') as f:
            f.writelines(edited_lines)
        self.Done.show()


app = QApplication()
window = myWindow()
window.show()
app.exec()