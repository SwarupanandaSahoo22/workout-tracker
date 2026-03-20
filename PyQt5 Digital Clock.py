#PyQt5 Digital Clock

# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
# from PyQt5.QtCore import QTimer, QTime, Qt
# from PyQt5.QtGui import QFont, QFontDatabase

# class DigitalClock(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time_label = QLabel(self)
#         self.timer = QTimer(self)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Digital Clock")
#         self.setGeometry(600, 400, 300, 100)

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.setLayout(vbox)

#         self.time_label.setAlignment(Qt.AlignCenter)
#         self.time_label.setStyleSheet(
#                                       "font-size: 150px;"
#                                       "color: hsl(111, 100%, 50%)"
#                                 )
        
#         self.setStyleSheet("background-color: black")

#         font_id = QFontDatabase.addApplicationFont(r"C:\Users\Acer\Downloads\ds_digital\DS-DIGIT.TTF")
#         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#         my_font = QFont(font_family, 150)
#         self.time_label.setFont(my_font)

#         self.timer.timeout.connect(self.update_time)
#         self.timer.start(1000)

#         self.update_time()

#     def update_time(self):
#         current_time = QTime.currentTime().toString("hh:mm:ss AP")
#         self.time_label.setText(current_time)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     clock = DigitalClock()
#     clock.show()
#     sys.exit(app.exec_())


import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "fonts", "DS-DIGIT.TTF")
FALLBACK_FONT = "Courier New"

STYLESHEET = """
    QWidget {
        background-color: #0a0a0a;
    }
    QLabel#time_label {
        color: hsl(111, 100%, 50%);
        padding: 20px 40px;
    }
    QLabel#date_label {
        color: hsl(111, 60%, 35%);
        font-size: 18px;
        font-family: Courier New;
        letter-spacing: 4px;
        padding-bottom: 15px;
    }
"""


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel()
        self.date_label = QLabel()
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setStyleSheet(STYLESHEET)

        # Load font safely with fallback
        font_family = self._load_font(FONT_PATH, FALLBACK_FONT)
        clock_font = QFont(font_family, 120)

        # Time label
        self.time_label.setObjectName("time_label")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(clock_font)

        # Date label
        self.date_label.setObjectName("date_label")
        self.date_label.setAlignment(Qt.AlignCenter)

        # Layout
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.date_label)
        self.setLayout(vbox)

        # Timer
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

        self.adjustSize()

    def _load_font(self, path: str, fallback: str) -> str:
        """Load a custom font from path, return fallback family if it fails."""
        if not os.path.exists(path):
            print(f"[Warning] Font not found at: {path}. Using fallback: {fallback}")
            return fallback

        font_id = QFontDatabase.addApplicationFont(path)
        families = QFontDatabase.applicationFontFamilies(font_id)

        if not families:
            print(f"[Warning] Failed to load font from: {path}. Using fallback: {fallback}")
            return fallback

        return families[0]

    def update_time(self):
        time_str = QTime.currentTime().toString("hh:mm:ss AP")
        from PyQt5.QtCore import QDate
        date_str = QDate.currentDate().toString("dddd, MMMM d yyyy").upper()

        self.time_label.setText(time_str)
        self.date_label.setText(date_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())