from PySide6.QtWidgets import *
from ui_1014 import Ui_MainWindow
import os

framerate = 24

def timecode_to_frames(timecode):
    return sum(f * int(t) for f,t in zip((3600*framerate, 60*framerate, framerate, 1), timecode.split(':')))

def frames_to_TC(frames):
    h = int(frames / 86400)
    m = int(frames / 1440) % 60
    s = int((frames % 1440)/24)
    f = frames % 1440 % 24
    return ("%02d:%02d:%02d:%02d" % (h, m, s, f))

def listToString(str_list):
    result = ""
    for s in str_list:
            result += s + " "
    return result.strip()

class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.upload.clicked.connect(self.upload_edl)
        self.start.clicked.connect(self.generate_edl)
        self.Done.hide()

    def upload_edl(self):
        self.Done.hide()
        self.linePath.clear()
        self.edlpath.clear()
        global edlFile
        edlFile = QFileDialog.getOpenFileName(self, self.tr('Open File'), '/', 'All File(*);; edl File(*.edl)')[0]
        self.edlpath.setText(edlFile.split("/")[-1])

    def generate_edl(self) :


        f = open(edlFile)

        lines = f.read().splitlines()

        user_name = os.path.expanduser('~')
        user_name = user_name + '/Desktop/razor_output.edl'

        new_edl = open(user_name, 'w')

        for line in lines :

            
            line = line.split()
            if self.linePath.text() == "":
                if len(line) == 8 :
                    line[4] = line[6]
                    line[5] = line[7]

                if 'V' in line and 'C' in line  :
                    new_edl.write(listToString(line)+'\n\n')
            else :
                if len(line) == 8 :
                    line[4] = frames_to_TC(timecode_to_frames(self.linePath.text()) + timecode_to_frames(line[6]))
                    line[5] = frames_to_TC(timecode_to_frames(self.linePath.text()) + timecode_to_frames(line[7]))
                    line[6] = line[4]
                    line[7] = line[5]
                    if line[4] == self.linePath.text() :
                        line[4]='00:00:00:00'
                        line[6]='00:00:00:00'        
               
                if 'V' in line and 'C' in line :
                    new_edl.write(listToString(line)+'\n')

    
        new_edl.close()
        self.Done.show()

    

app = QApplication()
window = myWindow()
window.show()
app.exec()
