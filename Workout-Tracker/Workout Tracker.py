# Workout Tracker

import os, json, sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QHBoxLayout, QVBoxLayout, QPushButton, 
    QStackedWidget, QComboBox, QTableWidget,
    QHeaderView, QTableWidgetItem, QLineEdit
)

from PyQt5.QtCore import Qt, QDate, QTimer

DATA_FILE = "workouts.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open (DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open (DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

STYLESHEET = """
    QWidget {
        background-color: #f5f5f5;
        font-family: Calibri;
    }
    QWidget#sidebar {
        background-color: #ffffff;
        border-right: 1px solid #e5e5e5;
    }
    QWidget#topbar {
        background-color: #ffffff;
        border-bottom: 1px solid #e5e5e5;
    }
    QWidget#card {
        background-color: #ffffff;
        border-radius: 12px;
    }
    QPushButton#nav_button {
        color: #888888;
        font-family: Calibri;
        font-weight: bold;
        font-size: 15px;
        padding: 15px 25px;
        text-align: left;
        background-color: transparent;
        border: none;
    }
    QPushButton#nav_button:hover{
        color: #2563eb;
        background-color: #eff6ff;
    }
    QPushButton#nav_button_active{
        color: #2563eb;
        font-family: Calibri;
        font-weight: bold;
        font-size: 15px;
        padding: 15px 22px;
        text-align: left;
        background-color: #eff6ff;
        border: none;
        border-left: 3px solid #2563eb;
    }
    QPushButton#primary_btn {
        color: #ffffff;
        font-family: Calibri;
        font-weight: bold;
        font-size: 14px;
        padding: 10px 25px;
        background-color: #2563eb;
        border: none;
        border-radius: 8px;
    }
    QPushButton#primary_btn:hover {
        background-color: #1d4ed8;
    }
    QPushButton#danger_btn {
        color: #dc2626;
        font-family: Calibri;
        font-weight: bold;
        font-size: 13px;
        padding: 6px 14px;
        background-color: #fee2e2;
        border: none;
        border-radius: 6px;
    }
    QPushButton#danger_btn:hover {
        background-color: #fecaca;
    }
    QLineEdit {
        color: #1a1a1a;
        font-family: Calibri;
        font-size: 13px;
        padding: 8px 12px;
        background-color: #ffffff;
        border: 1px solid #e5e5e5;
        border-radius: 8px;
    }
    QLineEdit:focus{
        border: 1px solid #2563eb;
    }
    QComboBox {
        color: #1a1a1a;
        font-family: Calibri;
        font-size: 13px;
        padding: 8px 12px;
        background-color: #ffffff;
        border: 1px solid #e5e5e5;
        border-radius: 8px;
    }
    QComboBox:focus {
        border: 1px solid #2563eb;
    }
    QComboBox::drop-down {
        border: none;
    }
    QTableWidget {
        color: #1a1a1a;
        font-family: Calibri;
        font-size: 14px;
        background-color: #ffffff;
        border: none;
        gridline-color: #f0f0f0;
    }
    QTableWidget::item {
        padding: 8px;
    }
    QTableWidget::item:selected {
        background-color: #eff6ff;
        color: #1a1a1a;
    }
    QHeaderView::section {
        color: #888888;
        font-family: Calibri;
        font-weight: bold;
        font-size: 13px;
        padding: 8px;
        background-color: #f9fafb;
        border: none;
        border-bottom: 1px solid #e5e5e5;
    }
"""

