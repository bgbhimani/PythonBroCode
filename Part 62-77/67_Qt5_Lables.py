import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Logo.png"))
        
        lable = QLabel("Hello",self)
        lable.setFont(QFont("Arial Bold",25))
        lable.setGeometry(0,0,500,100)
        lable.setStyleSheet("color:blue;"
                            "background-color : #fa6525;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")
        # lable.setAlignment(Qt.AlignTop)      # Vertically TOP
        # lable.setAlignment(Qt.AlignBottom)   # Vertically Bottom
        # lable.setAlignment(Qt.AlignVCenter)  # Vertically Center
        
        # lable.setAlignment(Qt.AlignLeft)  # Horizontally Left
        # lable.setAlignment(Qt.AlignHCenter)  # Horizontally Center
        # lable.setAlignment(Qt.AlignRight)  # Horizontally Right
        
        # lable.setAlignment(Qt.AlignCenter | Qt.AlignTop) # Center & Top
        lable.setAlignment(Qt.AlignCenter) # center & center
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()