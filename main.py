from expert.expert_agent import ExpertAgent
from expert.schema import UserAppRequest

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QDoubleSpinBox,
    QSpinBox,
    QComboBox,
    QMessageBox,
    QTextEdit,
    QDialog
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.expert = ExpertAgent()
        self.expert.reset()
        categories = self.expert.df['prime_genre'].unique()
        age_ratings = self.expert.df['cont_rating'].unique()

        categories.sort()
        age_ratings.sort()

        self.setWindowTitle("My Application")
        self.resize(400, 800)
        
        layout = QVBoxLayout()

        # Price
        layout.addWidget(QLabel("Max Price ($):"))
        self.price_input = QDoubleSpinBox()
        self.price_input.setRange(0, 100)
        self.price_input.setDecimals(2)
        layout.addWidget(self.price_input)

        # Category (Dropdown)
        layout.addWidget(QLabel("App Category:"))
        self.category_input = QComboBox()
        self.category_input.addItems(categories)
        layout.addWidget(self.category_input)

        # Size
        layout.addWidget(QLabel("Max Size (MB):"))
        self.size_input = QSpinBox()
        self.size_input.setRange(0, 5000)
        layout.addWidget(self.size_input)

        # Rating Count
        layout.addWidget(QLabel("Minimum Total Ratings:"))
        self.rating_count_input = QSpinBox()
        self.rating_count_input.setRange(0, 10000000)
        layout.addWidget(self.rating_count_input)

        # User Rating
        layout.addWidget(QLabel("Minimum User Rating (0.0 - 5.0):"))
        self.user_rating_input = QDoubleSpinBox()
        self.user_rating_input.setRange(0, 5)
        self.user_rating_input.setDecimals(1)
        layout.addWidget(self.user_rating_input)

        # Age Rating (Dropdown)
        layout.addWidget(QLabel("Age Rating:"))
        self.age_rating_input = QComboBox()
        self.age_rating_input.addItems(age_ratings)
        layout.addWidget(self.age_rating_input)

        # Submit Button
        self.button = QPushButton("Submit Preferences")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
        print("Preferences Submitted:")
        print("Price:", self.price_input.value())
        print("Category:", self.category_input.currentText())
        print("Size:", self.size_input.value())
        print("Rating Count:", self.rating_count_input.value())
        print("User Rating:", self.user_rating_input.value())
        print("Age Rating:", self.age_rating_input.currentText())

        user_request = UserAppRequest(
            price=self.price_input.value(),
            category=self.category_input.currentText(),
            size=self.size_input.value(),
            rating_count=self.rating_count_input.value(),
            user_rating=self.user_rating_input.value(),
            age_rating=self.age_rating_input.currentText()
        )
        self.expert.declare(user_request)
        self.expert.run()
        self.expert.reset()

        if self.expert.output_list:
            apps = set(self.expert.output_list)

            dialog = QDialog()
            dialog.setWindowTitle("Recommended Apps")
            dialog.setMinimumWidth(400)

            layout = QVBoxLayout()

            message = QMessageBox()
            message.setText("You might like the following apps:")
            message.setIcon(QMessageBox.Information)

            text_edit = QTextEdit()
            text_edit.setReadOnly(True)
            text_edit.setStyleSheet("font-family: Consolas; font-size: 12pt;")
            text_edit.setText("\n".join(sorted(apps)))

            ok_button = QPushButton("Return to Main")
            ok_button.clicked.connect(dialog.accept)

            layout.addWidget(message)
            layout.addWidget(text_edit)
            layout.addWidget(ok_button)

            dialog.setLayout(layout)
            dialog.exec_()

            self.expert.output_list = []
            del apps
            

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
