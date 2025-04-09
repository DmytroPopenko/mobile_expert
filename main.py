import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout
from expert.expert_agent import ExpertAgent
from expert.schema import UserAppRequest

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.resize(400, 300)

        self.center = QVBoxLayout()

        self.text_field = QLineEdit(self)
        self.center.addWidget(self.text_field)

        self.button = QPushButton("Click me!", self)
        self.button.move(20, 60)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button clicked!")
        print("Text field value:", self.text_field.text())

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())

if __name__ == "__main__":
    expert = ExpertAgent()
    expert.reset()
    expert.declare(UserAppRequest(app_type="Social Media", download_count_from=100, download_count_to=10000000))
    expert.run()