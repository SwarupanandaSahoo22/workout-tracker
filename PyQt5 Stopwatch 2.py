#PyQt5 Stopwatch 2

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                              QHBoxLayout, QListWidget, QPushButton, QListWidgetItem)
from PyQt5.QtCore import QTime, QTimer, Qt

STYLESHEET = """
    QWidget {
        background-color: #0f0f0f;
        color: #ffffff;
        font-family: Calibri;
    }

    QLabel#time_label {
        font-size: 100px;
        font-weight: bold;
        color: #ff6b35;
        padding: 30px 40px;
        background-color: #1a1a1a;
        border: 2px solid #ff6b35;
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
        font-family: Calibri;
        font-weight: bold;
        padding: 14px 0px;
        letter-spacing: 2px;
        border: 2px solid transparent;
        border-radius: 10px;
    }

    QPushButton#start_btn {
        background-color: #ff6b35;
        color: #0f0f0f;
    }
    QPushButton#start_btn:hover {
        background-color: #ff8c5a;
    }
    QPushButton#start_btn:disabled {
        background-color: #3d2010;
        color: #6b3a20;
        border: 2px solid #4e2a15;
    }

    QPushButton#stop_btn {
        background-color: #cc2200;
        color: #ffffff;
    }
    QPushButton#stop_btn:hover {
        background-color: #e63300;
    }
    QPushButton#stop_btn:disabled {
        background-color: #2a0a00;
        color: #5a2010;
        border: 2px solid #3d1500;
    }

    QPushButton#lap_btn {
        background-color: #1a1a1a;
        color: #ff9f1c;
        border: 2px solid #ff9f1c;
    }
    QPushButton#lap_btn:hover {
        background-color: #2a1f00;
    }
    QPushButton#lap_btn:disabled {
        background-color: #111111;
        color: #3d2e00;
        border: 2px solid #2a2000;
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
        color: #aaaaaa;
        border: 1px solid #222222;
        border-radius: 10px;
        padding: 6px;
        font-size: 14px;
    }

    QListWidget::item {
        padding: 6px 10px;
        border-bottom: 1px solid #1e1e1e;
    }

    QListWidget::item:last-child {
        border-bottom: none;
    }
"""

class StopWatch(QWidget):
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
        self.setWindowTitle("StopWatch")
        self.setStyleSheet(STYLESHEET)
        self.setMinimumWidth(500)

        # Object name for stylesheet targeting
        self.time_label.setObjectName("time_label")
        self.lap_header.setObjectName("lap_header")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn.setObjectName("stop_btn")
        self.lap_btn.setObjectName("lap_btn")
        self.reset_btn.setObjectName("reset_btn")

        # Alignment
        self.time_label.setAlignment(Qt.AlignCenter)
        self.lap_header.setAlignment(Qt.AlignCenter)

        #Cursor
        for btn in [self.start_btn, self.stop_btn, self.lap_btn, self.reset_btn]:
            btn.setCursor(Qt.PointingHandCursor)

        #Intial Button stage
        self.stop_btn.setEnabled(False)
        self.lap_btn.setEnabled(False)

        # Button Row
        btn_row = QHBoxLayout()
        btn_row.setSpacing(10)
        btn_row.addWidget(self.start_btn)
        btn_row.addWidget(self.stop_btn)
        btn_row.addWidget(self.lap_btn)
        btn_row.addWidget(self.reset_btn)
        
        # Root Layout
        vbox = QVBoxLayout()
        vbox.setSpacing(12)
        vbox.setContentsMargins(20, 20, 20, 20)
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
        self.timer.timeout.connect(self.update_time)

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

    def lap(self):
        self.lap_count += 1
        lap_time = self.format_time(self.time)
        items = QListWidgetItem(f"Laps {self.lap_count:02} {lap_time}")
        self.lap_list.insertItem(0, items) # new lap at top

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.lap_count = 0
        self.time_label.setText(self.format_time(self.time))
        self.lap_list.clear()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.lap_btn.setEnabled(False)

    def format_time(self, time:QTime) -> str:
        hours        =      time.hour()
        minutes      =      time.minute()
        seconds      =      time.second()
        milliseconds =      time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())