class Grind(QWidget):
    def __init__(self):
        super().__init__()
        self.workouts = load_data()
        self.setWindowTitle("GRIND")
        self.setMinimumSize(1100, 700)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(STYLESHEET)

        root = QHBoxLayout()
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        sidebar = self.build_sidebar()

        right_side = QVBoxLayout()
        right_side.setContentsMargins(0, 0, 0, 0)
        right_side.setSpacing(0)

        topbar = self.build_topbar()

        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: #f5f5f5;")
        self.stack.addWidget(self.build_log_page())
        self.stack.addWidget(self.build_history_page())
        self.stack.addWidget(self.build_progress_page())
        self.stack.addWidget(self.build_timer_page())

        right_side.addWidget(topbar)
        right_side.addWidget(self.stack, 1)

        right_widget = QWidget()
        right_widget.setLayout(right_side)

        root.addWidget(sidebar)
        root.addWidget(right_widget, 1)
        self.setLayout(root)

        self.switch_page(0)

    def build_sidebar(self):
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)

        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

        brand = QLabel("🏋️ GRIND")
        brand.setStyleSheet("""
            color: #2563eb;
            font-family: Calibri;
            font-size: 20px;
            font-weight: bold;
            padding: 28px 20px;
            background-color: transparent;
        """)

        vbox.addWidget(brand)

        self.nav_buttons = []
        pages = ["Log", "History", "Progress", "Timer"]

        for i, name in enumerate(pages):
            btn = QPushButton(name)
            btn.setObjectName("nav_button")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, idx=i: self.switch_page(idx))
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

        self.topbar_title = QLabel("Log Workout")
        self.topbar_title.setStyleSheet("""
            color: #1a1a1a;
            font-family: Calibri;
            font-size: 18px;
            font-weight: bold;
            background-color: transparent;
        """)

        date = QLabel(QDate.currentDate().toString("dddd, MMMM d yyyy"))
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
        titles = ["Log Workout", "History", "Progress", "Rest Timer"]
        self.stack.setCurrentIndex(index)
        self.topbar_title.setText(titles[index])

        for i, btn in enumerate(self.nav_buttons):
            if i == index:
                btn.setObjectName("nav_button_active")
            else:
                btn.setObjectName("nav_button")
            btn.setStyle(btn.style())
    
    def build_log_page(self):
        page = QWidget()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(25, 25, 25, 25)
        vbox.setSpacing(20)

        card = QWidget()
        card.setObjectName("card")
        card_vbox = QVBoxLayout()
        card_vbox.setContentsMargins(20, 20, 20, 20)
        card_vbox.setSpacing(15)

        card_title = QLabel("Add Workout")
        card_title.setStyleSheet("""
            color: #1a1a1a;
            font-family: Calibri;
            font-size: 15px;
            font-weight: bold;
            background-color: transparent;
        """)

        row1 = QHBoxLayout()
        row1.setSpacing(15)

        self.category_combo = QComboBox()
        self.category_combo.setCursor(Qt.PointingHandCursor)
        self.categories = {
            "Chest"    :      ["Incline DB Press", "Machine Pec Dec", "Barbell Bench Press", "Cable Flys", "Push-ups"],
            "Back"     :      ["Pull-ups", "Lat Pulldown", "Barbell Rows", "Chest Supported T-bar Rows", "Lat Prayers"],
            "Legs"     :      ["Barbell Squats", "Leg Press", "RDLs", "Leg Extension", "Leg Curls", "Bulgarian Split-squats", "Calves"],
            "Arms"     :      ["Barbell Skull Crushers", "Dips", "Cable Pushdown", "Preacher Curls", "Barbell Curls", "Incline DB Curls"],
            "Shoulders":      ["Cable Lateral Raises", "DB Lateral Raises", "Full ROM Laterals", "Reverse Flys", "Face Pull", "Shrugs"]
        }

        self.category_combo.addItems(self.categories.keys())
        self.category_combo.currentTextChanged.connect(self.update_exercises)

        self.exercise_combo = QComboBox()
        self.exercise_combo.setCursor(Qt.PointingHandCursor)
        self.update_exercises(self.category_combo.currentText())

        row1.addWidget(QLabel("Category"))
        row1.addWidget(self.category_combo, 1)
        row1.setSpacing(10)
        row1.addWidget(QLabel("Exercise"))
        row1.addWidget(self.exercise_combo, 1)

        row2 = QHBoxLayout()
        row2.setSpacing(15)

        self.sets_input = QLineEdit()
        self.sets_input.setPlaceholderText("Sets")

        self.reps_input = QLineEdit()
        self.reps_input.setPlaceholderText("Reps")

        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Weight (kg)")

        self.log_btn = QPushButton("+ Log workout")
        self.log_btn.setObjectName("primary_btn")
        self.log_btn.setCursor(Qt.PointingHandCursor)
        self.log_btn.clicked.connect(self.log_workout)
        self.log_btn.setFixedSize(150, 45)
        self.log_btn.setStyleSheet("background-color: #2563eb; color: white; border-radius: 8px;")

        row2.addWidget(self.sets_input, 1)
        row2.addWidget(self.reps_input, 1)
        row2.addWidget(self.weight_input, 1)
        row2.addWidget(self.log_btn)

        card_vbox.addWidget(card_title)
        card_vbox.addLayout(row1)
        card_vbox.addLayout(row2)
        card.setLayout(card_vbox)

        session_label = QLabel("Today's Session")
        session_label.setStyleSheet("""
            color: #1a1a1a;
            font-family: Calibri;
            font-size: 15px;
            font-weight: bold;
            background-color: transparent;
        """)

        self.session_table = QTableWidget()
        self.session_table.setColumnCount(5)
        self.session_table.setHorizontalHeaderLabels(
            ["Exercise", "Category", "Sets", "Reps", "Weight"]
        )

        self.session_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Makes all 5 columns stretch equally to fill the full table width.
        self.session_table.verticalHeader().setVisible(False) # Hides the row numbers (1, 2, 3...) on the left side.
        self.session_table.setEditTriggers(QTableWidget.NoEditTriggers) # Makes the table read-only
        self.session_table.setSelectionBehavior(QTableWidget.SelectRows) # Clicking any cell highlights the entire row instead of just that one cell
        self.session_table.setFocusPolicy(Qt.NoFocus) # Removes the blue dotted rectangle that appears around the table when clicked.
        self.session_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # Hides the vertical scrollbar on the right.
        
        vbox.addWidget(card)
        vbox.addWidget(session_label)
        vbox.addWidget(self.session_table, 1)
        page.setLayout(vbox)
        return page

    def update_exercises(self, category):
        self.exercise_combo.clear()
        self.exercise_combo.addItems(self.categories.get(category, []))

    def log_workout(self):
        exercise = self.exercise_combo.currentText()
        category = self.category_combo.currentText()
        sets     = self.sets_input.text().strip()
        reps     = self.reps_input.text().strip()
        weight   = self.weight_input.text().strip()

        if not all([exercise, sets, reps, weight]):
            return

        workout = {
            "date" : QDate.currentDate().toString("dd-MM-yyyy"),
            "exercise" : exercise,
            "category" : category,
            "sets" : sets,
            "reps" : reps,
            "weight" : weight
        }

        self.workouts.append(workout)
        save_data(self.workouts)

        row = self.session_table.rowCount()
        self.session_table.insertRow(row)
        self.session_table.setItem(row, 0, QTableWidgetItem(exercise))
        self.session_table.setItem(row, 1, QTableWidgetItem(category))
        self.session_table.setItem(row, 2, QTableWidgetItem(sets))
        self.session_table.setItem(row, 3, QTableWidgetItem(reps))
        self.session_table.setItem(row, 4, QTableWidgetItem(weight + "kg"))
        
        for col in range(5):
            item = self.session_table.item(row, col)
            if item:
                item.setTextAlignment(Qt.AlignCenter)

        self.sets_input.clear()
        self.reps_input.clear()
        self.weight_input.clear()
        self.refresh_history()
        self.refresh_progress()
    
    def build_history_page(self):
        page = QWidget()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(25, 25, 25, 25)
        vbox.setSpacing(20)

        header_row = QHBoxLayout()

        title = QLabel("All Workouts")
        title.setStyleSheet("""
            color: #1a1a1a;
            font-family: Calibri;
            font-size: 16px;
            font-weight: bold;
            background-color: transparent;
        """)

        header_row.addWidget(title)
        header_row.addStretch()

        self.history_table = QTableWidget()
        self.history_table.setColumnCount(7)
        self.history_table.setHorizontalHeaderLabels(
            ["Date", "Exercise", "Category", "Sets", "Reps", "Weight", "Delete"]
        )

        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Makes all 6 columns stretch equally to fill the full table width.
        self.history_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter) # Centers the header text in each column.
        self.history_table.verticalHeader().setVisible(False) # Hides the row numbers (1, 2, 3...) on the left side.
        self.history_table.setEditTriggers(QTableWidget.NoEditTriggers) # Makes the table read-only
        self.history_table.setSelectionBehavior(QTableWidget.SelectRows) # Clicking any cell highlights the entire row instead of just that one cell
        self.history_table.setFocusPolicy(Qt.NoFocus) # Removes the blue dotted rectangle that appears around the table when clicked.
        self.history_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # Hides the vertical scrollbar on the right.
        
        self.refresh_history()
        vbox.addLayout(header_row)
        vbox.addWidget(self.history_table, 1)
        page.setLayout(vbox)
        return page

    def refresh_history(self): # This method is responsible for populating the history table with the workouts data from the workouts list.
        self.history_table.setRowCount(0) # Clear all existing rows from the history table to prepare for repopulation with the current workouts data.
        for i, w in enumerate(self.workouts): # Loop through each workout in the workouts list, where 'i' is the index and 'w' is the workout dictionary.
            row = self.history_table.rowCount() # Get the current number of rows in the table, which will be the index for the new row to insert.
            self.history_table.insertRow(row) # Insert a new empty row at the end of the table and get its index.
            for col, key in enumerate(["date", "exercise", "category", "sets", "reps", "weight"]): # Loop through the first 6 keys of the workout dictionary, where 'col' is the column index and 'key' is the key name (e.g., "date", "exercise", etc.)
                item = QTableWidgetItem(str(w.get(key, ""))) # Convert the value to string in case it's not already (e.g., weight might be a number)
                self.history_table.setItem(row, col, item) # Populate the first 6 columns with workout data
                self.history_table.item(row, col).setTextAlignment(Qt.AlignCenter) # Center-align the text in each cell for better readability
        
            del_btn = QPushButton("Delete")
            del_btn.setCursor(Qt.PointingHandCursor)
            del_btn.clicked.connect(lambda checked, idx=i: self.delete_workout(idx)) # Connect the delete button's click event to the delete_workout method, passing the current workout index 'i'
            self.history_table.setCellWidget(row, 6, del_btn) # Place the delete button in the 7th column of the current row

    def delete_workout(self, index):
        self.workouts.pop(index) # Remove the workout at the specified index from the workouts list
        save_data(self.workouts) # Save the updated workouts list to the JSON file to persist the deletion
        self.refresh_history() # Refresh the history table to reflect the deletion
        self.refresh_progress() # Refresh the progress page as well, since deleting a workout may affect the personal bests and total sets displayed there.

    def build_progress_page(self): # This method constructs the UI for the progress page, which includes a title label and a table that will display the user's personal bests and total sets for each exercise based on the workouts data. The refresh_progress() method will be responsible for calculating and populating the table with the relevant data.
        page = QWidget()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(25, 25, 25, 25)
        vbox.setSpacing(20)

        title = QLabel("Personal Bests")
        title.setStyleSheet("""
            color: #1a1a1a;
            font-family: Calibri;
            font-size: 16px;
            font-weight: bold;
            background-color: transparent;
        """)

        self.progress_table = QTableWidget()
        self.progress_table.setColumnCount(4)
        self.progress_table.setHorizontalHeaderLabels (
            ["Exercise", "Category", "Best Weight", "Total Sets"]
        )

        self.progress_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Makes all 4 columns stretch equally to fill the full table width.
        self.progress_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter) # Centers the header text in each column.
        self.progress_table.verticalHeader().setVisible(False) # Hides the row numbers (1, 2, 3...) on the left side.
        self.progress_table.setEditTriggers(QTableWidget.NoEditTriggers) # Makes the table read-only
        self.progress_table.setSelectionBehavior(QTableWidget.SelectRows) # Clicking any cell highlights the entire row instead of just that one cell.
        self.progress_table.setFocusPolicy(Qt.NoFocus) # Removes the blue dotted rectangle that appears around the table when clicked.
        self.progress_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # Hides the vertical scrollbar on the right.

        self.refresh_progress() # This method will calculate the personal bests and total sets for each exercise based on the workouts data and populate the progress table accordingly. Implementation will be added in a future update.

        vbox.addWidget(title)
        vbox.addWidget(self.progress_table, 1)
        page.setLayout(vbox)
        return page
    
    def refresh_progress(self):
        self.progress_table.setRowCount(0) # Clear existing rows before repopulating.

        bests = {}
        for w in self.workouts:
            exercise = w.get("exercise") # Get the exercise name from the workout dictionary.
            category = w.get("category") # Get the category name from the workout dictionary.
            weight = str(w.get("weight", "0")) # Convert the weight value to a float for comparison, defaulting to 0 if it's missing or invalid.
            sets = int(w.get("sets", "0")) # Convert the sets value to an integer, defaulting to 0 if it's missing or invalid.

            try:
                weight_val = float(weight)

            except ValueError:
                weight_val = 0.0

            if exercise not in bests: # If this exercise hasn't been encountered before, add it to the bests dictionary with the current workout's category, weight, and sets as the initial values.
                bests[exercise] = {
                    "category": category,
                    "best_weight": weight_val,
                    "total_sets": sets
                }
            else: # If the exercise is already in the bests dictionary, compare the current workout's weight with the stored best weight. If it's higher, update the best weight. Also, add the current workout's sets to the total sets for that exercise.
                bests[exercise]["total_sets"] += sets
                if weight_val > bests[exercise]["best_weight"]:
                    bests[exercise]["best_weight"] = weight_val

        for exercise, data in bests.items(): # Loop through the bests dictionary to populate the progress table. For each exercise, insert a new row and fill in the exercise name, category, best weight, and total sets.
            row = self.progress_table.rowCount()
            self.progress_table.insertRow(row)

            values = [
                exercise,
                data["category"],
                f"{str(data['best_weight'])} kg",
                f"{str(data['total_sets'])} sets",
            ]

            for col, val in enumerate(values):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignCenter)
                self.progress_table.setItem(row, col, item)
    
    def build_timer_page(self): # This method constructs the UI for the timer page, which includes a large timer display, a status label, control buttons for starting/pausing and resetting the timer, and preset buttons for quickly setting common timer durations. The timer logic will be implemented in the start_pause_timer(), reset_timer(), set_timer(), tick_timer(), and update_timer_label() methods.
        page = QWidget()
        vbox = QVBoxLayout()
        vbox.setContentsMargins(25, 25, 25, 25)
        vbox.setSpacing(20)
        vbox.setAlignment(Qt.AlignCenter)

        # Timer display
        self.timer_label = QLabel("02:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("""
            color: #CCCCD9;
            font-family: Calibri;
            font-size: 100px;
            font-weight: bold;
            background-color: transparent;
        """)

        # Status Label
        self.status_label = QLabel("Ready!")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            color: #888888;
            font-family: Calibri;
            font-size: 16px;
            background-color: transparent;                           
        """)

        # Control Buttons
        btn_row = QHBoxLayout()
        btn_row.setSpacing(15)
        btn_row.setAlignment(Qt.AlignCenter)

        self.start_pause_btn = QPushButton("Start")
        self.start_pause_btn.setObjectName("primary_btn")
        self.start_pause_btn.setCursor(Qt.PointingHandCursor)
        self.start_pause_btn.setFixedWidth(120)
        self.start_pause_btn.setStyleSheet("""
            QPushButton#primary_btn {
                background-color: #2563eb;
                color: #ffffff;
                font-family: Calibri;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 25px;
                border: none;
                border-radius: 8px;
            }
            QPushButton#primary_btn:hover {
                background-color: #1d4ed8;
            }
        """)
        self.start_pause_btn.clicked.connect(self.start_pause_timer)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setObjectName("danger_btn")
        self.reset_btn.setCursor(Qt.PointingHandCursor)
        self.reset_btn.setFixedWidth(120)
        self.reset_btn.setStyleSheet("""
            QPushButton#danger_btn {
                background-color: #ff0000;
                color: #ffffff;
                font-family: Calibri;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 25px;
                border: none;
                border-radius: 8px;
            }
            QPushButton#danger_btn:hover {
                background-color: #cc0000;
            }
        """)
        self.reset_btn.clicked.connect(self.reset_timer)

        btn_row.addWidget(self.start_pause_btn)
        btn_row.addWidget(self.reset_btn)

        preset_row = QHBoxLayout()
        preset_row.setSpacing(10)
        preset_row.setAlignment(Qt.AlignCenter)

        presets = [("30 sec", 30), ("1 min", 60), ("90 sec", 90), ("2 min", 120), ("3 min", 180), ("5 min", 300)]
        for label, seconds in presets:
            btn = QPushButton(label)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedWidth(80)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    color: #2563eb;
                    font-family: Calibri;
                    font-size: 13px;
                    font-weight: bold;
                    padding: 8px;
                    border: 2px solid #2563eb;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #eff6ff;
                }
            """)
            btn.clicked.connect(lambda checked, s = seconds: self.set_timer(s))
            preset_row.addWidget(btn)

        # Timer Logic
        self.timer_second = 120
        self.timer_running = False
        self.qt_timer = QTimer(self)
        self.qt_timer.timeout.connect(self.tick_timer)

        vbox.addWidget(self.timer_label)
        vbox.addWidget(self.status_label)
        vbox.addLayout(btn_row)
        vbox.addLayout(preset_row)
        page.setLayout(vbox)
        return page

    def start_pause_timer(self): # When the start/pause button is clicked, this method checks if the timer is currently running. If it is, it stops the QTimer, sets timer_running to False, updates the button text to "Resume", and changes the status label to "Paused". If the timer is not running, it starts the QTimer with a 1-second interval, sets timer_running to True, updates the button text to "Pause", and changes the status label to "Rest..." to indicate that the timer has started.
        if self.timer_running:
            self.qt_timer.stop()
            self.timer_running = False
            self.start_pause_btn.setText("Resume")
            self.status_label.setText("Paused")

        else:
            self.qt_timer.start(1000)
            self.timer_running = True
            self.start_pause_btn.setText("Pause")
            self.status_label.setText("Rest...")

    def reset_timer(self): # When the reset button is clicked, this method stops the timer if it's running, resets the timer seconds to the default value (120 seconds), updates the start/pause button text back to "Start", and updates the status label to "Ready!" to indicate that the timer has been reset and is ready to start again.
        self.qt_timer.stop()
        self.timer_running = False
        self.timer_second = 120
        self.start_pause_btn.setText("Start")
        self.status_label.setText("Ready!")
        self.update_timer_label()

    def set_timer(self, seconds): # This method is called when a preset timer button is clicked. It stops the timer if it's currently running, sets the timer_second variable to the specified number of seconds, updates the start/pause button text back to "Start", updates the status label to "Ready!", and calls update_timer_label() to refresh the timer display with the new time.
        self.qt_timer.stop()
        self.timer_running = False
        self.timer_second = seconds
        self.start_pause_btn.setText("Start")
        self.status_label.setText("Ready!")
        self.update_timer_label()

    def tick_timer(self): # This method is called every second by the QTimer when the timer is running. It checks if there are still seconds left on the timer. If there are, it decrements the timer_second variable by 1 and calls update_timer_label() to refresh the timer display. If the timer has reached zero, it stops the QTimer, sets timer_running to False, updates the start/pause button text to "Start", changes the status label to "Time's up!", and updates the timer label's style to indicate that the time has expired.
        if self.timer_second > 0:
            self.timer_second -= 1
            self.update_timer_label()
        
        else:
            self.qt_timer.stop()
            self.timer_running = False
            self.start_pause_btn.setText("Start")
            self.status_label.setText("Time's up!")
            self.timer_label.setStyleSheet("""
                color: #1a1a1a;
                font-family: Calibri;
                font-size: 100px;
                font-weight: bold;
                background-color: transparent;
        """)

    def update_timer_label(self): # This method updates the timer display label based on the current value of timer_second. It calculates the minutes and seconds from the total seconds, formats them as MM:SS, and updates the timer_label text accordingly. It also resets the timer label's style to the default appearance in case it was changed when the timer expired.
        mins = self.timer_second // 60
        secs = self.timer_second % 60
        self.timer_label.setText(f"{mins:02}:{secs:02}")
        self.timer_label.setStyleSheet("""
            color: #2563eb;
            font-family: Calibri;
            font-size: 100px;
            font-weight: bold;
            background-color: transparent;
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Grind()
    window.show()
    sys.exit(app.exec_())