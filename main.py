import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
from expert.expert_agent import ExpertAgent
from expert.schema import UserAppRequest

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.resize(400, 300)
        
        my_layout = QVBoxLayout()

        self.text_field = QLineEdit(self)
        my_layout.addWidget(self.text_field)

        self.button = QPushButton("Click me!", self)
        self.button.clicked.connect(self.on_button_click)
        my_layout.addWidget(self.button)

        central_widget = QWidget(self)
        central_widget.setLayout(my_layout)
        self.setCentralWidget(central_widget)

    def on_button_click(self):
        print("Button clicked!")
        print("Text field value:", self.text_field.text())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

# if __name__ == "__main__":
#     expert = ExpertAgent()
#     expert.reset()
#     expert.declare(UserAppRequest(
#         category="Games",
#         user_rating=5.0
#     ))
#     expert.run()