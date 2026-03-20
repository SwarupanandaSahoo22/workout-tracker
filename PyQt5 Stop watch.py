# # #PyQt5 Stop watch

# import sys
# from PyQt5.QtWidgets import (QApplication, QLabel, QWidget,
#                               QVBoxLayout, QHBoxLayout, QPushButton)
# from PyQt5.QtCore import QTimer, QTime, Qt

# class Stopwatch(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label = QLabel("00:00:00.00", self)
#         self.start_button = QPushButton("Start", self)
#         self.stop_button = QPushButton("Stop", self)
#         self.reset_button = QPushButton("Reset", self)
#         self.timer = QTimer(self)
#         self.initUI()
    
#     def initUI(self):
#         self.setWindowTitle("Stopwatch")

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.time_label)
#         self.setLayout(vbox)

#         self.time_label.setAlignment(Qt.AlignCenter)

#         hbox = QHBoxLayout()
#         hbox.addWidget(self.start_button)
#         hbox.addWidget(self.stop_button)
#         hbox.addWidget(self.reset_button)

#         vbox.addLayout(hbox)

#         self.setStyleSheet("""
#                 QPushButton, QLabel{
#                     padding: 20px;
#                     font-family: Calibri;
#                     font-weight: bold;
#                 }
#                 QPushButton{
#                     font-size: 40px;
#                 }
#                 QLabel{
#                     font-size: 120px;
#                     background-color: hsl(200, 100%, 85%);
#                     border-radius: 15px;
#                     padding: 
#                 }
#         """)

#         self.start_button.clicked.connect(self.start)
#         self.stop_button.clicked.connect(self.stop)
#         self.reset_button.clicked.connect(self.reset)
#         self.timer.timeout.connect(self.update_display)

#     def start(self):
#         self.timer.start(10)

#     def stop(self):
#         self.timer.stop()

#     def reset(self):
#         self.timer.stop()
#         self.time = QTime(0, 0, 0, 0) 
#         self.time_label.setText(self.format_time(self.time))

#     def format_time(self, time):
#         hours = time.hour()
#         minutes = time.minute()
#         seconds = time.second()
#         milliseconds = time.msec() // 10

#         return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

#     def update_display(self):
#         self.time = self.time.addMSecs(10)
#         self.time_label.setText(self.format_time(self.time))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     stopwatch = Stopwatch()
#     stopwatch.show()
#     sys.exit(app.exec_())



import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import QTimer, QTime, Qt

STYLESHEET = """
    QWidget {
        background-color: #0f0f0f;
        color: #ffffff;
        font-family: Consolas;
    }

    QLabel#time_label {
        font-size: 100px;
        font-weight: bold;
        color: #00e5ff;
        padding: 30px 40px;
        background-color: #1a1a1a;
        border: 2px solid #00e5ff;
        border-radius: 18px;
        letter-spacing: 4px;
    }

    QLabel#lap_header {
        font-size: 13px;
        letter-spacing: 3px;
        color: #555555;
        padding: 10px 0px 4px 0px;
    }

    QPushButton {
        font-size: 16px;
        font-family: Consolas;
        font-weight: bold;
        letter-spacing: 2px;
        padding: 14px 0px;
        border-radius: 10px;
        border: 2px solid transparent;
    }

    QPushButton#start_btn {
        background-color: #00e5ff;
        color: #0f0f0f;
    }
    QPushButton#start_btn:hover {
        background-color: #33ecff;
    }
    QPushButton#start_btn:disabled {
        background-color: #1a3a3d;
        color: #336066;
        border: 2px solid #1f4a4e;
    }

    QPushButton#stop_btn {
        background-color: #ff3d5a;
        color: #ffffff;
    }
    QPushButton#stop_btn:hover {
        background-color: #ff6070;
    }
    QPushButton#stop_btn:disabled {
        background-color: #3d1a20;
        color: #663040;
        border: 2px solid #4e1f28;
    }

    QPushButton#lap_btn {
        background-color: #1a1a1a;
        color: #00e5ff;
        border: 2px solid #00e5ff;
    }
    QPushButton#lap_btn:hover {
        background-color: #002a2e;
    }
    QPushButton#lap_btn:disabled {
        background-color: #111111;
        color: #1f4a4e;
        border: 2px solid #1f3a3d;
    }

    QPushButton#reset_btn {
        background-color: #1a1a1a;
        color: #888888;
        border: 2px solid #333333;
    }
    QPushButton#reset_btn:hover {
        background-color: #222222;
        color: #aaaaaa;
    }

    QListWidget {
        background-color: #111111;
        border: 1px solid #222222;
        border-radius: 10px;
        padding: 6px;
        font-size: 14px;
        color: #aaaaaa;
    }

    QListWidget::item {
        padding: 6px 10px;
        border-bottom: 1px solid #1e1e1e;
    }

    QListWidget::item:last-child {
        border-bottom: none;
    }
"""


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.lap_count = 0

        # Widgets
        self.time_label = QLabel("00:00:00.00")
        self.lap_header = QLabel("LAPS")
        self.lap_list = QListWidget()
        self.start_btn = QPushButton("START")
        self.stop_btn = QPushButton("STOP")
        self.lap_btn = QPushButton("LAP")
        self.reset_btn = QPushButton("RESET")

        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setStyleSheet(STYLESHEET)
        self.setMinimumWidth(500)

        # Object names for stylesheet targeting
        self.time_label.setObjectName("time_label")
        self.lap_header.setObjectName("lap_header")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn.setObjectName("stop_btn")
        self.lap_btn.setObjectName("lap_btn")
        self.reset_btn.setObjectName("reset_btn")

        # Alignment
        self.time_label.setAlignment(Qt.AlignCenter)
        self.lap_header.setAlignment(Qt.AlignCenter)

        # Cursor
        for btn in [self.start_btn, self.stop_btn, self.lap_btn, self.reset_btn]:
            btn.setCursor(Qt.PointingHandCursor)

        # Initial button states
        self.stop_btn.setEnabled(False)
        self.lap_btn.setEnabled(False)

        # Button row
        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)
        btn_row.addWidget(self.start_btn)
        btn_row.addWidget(self.stop_btn)
        btn_row.addWidget(self.lap_btn)
        btn_row.addWidget(self.reset_btn)

        # Root layout
        vbox = QVBoxLayout()
        vbox.setContentsMargins(20, 20, 20, 20)
        vbox.setSpacing(12)
        vbox.addWidget(self.time_label)
        vbox.addLayout(btn_row)
        vbox.addWidget(self.lap_header)
        vbox.addWidget(self.lap_list)
        self.setLayout(vbox)

        # Connections
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.lap_btn.clicked.connect(self.lap)
        self.reset_btn.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    # ── Stopwatch controls ──────────────────────────────────────────

    def start(self):
        self.timer.start(10)
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.lap_btn.setEnabled(True)

    def stop(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.lap_btn.setEnabled(False)

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.lap_count = 0
        self.time_label.setText(self.format_time(self.time))
        self.lap_list.clear()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.lap_btn.setEnabled(False)

    def lap(self):
        self.lap_count += 1
        lap_time = self.format_time(self.time)
        item = QListWidgetItem(f"  Lap {self.lap_count:02}     {lap_time}")
        self.lap_list.insertItem(0, item)  # newest lap at top

    # ── Time formatting ─────────────────────────────────────────────

    def format_time(self, time: QTime) -> str:
        hours        = time.hour()
        minutes      = time.minute()
        seconds      = time.second()
        centiseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{centiseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())