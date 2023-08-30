from PySide6.QtWidgets import *
from ui_log import Ui_MainWindow


class LogWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(LogWindow, self).__init__()
		self.setupUi(self)


app = QApplication()
window = LogWindow()
window.show()
app.exec()