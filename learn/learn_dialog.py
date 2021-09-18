#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication, QHBoxLayout, QColorDialog, QFrame, QFontDialog, QLabel,
                             QVBoxLayout, QSizePolicy, QFileDialog, QAction, QTextEdit, QMainWindow)
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        ''' 
        self.lbl = QLabel('Knowledge only matters', self)
        self.btn = QPushButton('Dialog', self)
        self.frm = QFrame(self)

        self.layout = QHBoxLayout()
        
            self.le = QLineEdit(self)
            self.btn = QPushButton('Dialog', self)
        '''
        self.init_ui4()

    '''
    def init_ui1(self):

        self.btn.clicked.connect(self.show_dialog)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.le)
        self.setLayout(self.layout)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
    '''

    def show_dialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))

    def init_ui2(self):

        col = QColor(0, 0, 0)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.frm)
        self.setLayout(self.layout)

        self.btn.clicked.connect(self.show_dialog2)

        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def show_dialog2(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())

    def init_ui3(self):

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.show_dialog3)

        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def show_dialog3(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def init_ui4(self):

        self.setCentralWidget(self.textEdit)
        self.statusBar()

        open_file = QAction(QIcon('C:/Document/NXU/HTML/NXUHelper/Pics/NXU.png'), 'Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open new File')
        open_file.triggered.connect(self.show_dialog4)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def show_dialog4(self):

        f_name = QFileDialog.getOpenFileName(self, 'Open file', "/")

        if f_name[0]:
            f = open(f_name[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
