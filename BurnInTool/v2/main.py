from PySide6.QtWidgets import *
from BI_ui_ui import Ui_MainWindow
import re


class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.Tab.setCurrentIndex(0)
        self.xmlupload.clicked.connect(self.xml_upload_e)
        self.xmlupload_2.clicked.connect(self.xml_upload_t)
        self.excel_upload.clicked.connect(self.xl_upload)
        self.txtupload.clicked.connect(self.txt_upload)
        self.start_xl.clicked.connect(self.start_e)
        self.start_txt.clicked.connect(self.start_t)
        self.xl_seq.clear()
        self.txt_seq.clear()
        self.done_xl.hide()
        self.Done_txt.hide()

    def xml_upload_e(self):
        self.done_xl.hide()
        global xmlFile_e
        xmlFile_e = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; xml File(*.fcpxml)')[0]
        self.xmlpath.setText(xmlFile_e.split("/")[-1])

    def xml_upload_t(self):
        self.Done_txt.hide()
        global xmlFile_t
        xmlFile_t = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; xml File(*.fcpxml)')[0]
        self.xmlpath_2.setText(xmlFile_t.split("/")[-1])

    def xl_upload(self):
        global listFile_xl
        listFile_xl = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; text File(*.txt)')[0]
        self.excelpath.setText(listFile_xl.split("/")[-1])

    def txt_upload(self):
        global listFile_txt
        listFile_txt = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; text File(*.txt)')[0]
        self.txtpath.setText(listFile_txt.split("/")[-1])

    def start_e(self) :
        edited_lines = []
        shotName = self.xl_seq.text()
        rename_wb = load_workbook(listFile_xl, data_only=True)
        rename_ws = rename_wb.active
        new_lines = []
        for cell in rename_ws['A']:
            new_lines.append(cell.value)
        pattern = shotName + "_?\d{0,4}"
        print(len(new_lines))
        with open(xmlFile_e) as f:
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
        self.done_xl.show()

    def start_t(self):
        edited_lines = []
        shotName = self.shot_name.text()
        new_file = open(listFile_txt)
        new_lines = new_file.readlines()
        new_lines = list(map(lambda s: s.strip(), new_lines))
        pattern = shotName + "_?\d{0,4}"

        with open(xmlFile_t) as f:
            lines = f.readlines()
            i = 0
            for line in lines:
                if shotName in line and re.compile("ts\d{0,4}").search(line):
                    new_str = re.sub(pattern, new_lines[i], line)
                    edited_lines.append(new_str)
                    i += 1
                else:
                    edited_lines.append(line)

        with open(xmlFile_t, 'w') as f:
            f.writelines(edited_lines)
        self.Done_txt.show()


app = QApplication()
window = myWindow()
window.show()
app.exec()
