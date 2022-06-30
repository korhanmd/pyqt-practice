import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Hello!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.question(self, "I have a question!", "This is a simple dialog")

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()