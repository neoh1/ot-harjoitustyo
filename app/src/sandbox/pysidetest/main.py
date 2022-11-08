import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from circular_progress import CircularProgress

#GLOBALS
counter = 0


class MainWindow(QMainWindow):
    """
    Window for circular progress bar testing
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(500, 500)

        # Remove standard title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Container
        self.container = QFrame()
        self.container.setStyleSheet("background-color: transparent")
        self.layout = QVBoxLayout()

        # CREATE CIRCULAR PROGRESS BAR
        self.progress = CircularProgress()
        self.progress.value = 50  # initial value for testing
        self.progress.add_shadow(True)
        self.progress.setMinimumSize(self.progress.width, self.progress.height)

        # ADD SLIDER
        self.slider = QSlider(Qt.Horizntal)  # values for circular progress
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.change_value)

        # Add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.slider, Qt.AlignCenter, Qt.AlignCenter)

        # Set CENTRAL WIDGET
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # Display window
        self.show()

    def change_value(self, value):
        self.progress.set_value(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())o
