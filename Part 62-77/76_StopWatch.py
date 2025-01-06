import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_lable = QLabel("00:00:00.00",self)
        self.start_button = QPushButton('Start',self)
        self.stop_button = QPushButton('Stop',self)
        self.reset_button = QPushButton('Reset',self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("StopWatch")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_lable)
        self.setLayout(vbox)
        
        self.time_lable.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
                           QPushButton,QLabel{
                               padding:20px;
                               font-weight:bold;
                               font-family:Calibri
                           }
                           QPushButton{
                               font-size:50px;
                               background-color:aqua;
                           }
                           QLabel{
                               border-radius:20px;
                               font-size:120px;
                               background-color:skyblue;
                           }
                           """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_displat)
        
    
    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_lable.setText(self.formate_time(self.time))
    
    def formate_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        secondss = time.second()
        milisecond = time.msec() //10
        return f"{hours:02}:{minutes:02}:{secondss:02}.{milisecond:02}"
        
    
    def update_displat(self):
        self.time = self.time.addMSecs(10)
        self.time_lable.setText(self.formate_time(self.time))
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())