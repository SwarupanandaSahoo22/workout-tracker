# Pomodoro Timer

import sys, json, os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QPushButton, QHBoxLayout, 
    QStackedWidget, QSpinBox, QTableWidget,
    QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import QTimer, Qt, QDate

DATA_FILE = "sessions.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return[]

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

STYLESHEET = """
    QWidget {
        background-color: #1a1a1a;
        font-family: Calibri;
        color: #ffffff;    
    }
    QWidget#topbar {
        background-color: #111111;
        border-bottom: 1px solid #2a2a2a;
    }
    QWidget#sidebar {
        background-color: #111111;
        border-right: 1px solid #2a2a2a;
    }
    QWidget#card {
        background-color: #222222;
        border-radius: 12px;
    }
    QPushButton#nav_btn {
        color: #888888;
        font-family: Calibri;
        font-weight: bold;
        font-size: 15px;
        padding: 15px 25px;
        background-color: transparent;
        border: none;
        text-align: left;
    }
    QPushButton#nav_btn:hover {
        color: #ff6b35;
        background-color: #2a2a2a;
    }
    QPushButton#nav_btn_active {
        color: #ff6b35;
        background-color: #2a2a2a;
        font-family: Calibri;
        font-weight: bold;
        font-size: 15px;
        padding: 15px 22px;
        border: none;
        text-align: left;
        border-left: 3px solid #ff6b35;
    }
    QPushButton#primary_btn {
        color: #ffffff;
        background-color: #ff6b35;
        font-family: Calibri;
        font-weight: bold;
        font-size: 15px;
        padding: 12px 35px;
        border: none;
        border-radius: 10px;
    }
    QPushButton#primary_btn:hover {
        background-color: #ff8c5a;
    }
    QPushButton#secondary_btn {
        color: #888888;
        background-color: #2a2a2a;
        font-family: Calibri;
        font-weight: bold;
        font-size: 15px;
        padding: 12px 35px;
        border: none;
        border-radius: 10px;
    }
    QPushButton#secondary_btn:hover {
        color: #ffffff;
        background-color: #333333;
    }
    QSpinBox {
        color: #ffffff;
        background-color: #2a2a2a;
        font-family: Calibri;
        font-size: 15px;
        padding: 8px 12px;
        border: 1px solid #333333;
        border-radius: 8px;
    }
    QTableWidget {
        color: #cccccc;
        background-color: #2a2a2a;
        font-family: Calibri;
        font-size: 14px;
        gridline-color: #2a2a2a;
        border: none;
    }
    QTableWidget::item {
        padding: 8px;
    }
    QTableWidget::item:selected {
        background-color: #2a2a2a;
        color: #ffffff;
    }
    QHeaderView::section {
        color: #888888;
        background-color: #1a1a1a;
        font-family: Calibri;
        font-size: 13px;
        font-weight: bold;
        border: none;
        border-bottom: 1px solid #2a2a2a;
    }
"""


