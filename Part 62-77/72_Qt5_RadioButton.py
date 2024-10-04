import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Logo.png"))
        self.radio1 = QRadioButton("VISA",self)
        self.radio2 = QRadioButton("Master Card",self)
        self.radio4 = QRadioButton("Gift Card",self)
        
        self.radio5 = QRadioButton("In Store",self)
        self.radio6 = QRadioButton("Online",self)
        
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        
        self.initUI()
        
        
    def initUI(self):
        self.radio1.setGeometry(10,0,300,50)
        self.radio2.setGeometry(10,50,300,50)
        self.radio4.setGeometry(10,100,300,50)
        self.radio5.setGeometry(10,200,300,50)
        self.radio6.setGeometry(10,250,300,50)
        
        self.setStyleSheet("QRadioButton{"
                                      "font-size: 25px;"
                                      "font-family: Arial;"
                                      "font-weight: bold;"
                                      "}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        self.button_group2.addButton(self.radio6)
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        self.radio6.toggled.connect(self.radio_button_changed)
        
    def radio_button_changed(self):
        # print("You Have selected Something!!!")
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected!")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()