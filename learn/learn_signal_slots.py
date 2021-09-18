#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import (QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QGridLayout, QLabel, QPushButton, QMainWindow)


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.c = Communicate()
        self.text1 = "x: {0},  y: {1}".format(0, 0)
        self.label = QLabel(self.text1, self)
        self.init_ui5()

    def init_ui(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

    def init_ui2(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def init_ui3(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)

    def init_ui4(self):
        btn1 = QPushButton("Button 1", self)
        btn1.setText("Button 1")
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.setText("Button 2")
        btn2.move(150, 50)

        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def init_ui5(self):
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
