import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Logo.png"))
        self.button = QPushButton("Click Me!!",self)
        self.label = QLabel("Hello",self)
        self.initUI()
        
    def initUI(self):
        self.button.setGeometry(150,200,200,100)  
        self.button.setStyleSheet("font-size: 35px;"
                             "color: red;"
                             "backgronud-color:white;"
                             "font-weight: bold")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(150,300,400,100)
        self.label.setStyleSheet("font-size: 40px;")
        
    def on_click(self):
        # print("Button Clicked")
        # self.button.setText("Clicked!!")
        # self.button.setStyleSheet("font-size: 35px;"
        #                      "color: Blue;"
        #                      "backgronud-color:white;"
        #                      "font-weight: bold")
        # self.button.setDisabled(True)
        self.label.setText("👋🏻 Good Bye")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())