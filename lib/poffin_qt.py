from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QThread
from PyQt6.QtGui import QAction
from ui.mainwindow import Ui_MainWindow
from ui.configwindow import Ui_ConfigWindow


class Worker(QThread):
    """TODO
    """
    def __init__(self, func, args):
        """TODO
        """

        super(Worker, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        """TODO
        """

        self.func(*self.args)

    def set_args(self, args):
        """TODO
        """

        self.args = args


class PoffinConfigQt(QMainWindow, Ui_ConfigWindow):
    def __init__(self):
        """Poffin Config Window Class
        """

        super(PoffinConfigQt, self).__init__()
        self.setupUi(self)


class PoffinQt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Poffin Window Class
        """

        super(PoffinQt, self).__init__()
        self.setupUi(self)

        self.config_window = PoffinConfigQt()
        self.menuSettings.triggered.connect(
            self.config_window.show
        )
