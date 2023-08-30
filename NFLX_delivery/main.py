from PySide6.QtWidgets import *
from ui_delivery import Ui_MainWindow
import os
import subprocess
import pandas as pd
from ui_log import Ui_mainWindow


class myWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(myWindow, self).__init__()
		self.setupUi(self)
		self.excel_btn.clicked.connect(self.upload_xl)
		self.org_btn.clicked.connect(self.upload_org)
		self.new_btn.clicked.connect(self.upload_new)
		self.start.clicked.connect(self.start_move)
		self.excel_text.hide()
		self.new_text.hide()
		self.org_text.hide()
		self.Done_btn.hide()
		self.Done_text.hide()
		self.Done_btn.clicked.connect(self.open_log)
		self.log_text = ""

	def upload_xl(self) :
		self.Done_btn.hide()
		self.Done_text.hide()
		global xl_list
		xl_list = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; xlsx File(*.xlsx)')[0]
		print(xl_list)
		self.excel_text.setText(xl_list.split("/")[-1])
		self.excel_text.show()

	def upload_org(self) :
		self.Done_btn.hide()
		self.Done_text.hide()
		global source_path
		source_path = QFileDialog.getExistingDirectory(self, self.tr("Open Data files"), "/", QFileDialog.ShowDirsOnly)
		self.org_text.setText(source_path.split("/")[-1])
		self.org_text.show()

	def upload_new(self) :
		self.Done_btn.hide()
		self.Done_text.hide()
		global deliver_path
		deliver_path = QFileDialog.getExistingDirectory(self, self.tr("Open Data files"), "/", QFileDialog.ShowDirsOnly)
		self.new_text.setText(deliver_path.split("/")[-1])
		self.new_text.show()

	def start_move(self) :
		self.Done_btn.hide()
		self.Done_text.hide()
		df = pd.read_excel(xl_list, usecols=[0,10,11])

		for column_name, item in df.iterrows() :
			folder_name = str(df.loc[column_name].values[0]) #A열 : 에피소드 (test1)
			origin_folder = str(df.loc[column_name].values[1]) #K열 : 파일이름
			sub_folder = str(df.loc[column_name].values[2]) #J열 : 서브폴더 이름

			if sub_folder == "MOV" :
				origin_folder = origin_folder + '.mov'

			new_source_path= os.path.join(source_path,sub_folder,origin_folder)
			sub_destination_path = os.path.join(deliver_path, folder_name, sub_folder)
			destination_path = os.path.join(deliver_path, folder_name, sub_folder, origin_folder)
			global log_text
			if os.path.exists(new_source_path):

				if not os.path.exists(sub_destination_path):
					os.makedirs(sub_destination_path)

				subprocess.run(["mv", new_source_path, destination_path])
				self.log_text += (f"[SUCCESS] : {origin_folder}\n")
				# SW = LogWindow(log_text)

			else :
				self.log_text += (f"[FAILED] : {origin_folder}\n")
				# SW = LogWindow(log_text)

		self.Done_btn.show()
		self.Done_text.show()

	def open_log(self) :
		self.log_window = LogWindow(self.log_text)
		self.excel_text.hide()
		self.new_text.hide()
		self.org_text.hide()
		self.log_window.show()

class LogWindow(QMainWindow,Ui_mainWindow):
	def __init__(self,log_text):
		super(LogWindow, self).__init__()
		self.setupUi(self)
		self.close.clicked.connect(self.close_window)
		self.textBrowser.append(log_text)

	def close_window(self) :
		self.hide()


app = QApplication()
window = myWindow()
window.show()
app.exec()