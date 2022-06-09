#!/usr/bin/env python3

import sys
from keyboard_project.gui import MyWindow
from PyQt5.QtWidgets import QApplication


def main():

    app = QApplication(sys.argv)

    ex = MyWindow(app)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
  