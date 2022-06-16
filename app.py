import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")

		button = QPushButton("Press Me!")

		self.setFixedSize(QSize(400, 300))

		self.setCentralWidget(button)

	def the_button_was_clicked(self):
		print("Clicked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()