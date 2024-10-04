import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First cool GUI")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Logo.png"))
        
        lable = QLabel(self)
        lable.setGeometry(0,0,250,250 )
        pixmap = QPixmap("Background.jpg")
        lable.setPixmap(pixmap)
        lable.setScaledContents(True)
        
        lable.setGeometry((self.width()- lable.width())//2 ,  #//2 floor division gives the int ans
                          (self.height()-lable.height())//2,
                          lable.width(),lable.height())
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()