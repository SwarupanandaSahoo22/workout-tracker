#PyQt5 Gym workout tracker

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, 
    QVBoxLayout, QHBoxLayout, QPushButton, 
    QStackedWidget, QLineEdit, QFormLayout,
    QDialog
)
from PyQt5.QtCore import Qt

class AddWorkout(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Add Workout")

        self.exercise_input = QLineEdit()
        self.sets_input = QLineEdit()
        self.reps_input = QLineEdit()
        self.weight_input = QLineEdit()

        save_btn = QPushButton("Save Workout")

        layout = QFormLayout()

        layout.addRow("Exercise: ", self.exercise_input)
        layout.addRow("Sets: ", self.sets_input)
        layout.addRow("Reps: ", self.reps_input)
        layout.addRow("Weight: ", self.weight_input)
        self.addWidget(save_btn)

        self.setLayout(layout)

class Grind(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("GRIND")
        title = QLabel("GRIND")
        self.setMinimumSize(1100, 700)
        self.setStyleSheet("background-color: #f5f5f5;")

        self.add_workout_btn = QPushButton("Add Wokout")
        self.add_workout_btn.clicked.connect(self.open_add_workout)

        self.view_workout_btn = QPushButton("View Workout")
        self.progress_btn = QPushButton("Progress")

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addWidget(self.add_workout_btn)
        layout.addWidget(self.view_workout_btn)
        layout.addWidget(self.progress_btn)
        
        self.setLayout(layout)

    def open_add_workout(self):
        self.window = AddWorkout()
        sys.window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Grind()
    window.show()
    sys.exit(app.exec_())