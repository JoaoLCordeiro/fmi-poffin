#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication

from poffin_qt import PoffinQt


def main():
    app = QApplication(["Poffin from FMI"])
    main_win = PoffinQt()
    main_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
