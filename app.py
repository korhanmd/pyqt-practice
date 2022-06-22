import sys
from random import choice

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
	'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")

		self.button = QPushButton("Press Me!")
		self.button.clicked.connect(self.the_button_was_clicked)

		self.setCentralWidget(self.button)

	def the_button_was_clicked(self):
		print("Clicked!")
		new_window_title = choice(window_titles)

		print("Setting title: %s" % new_window_title)
		self.setWindowTitle(new_window_title)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()