import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    """ Takes layout mode as parameter
    0 for grid layout
    1 for horizontal and vertical layouts
    """

    def __init__(self, layout_mode):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        if (layout_mode):
            layout1 = QHBoxLayout()
            layout2 = QVBoxLayout()
            layout3 = QVBoxLayout()

            layout1.setContentsMargins(0,0,0,0)
            layout1.setSpacing(20)

            layout2.addWidget(Color('red'))
            layout2.addWidget(Color('yellow'))
            layout2.addWidget(Color('purple'))

            layout1.addLayout(layout2)

            layout1.addWidget(Color('green'))

            layout3.addWidget(Color('red'))
            layout3.addWidget(Color('purple'))

            layout1.addLayout(layout3)
        else:
            layout = QGridLayout()

            layout.addWidget(Color('red'), 0, 0)
            layout.addWidget(Color('green'), 1, 0)
            layout.addWidget(Color('blue'), 1, 1)
            layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()

        if (layout_mode):
            widget.setLayout(layout1)
        else:
            widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow(0)
window.show()

app.exec()