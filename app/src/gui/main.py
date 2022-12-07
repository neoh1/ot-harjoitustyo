import sys
import os
import json
from pathlib import Path
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
        self.center_window()
        self.show()

        # popup menu
        self.ui.trainButton.clicked.connect(
            lambda: self.ui.leftPopMenuCont.expandMenu())
        self.ui.systemTempButton.clicked.connect(
            lambda: self.ui.leftPopMenuCont.expandMenu())
        self.ui.resultsButton.clicked.connect(
            lambda: self.ui.leftPopMenuCont.expandMenu())
        self.ui.settingsButton.clicked.connect(
            lambda: self.ui.leftPopMenuCont.expandMenu())

        self.ui.hidePopMenuButton.clicked.connect(
            lambda: self.ui.leftPopMenuCont.collapseMenu())
        #self.ui.homeButton.clicked.connect(lambda: self.ui.leftPopMenuCont.collapseMenu())
        self.ui.closeAlertButton.clicked.connect(
            lambda: self.ui.popupCont.collapseMenu())

    def get_style(self, path=Path(__file__).with_name('style.json')):
        with open(path, 'r') as file:
            return json.load(file)

    def center_window(self):
        frame_geom = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geom.moveCenter(center_point)
        self.move(frame_geom.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
