import sys
import os
import json
from PySide2 import *
from gui.main_gui import *
from Custom_Widgets.Widgets import *



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.customWidgetsThreadpool = QThreadPool()
        applyJsonStyle(self, self.ui, self.get_style())
        self.show()

        #popup menu
        self.ui.trainButton.clicked.connect(lambda: self.ui.leftPopMenuCont.expandMenu())
        self.ui.systemTempButton.clicked.connect(lambda: self.ui.leftPopMenuCont.expandMenu())
        self.ui.resultsButton.clicked.connect(lambda: self.ui.leftPopMenuCont.expandMenu())
        self.ui.settingsButton.clicked.connect(lambda: self.ui.leftPopMenuCont.expandMenu())

        self.ui.hidePopMenuButton.clicked.connect(lambda: self.ui.leftPopMenuCont.collapseMenu())
        #self.ui.homeButton.clicked.connect(lambda: self.ui.leftPopMenuCont.collapseMenu())
        self.ui.closeAlertButton.clicked.connect(lambda: self.ui.popupCont.collapseMenu())

    def get_style(self, path="src/gui/style.json"):
        with open(path, 'r') as file:
            return json.load(file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
