import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First cool GUI")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Logo.png"))
        self.checkbox = QCheckBox("Do you like Food??",self)
        
        self.initUI()
        
    def initUI(self):
        self.checkbox.setGeometry(10,10,400,100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                 "font-family: Arial;")
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.checkbox_changes)   

    def checkbox_changes(self,state):
        # if state == 2:  # 2 for checked
        if state == Qt.Checked:
            print("You like the food!!")
        elif state == 0: # for not checked
            print("You Don't Like food!!")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())