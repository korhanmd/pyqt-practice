import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

from PyQt5.uic import loadUi


class Window(QMainWindow):
    """Main window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        # Use a QPushButton for the central widget
        self.centralWidget = QPushButton("Employee...")
        # Connect the .clicked() signal with the .onEmployeeBtnClicked() slot
        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
        self.setCentralWidget(self.centralWidget)

    # Create a slot for launching the employee dialog
    def onEmployeeBtnClicked(self):
        """Launch the employee dialog."""
        dlg = EmployeeDlg(self)
        dlg.exec()


class EmployeeDlg(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Load the dialog's GUI
        loadUi("dialog.ui", self)


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the application's main window
    win = Window()
    win.show()
    # Run the application's main loop
    sys.exit(app.exec())