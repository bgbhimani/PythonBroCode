import sys
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Logo.png"))
        self.line_edits = QLineEdit(self)
        self.print_Button = QPushButton("Submit",self)
       
        self.lable = QLabel("your name",self)
        self.initUI()
        
    def initUI(self):
        self.line_edits.setGeometry(10,10, 300,50)
        self.line_edits.setStyleSheet("font-size: 25px;"
                                      "font-family: Arial;")
        self.line_edits.setPlaceholderText("Enter Your Name:")
        
        self.print_Button.setGeometry(320,10,100,50)
        self.print_Button.clicked.connect(self.button_click)
        self.print_Button.setStyleSheet("font-size:20px;"
                                 "font-weight: bold")
        
        self.lable.setGeometry(10,70,500,50)
        self.lable.setStyleSheet("font-size:25px;"
                                 "color:#bfbfbf;")
        
    def button_click(self):
        self.lable.setText(f"Hello, {self.line_edits.text()}")
        self.lable.setStyleSheet("font-size:25px;"
                                 "color: blue;"
                                 "font-weight: bold")
                                 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()