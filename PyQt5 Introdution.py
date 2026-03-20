#PyQt5 Introdution

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(r"C:\Users\Acer\OneDrive\Pictures\𝐈𝐜𝐡𝐢𝐠𝐨 𝐊𝐮𝐫𝐨𝐬𝐚𝐤𝐢 𝐈𝐜𝐨𝐧.png"))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()