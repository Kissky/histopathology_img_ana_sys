#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    w = QWidget()
    w.resize(1000, 500)
    w.move(1500, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
