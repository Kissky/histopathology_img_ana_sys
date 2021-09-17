#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, \
    QLineEdit, QTextEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        lbl1 = QLabel('zet_code', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


class Example2(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui3()

    def init_ui(self):

        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")

        h_box = QHBoxLayout()
        h_box.addStretch(1)
        h_box.addWidget(ok_button)
        h_box.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(h_box)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def init_ui2(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            print(position)
            print(*position)
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def init_ui3(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_edit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())
