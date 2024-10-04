import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Logo.png"))
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        lable1 = QLabel("#1",self)
        lable2 = QLabel("#2",self)
        lable3 = QLabel("#3",self)
        lable4 = QLabel("#4",self)
        lable5 = QLabel("#5",self)
        
        lable1.setStyleSheet("background-color : red;")
        lable2.setStyleSheet("background-color : blue;")
        lable3.setStyleSheet("background-color : yellow;")
        lable4.setStyleSheet("background-color : green;")
        lable5.setStyleSheet("background-color : purple;")
        
        # vbox = QVBoxLayout()
        
        # vbox.addWidget(lable1)
        # vbox.addWidget(lable2)
        # vbox.addWidget(lable3)
        # vbox.addWidget(lable4)
        # vbox.addWidget(lable5)
        
        # central_widget.setLayout(vbox)
        
        # hbox = QHBoxLayout()
        # hbox.addWidget(lable1)
        # hbox.addWidget(lable2)
        # hbox.addWidget(lable3)
        # hbox.addWidget(lable4)
        # hbox.addWidget(lable5)
        # central_widget.setLayout(hbox)
        
        gbox = QGridLayout()
        gbox.addWidget(lable1,0,0)
        gbox.addWidget(lable2,0,1)
        gbox.addWidget(lable3,0,2)
        gbox.addWidget(lable4,1,0)
        gbox.addWidget(lable5,1,1   )
        central_widget.setLayout(gbox)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()