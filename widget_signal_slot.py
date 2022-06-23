from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()