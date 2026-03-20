# PyQt5 Labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(r"C:\Users\Acer\OneDrive\Pictures\𝐈𝐜𝐡𝐢𝐠𝐨 𝐊𝐮𝐫𝐨𝐬𝐚𝐤𝐢 𝐈𝐜𝐨𝐧.png"))

        label = QLabel("Kurosaki Ichigo", self)
        label.setFont(QFont("Rany", 10))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #E23E3A;"
                            "background-color: #000000;"
                            "font-weight: lighter;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop) # Vertically Top
        # label.setAlignment(Qt.AlignBottom) # Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) # Vertically Center

        # label.setAlignment(Qt.AlignRight) #Horizontally Right
        # label.setAlignment(Qt.AlignLeft) #Horziontally Left
        # label.setAlignment(Qt.AlignHCenter) #Horizontally Center

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & Center
        label.setAlignment(Qt.AlignCenter) # Center & Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()