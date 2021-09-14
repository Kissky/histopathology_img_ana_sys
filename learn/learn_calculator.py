#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
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

        q_btn = QPushButton('Quit', self)
        q_btn.clicked.connect(QCoreApplication.instance().quit)
        q_btn.resize(q_btn.sizeHint())
        q_btn.move(300, 100)

        self.setGeometry(1000, 300, 1000, 220)
        self.center()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('C:/Document/NXU/HTML/NXUHelper/Pics/NXU.png'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    # w = QWidget()
    # w.resize(1000, 500)
    # w.move(1500, 300)
    # w.setWindowTitle('Simple')
    # w.show()
    sys.exit(app.exec_())