class Focus(QWidget):
    def __init__(self):
        super().__init__()
        self.session = load_data()
        self.setWindowTitle("Pomodoro Timer")
        self.setMinimumSize(900, 600)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(STYLESHEET)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        sidebar = self.build_sidebar()

        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

        topbar = self.build_topbar()

        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: #1a1a1a;")
        self.stack.addWidget(self.build_timer_page())
        self.stack.addWidget(self.build_session_page())
        self.stack.addWidget(self.build_settings_page())

        vbox.addWidget(topbar)
        vbox.addWidget(self.stack, 1)

        right_widget = QWidget()
        right_widget.setLayout(vbox)

        hbox.addWidget(sidebar)
        hbox.addWidget(right_widget, 1)
        self.setLayout(hbox)

        self.switch_page(0)

    def build_sidebar(self):
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

        brand = QLabel("🍅 FOCUS")
        brand.setAlignment(Qt.AlignCenter)
        brand.setStyleSheet("""
            color: #ff6b35;
            background-color: transparent;
            font-family: Calibri;
            font-size: 20px;
            font-weight: bold;
            padding: 28px 20px;            
        """)

        vbox.addWidget(brand)

        self.nav_buttons = []
        pages = ["Timer", "Session", "Settings"]

        for i, name in enumerate(pages):
            btn = QPushButton(name)
            btn.setObjectName("nav_btn")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, index=i: self.switch_page(index))
            self.nav_buttons.append(btn)
            vbox.addWidget(btn)

        vbox.addStretch()
        sidebar.setLayout(vbox)
        return sidebar

    def build_topbar(self):
        topbar = QWidget()
        topbar.setObjectName("topbar")
        topbar.setFixedHeight(65)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(25, 0, 25, 0)
        
        self.topbar_title = QLabel("Timer")
        self.topbar_title.setStyleSheet("""
            color: #ffffff;
            background-color: transparent;
            font-family: Calibri;
            font-size: 18px;
            font-weight: bold;
        """)

        date = QLabel(QDate.currentDate().toString("dddd, MMMM d, yyyy"))
        date.setStyleSheet("""
            color: #888888;
            font-family: Calibri;
            font-size: 12px;
            background-color: transparent;
        """)

        hbox.addWidget(self.topbar_title)
        hbox.addStretch()
        hbox.addWidget(date)
        topbar.setLayout(hbox)
        return topbar

    def switch_page(self, index):
        titles = ["Timer", "Session", "Settings"]
        self.stack.setCurrentIndex(index)
        self.topbar_title.setText(titles[index])

        for i, btn in enumerate(self.nav_buttons):
            if i == index:
                btn.setObjectName("nav_btn_active")
            else:
                btn.setObjectName("nav_btn")
            btn.setStyle(btn.style()) # Refresh style
    
    def build_timer_page(self):
        page = QWidget()
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)
        vbox.setContentsMargins(40, 40, 40, 40)
        vbox.setSpacing(20)

        self.session_type_label = QLabel("WORK SESSION")
        self.session_type_label.setStyleSheet("""
            color: #ff6b35;
            background-color: transparent;
            font-family: Calibri;
            font-size: 16px;
            font-weight: bold;
            letter-spacing: 3px;
        """)

        self.timer_display = QLabel("25:00")
        self.timer_display.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-size: 100px;
            font-weight: bold;
            background-color: transparent;
        """)

        self.session_count_label = QLabel("Session 1 of 4")
        self.session_count_label.setStyleSheet("""
            color: #888888;
            font-family: Calibri;
            font-size: 14px;
            background-color: transparent;
        """)

        self.dots_layout = QHBoxLayout()
        self.dots_layout.setAlignment(Qt.AlignCenter)
        self.dots_layout.setSpacing(10)
        self.dots = []

        for i in range(4):
            dot = QLabel("●")
            dot.setStyleSheet("""
                color: #888888;
                font-size: 20px;
                background-color: transparent;
            """)
            self.dots.append(dot)
            self.dots_layout.addWidget(dot)

        btn_row = QHBoxLayout()
        btn_row.setAlignment(Qt.AlignCenter)
        btn_row.setSpacing(15)

        self.start_pause_btn = QPushButton("Start")
        self.start_pause_btn.setObjectName("primary_btn")
        self.start_pause_btn.setCursor(Qt.PointingHandCursor)
        self.start_pause_btn.setFixedWidth(140)
        self.start_pause_btn.clicked.connect(self.start_pause)

        skip_btn = QPushButton("Skip")
        skip_btn.setObjectName("secondary_btn")
        skip_btn.setCursor(Qt.PointingHandCursor)
        skip_btn.setFixedWidth(140)
        skip_btn.clicked.connect(self.skip_session)

        btn_row.addWidget(self.start_pause_btn)
        btn_row.addWidget(skip_btn)

        # Time Logic
        self.work_duration = 25 * 60 # 25 minutes
        self.short_break = 5 * 60 # 5 minutes
        self.long_break = 15 * 60 # 15 minutes
        self.current_seconds = self.work_duration
        self.is_running = False
        self.is_work = True # Start with work session
        self.count_sessions = 0
        self.current_session = 1 # Track current session number

        self.pomodoro_timer = QTimer()
        self.pomodoro_timer.timeout.connect(self.tick)

        vbox.addWidget(self.session_type_label)
        vbox.addWidget(self.timer_display)
        vbox.addWidget(self.session_count_label)
        vbox.addLayout(self.dots_layout)
        vbox.addLayout(btn_row)
        page.setLayout(vbox)
        return page
    
    def start_pause(self):
        if self.is_running:
            self.pomodoro_timer.stop()
            self.is_running = False
            self.start_pause_btn.setText("Resume")
        
        else:
            self.pomodoro_timer.start(1000)
            self.is_running = True
            self.start_pause_btn.setText("Pause")

    def skip_session(self):
        self.pomodoro_timer.stop()
        self.is_running = False
        self.start_pause_btn.setText("Start")
        self.next_session()
        self.start_pause()

    def tick(self):
        if self.current_seconds > 0:
            self.current_seconds -= 1
            self.update_timer_display()

        else:
            self.pomodoro_timer.stop()
            self.is_running = False
            self.start_pause_btn.setText("Start")

            if self.is_work:
                # Save session data
                self.count_sessions += 1
                session = {
                    "date" : QDate.currentDate().toString("yyyy-MM-dd"),
                    "type" : "Work",
                    "duration" : self.work_duration // 60,
                    "session" : self.current_session
                }
                self.session.append(session)
                save_data(self.session)
                self.refresh_sessions()
            
            self.next_session()

    def next_session(self):
        if self.is_work:
            self.is_work = False
            if self.count_sessions % 4 == 0:
                self.current_seconds = self.long_break
                self.session_type_label.setText("LONG BREAK 🌿")
                self.session_type_label.setStyleSheet("""
                    color: #4ade80;
                    font-family: Calibri;
                    font-size: 16px;
                    font-weight: bold;
                    background-color: transparent;
                    letter-spacing: 3px;              
                """)
            
            else:
                self.current_seconds = self.short_break
                self.session_type_label.setText("SHORT BREAK 🕒")
                self.session_type_label.setStyleSheet("""
                    color: #60a5fa;
                    font-family: Calibri;
                    font-size: 16px;
                    font-weight: bold;
                    background-color: transparent;
                    letter-spacing: 3px;              
                """)
            
        else:
            self.is_work = True
            self.current_session += 1
            if self.current_session > 4:
                self.current_session = 1
            self.current_seconds = self.work_duration
            self.session_type_label.setText("WORK SESSION 🍅")
            self.session_type_label.setStyleSheet("""
                color: #ff6b35;
                font-family: Calibri;
                font-size: 16px;
                font-weight: bold;
                background-color: transparent;
                letter-spacing: 3px;
            """)
        
        self.update_timer_display()
        self.update_dots()
        self.session_count_label.setText(f"Session {self.current_session} of 4")


    def update_timer_display(self):
        minutes = self.current_seconds // 60 
        seconds = self.current_seconds % 60
        self.timer_display.setText(f"{minutes:02d}:{seconds:02d}")

    def update_dots(self):
        for i, dot in enumerate(self.dots):
            if i < self.count_sessions % 4:
                dot.setText("●")
                dot.setStyleSheet("""
                    color: #ff6b35;
                    font-size: 20px;
                    background-color: transparent;
                """)
            else:
                dot.setText("○")
                dot.setStyleSheet("""
                    color: #444444;
                    font-size: 20px;
                    background-color: transparent;
                """)
    def build_session_page(self):
        page = QWidget()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(25, 25, 25, 25)
        vbox.setSpacing(20)

        header = QHBoxLayout()

        title = QLabel("COMPLETED SESSIONS")
        title.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-size: 16px;
            font-weight: bold;
            background-color: transparent;
        """)

        # Total session Count
        self.total_label = QLabel("")
        self.total_label.setStyleSheet("""
            color: #ff6b35;
            background-color: transparent;
            font-family: Calibri;
            font-size: 16px;
            font-weight: bold;
        """)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.total_label)

        #Table
        self.session_table = QTableWidget()
        self.session_table.setColumnCount(4)
        self.session_table.setHorizontalHeaderLabels(
            [
                "Date", "Type", "Duration", "Session #"
            ]
        )

        self.session_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.session_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.session_table.verticalHeader().setVisible(False)
        self.session_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.session_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.session_table.setFocusPolicy(Qt.NoFocus)
        self.session_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.refresh_sessions()

        vbox.addLayout(header)
        vbox.addWidget(self.session_table, 1)
        page.setLayout(vbox)
        return page

    def refresh_sessions(self):
        self.session_table.setRowCount(0)

        for s in self.session:
            row = self.session_table.rowCount()
            self.session_table.insertRow(row)

            values = [
                s.get("date", ""),
                s.get("type", ""),
                f"{s.get('duration', 0)}min",
                f"# {s.get('session', 0)}",
            ]

            for col, val in enumerate(values):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                self.session_table.setItem(row, col, item)

        total = len([s for s in self.session if s.get("type") == "Work"])
        self.total_label.setText(f"🍅 {total} sessions completed")

    def build_settings_page(self):
        page = QWidget()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(40, 40, 40, 40)
        vbox.setSpacing(30)

        title = QLabel("Settings")
        title.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-size: 16px;
            font-weight: bold;
            background-color: transparent;
        """)

        # Card
        card = QWidget()
        card.setObjectName("card")
        hbox = QVBoxLayout()
        hbox.setContentsMargins(25, 25, 25, 25)
        hbox.setSpacing(20)

        card_title = QLabel("Time Durations")
        card_title.setStyleSheet("""
            color: #888888;
            font-family: Calibri;
            font-size: 13px;
            font-weight: bold;
            letter-spacing: 2px;
            background-color: transparent;
        """)

        # Work duration Row
        work_row = QHBoxLayout()
        work_label = QLabel("Work Session")
        work_label.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-size: 15px;
            background-color: transparent;
        """)

        self.work_spinbox = QSpinBox()
        self.work_spinbox.setRange(1, 60)
        self.work_spinbox.setValue(25)
        self.work_spinbox.setSuffix(" min")
        self.work_spinbox.setFixedWidth(100)

        work_row.addWidget(work_label)
        work_row.addStretch()
        work_row.addWidget(self.work_spinbox)

        # Short Break Row
        short_row = QHBoxLayout()
        short_label = QLabel("Short Break")
        short_label.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-size: 15px;
            background-color: transparent;
        """)

        self.short_spinbox = QSpinBox()
        self.short_spinbox.setRange(1, 30)
        self.short_spinbox.setValue(5)
        self.short_spinbox.setSuffix(" min")
        self.short_spinbox.setFixedWidth(100)

        short_row.addWidget(short_label)
        short_row.addStretch()
        short_row.addWidget(self.short_spinbox)

        # Long Break Row
        long_row = QHBoxLayout()
        long_label = QLabel("Long Break")
        long_label.setStyleSheet("""
            color: #ffffff;
            font-family: Calibri;
            font-size: 15px;
            background-color: transparent;
        """)

        self.long_spinbox = QSpinBox()
        self.long_spinbox.setRange(1, 60)
        self.long_spinbox.setValue(15)
        self.long_spinbox.setSuffix(" min")
        self.long_spinbox.setFixedWidth(100)

        long_row.addWidget(long_label)
        long_row.addStretch()
        long_row.addWidget(self.long_spinbox)

        save_btn = QPushButton("Save Setting")
        save_btn.setObjectName("primary_btn")
        save_btn.setFixedWidth (160)
        save_btn.setCursor(Qt.PointingHandCursor)
        save_btn.clicked.connect(self.save_settings)

        hbox.addWidget(card_title)
        hbox.addLayout(work_row)
        hbox.addLayout(short_row)
        hbox.addLayout(long_row)
        hbox.addWidget(save_btn)
        card.setLayout(hbox)

        vbox.addWidget(title)
        vbox.addWidget(card)
        vbox.addStretch()
        page.setLayout(vbox)

        return page

    def save_settings(self):
        self.work_duration = self.work_spinbox.value() * 60
        self.short_break = self.short_spinbox.value() * 60
        self.long_break = self.long_spinbox.value() * 60

        # Reset timer w/ new work duration
        self.pomodoro_timer.stop()
        self.is_running = False
        self.current_seconds = self.work_duration
        self.is_work = True
        self.start_pause_btn.setText("Start")
        self.session_type_label.setText("WORK SESSION 🍅")
        self.update_timer_display()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Focus()
    window.show()
    sys.exit(app.exec_())