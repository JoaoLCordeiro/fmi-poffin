from PyQt6.QtWidgets import QMainWindow  # , QApplication
from ui.mainwindow import Ui_MainWindow


class PoffinQt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Poffin Window Class
        """

        super(PoffinQt, self).__init__()
        self.setupUi(self)
