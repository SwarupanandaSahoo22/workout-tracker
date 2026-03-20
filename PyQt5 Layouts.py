# PyQt5 Layouts

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
    
    def initUI(self):
        cental_widget = QWidget()
        self.setCentralWidget(cental_widget)

        label1 = QLabel("Rukia")
        label2 = QLabel("Ichigo")
        label3 = QLabel("Orihime")
        label4 = QLabel("Ishida")
        label5 = QLabel("Chad")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: orange;")
        label3.setStyleSheet("background-color: pink;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: brown;")

        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)

        cental_widget.setLayout(grid)
  

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()