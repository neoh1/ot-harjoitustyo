import sys
from PySide6.QtCore import QSize, QtMsgType
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gradient Descender")
        self.setMinimumSize(QSize(800, 600))
        
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
      
        container = QWidget()
        container.setLayout(layout)

        login_button = QPushButton("Login")
        login_button.setCheckable(True)
        login_button.clicked.connect(self.login_clicked)
        #login_button.clicked.connect(self.login_toggled)

        exit_button = QAction("Exit", self)
        exit_button.setStatusTip("Exits the program")
        exit_button.triggered.connect(self.exit_clicked)
        exit_button.setCheckable(True)

        #widget
        self.setCentralWidget(container)

        menu = self.menuBar()

        menu_file = menu.addMenu("&File")
        menu_file = menu.addAction(exit_button)

    def login_clicked(self):
        #  TODO: check if login works
        # Redirect to home page
        print("Login clicked!")

    def exit_clicked(self):
        print("Exit clicked")
        sys.exit()

    def contextMenuEvent(self, event):
        right_menu = QMenu(self)
        right_menu.addAction(QAction("Logout", self))
        right_menu.exec(event.globalPos())

    #def login_toggled(self, checked):
    #    print("toggled?", checked)
    #    self.login_button.setText("nice try")
    #    self.login_button.setEnabled(False)
    #    self.setWindowTitle("Haxor detected")
