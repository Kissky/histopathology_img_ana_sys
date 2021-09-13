#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        QToolTip.setFont(QFont('华文行楷', 20))
        self.setToolTip('This is a <b><i>QWidget</i></b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit())
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 300)

        self.setGeometry(1000, 300, 1000, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('C:/Document/NXU/HTML/NXUHelper/Pics/NXU.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()
    # w = QWidget()
    # w.resize(1000, 500)
    # w.move(1500, 300)
    # w.setWindowTitle('Simple')
    # w.show()
    sys.exit(app.exec_())
