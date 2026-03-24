from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from qt_material import apply_stylesheet
from datetime import datetime

class AgeCalculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        self.setMinimumSize(500, 250)
        grid = QGridLayout()

        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_label = QLabel("Date of Birth (DD/MM/YYYY):")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)


        self.setLayout(grid)

    def calculate_age(self):
        try:
            current_year = datetime.now().year
            date_of_birth = self.date_birth_line_edit.text()
            year_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y").date().year

            age = current_year - year_of_birth

            current_month = datetime.now().month
            date_of_month= self.date_birth_line_edit.text()
            month_of_birth = datetime.strptime(date_of_month, "%d/%m/%Y").date().month

            month = current_month - month_of_birth

            current_day = datetime.now().day
            day_of_birth = self.date_birth_line_edit.text()
            birth_day = datetime.strptime(day_of_birth, "%d/%m/%Y").date().day

            day = current_day - birth_day

            self.output_label.setText(f"{self.name_line_edit.text()} is {age} years, {month} months , {day} days old. ")
        except ValueError:
            self.output_label.setText("Please enter a valid Date of Birth")

app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_teal.xml')
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

