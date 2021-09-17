#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, \
    QAction, qApp, QMenu, QTextEdit
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


class Example2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.too_bar = self.addToolBar('Exit')
        self.init_ui()

    def toggle_menu(self, status):
        if status:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def init_ui(self):
        exit_act = QAction(QIcon('C:/Document/Temporary/exit_PNG18.png'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(qApp.quit)

        self.too_bar.addAction(exit_act)

        view_sta_act = QAction('View statusbar', self)
        view_sta_act.setCheckable(True)
        view_sta_act.setStatusTip('View statusbar')
        view_sta_act.setChecked(True)
        view_sta_act.triggered.connect(self.toggle_menu)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        view_menu = menu_bar.addMenu('View')

        view_menu.addAction(view_sta_act)

        imp_menu = QMenu('Import', self)
        imp_act = QAction('Import mail', self)
        imp_menu.addAction(imp_act)

        new_act = QAction('New', self)
        file_menu.addAction(new_act)
        file_menu.addMenu(imp_menu)

        file_menu.addAction(exit_act)

        self.statusBar().showMessage('Ready')
        self.setGeometry(1000, 300, 1000, 220)
        self.setWindowTitle('Statusbar')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def contextMenuEvent(self, event):

        c_menu = QMenu(self)

        new_act = c_menu.addAction('New')
        opn_act = c_menu.addAction('Open')
        quit_act = c_menu.addAction('Quit')
        action = c_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_act:
            qApp.quit()


class Example3(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)

        exit_act = QAction(QIcon('C:/Document/Temporary/exit_PNG18.png'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')

def



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = Example()
    # ex = Example2()
    ex = Example3()
    # w = QWidget()
    # w.resize(1000, 500)
    # w.move(1500, 300)
    # w.setWindowTitle('Simple')
    # w.show()
    sys.exit(app.exec_())
