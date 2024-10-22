import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        
        self.time_Lable = QLabel(self)
        self.timer =  QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100,100,500,100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_Lable)
        self.setLayout(vbox)
        self.time_Lable.setAlignment(Qt.AlignCenter)
        self.time_Lable.setStyleSheet("font-size:150px;"
                                      "color:#26ff00;")
        self.setStyleSheet("background: black;")
        
        font_id = QFontDatabase.addApplicationFont("Oxanium-VariableFont_wght.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_Lable.setFont(my_font)
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.update_time()
        
        
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_Lable.setText(current_time)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
    
