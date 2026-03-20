#PyQt5 Stylesheet

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.button1 = QPushButton("#1")
#         self.button2 = QPushButton("#2")
#         self.button3 = QPushButton("#3")
#         self.initUI()
    
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         hbox = QHBoxLayout()

#         hbox.addWidget(self.button1)
#         hbox.addWidget(self.button2)
#         hbox.addWidget(self.button3)

#         central_widget.setLayout(hbox)
        
#         self.button1.setObjectName("button1")
#         self.button2.setObjectName("button2")
#         self.button3.setObjectName("button3")

#         self.setStyleSheet("""
#                 QPushButton{
#                         font-size: 20px;
#                         font-family: Rany;
#                         padding: 15px 75px;
#                         margin: 25px;
#                         border: 3px solid;
#                         border-radius: 15px;
#             }   
#                            QPushButton#button1{
#                                     background-color: hsl(0, 100%, 54%)
#                            }
#                            QPushButton#button2{
#                                     background-color: hsl(240, 100%, 54%)
#                            }
#                            QPushButton#button3{
#                                     background-color: hsl(120, 100%, 54%)
#                            }

#                            QPushButton#button1:hover{
#                                     background-color: hsl(0, 100%, 74%)
#                            }
#                            QPushButton#button2:hover{
#                                     background-color: hsl(240, 100%, 74%)
#                            }
#                            QPushButton#button3:hover{
#                                     background-color: hsl(120, 100%, 74%)
#                            }

                            
#         """)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())




import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QWidget, QHBoxLayout, QLabel, QVBoxLayout
)
from PyQt5.QtCore import Qt


BUTTONS_CONFIG = [
    {"label": "Red",   "hue": 0,   "name": "button1"},
    {"label": "Blue",  "hue": 240, "name": "button2"},
    {"label": "Green", "hue": 120, "name": "button3"},
]

STYLESHEET = """
    QMainWindow {
        background-color: #1a1a2e;
    }

    QWidget#central {
        background-color: #1a1a2e;
    }

    QLabel#title {
        color: #ffffff;
        font-size: 22px;
        font-family: Segoe UI;
        font-weight: bold;
        padding: 10px;
    }

    QLabel#status {
        color: #aaaaaa;
        font-size: 14px;
        font-family: Segoe UI;
        padding: 5px;
    }

    QPushButton {
        font-size: 18px;
        font-family: Segoe UI;
        font-weight: 600;
        padding: 15px 60px;
        margin: 20px 15px;
        border: 3px solid rgba(255,255,255,0.2);
        border-radius: 15px;
        color: white;
    }

    QPushButton:hover {
        border: 3px solid rgba(255,255,255,0.6);
    }

    QPushButton:pressed {
        border: 3px solid white;
        padding: 17px 58px 13px 62px;
    }

    QPushButton#button1 { background-color: hsl(0, 85%, 50%); }
    QPushButton#button2 { background-color: hsl(240, 85%, 55%); }
    QPushButton#button3 { background-color: hsl(120, 60%, 38%); }

    QPushButton#button1:hover { background-color: hsl(0, 85%, 65%); }
    QPushButton#button2:hover { background-color: hsl(240, 85%, 70%); }
    QPushButton#button3:hover { background-color: hsl(120, 60%, 52%); }

    QPushButton#button1:pressed { background-color: hsl(0, 85%, 40%); }
    QPushButton#button2:pressed { background-color: hsl(240, 85%, 44%); }
    QPushButton#button3:pressed { background-color: hsl(120, 60%, 28%); }
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Buttons")
        self.setFixedSize(700, 220)
        self.setStyleSheet(STYLESHEET)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        central_widget.setObjectName("central")
        self.setCentralWidget(central_widget)

        root_layout = QVBoxLayout()
        root_layout.setAlignment(Qt.AlignCenter)

        # Title
        title = QLabel("Choose a Color")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        # Status label
        self.status_label = QLabel("No button pressed yet")
        self.status_label.setObjectName("status")
        self.status_label.setAlignment(Qt.AlignCenter)

        # Buttons row
        btn_row = QHBoxLayout()
        btn_row.setAlignment(Qt.AlignCenter)

        for config in BUTTONS_CONFIG:
            btn = QPushButton(config["label"])
            btn.setObjectName(config["name"])
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(
                lambda checked, label=config["label"], hue=config["hue"]:
                    self.on_button_click(label, hue)
            )
            btn_row.addWidget(btn)

        root_layout.addWidget(title)
        root_layout.addLayout(btn_row)
        root_layout.addWidget(self.status_label)

        central_widget.setLayout(root_layout)

    def on_button_click(self, label: str, hue: int):
        self.status_label.setText(f"You picked: {label}  |  HSL hue: {hue}°")
        self.status_label.setStyleSheet(
            f"color: hsl({hue}, 80%, 75%); font-size: 14px; font-family: Segoe UI; padding: 5px;"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())