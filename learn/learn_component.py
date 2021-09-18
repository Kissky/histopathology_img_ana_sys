#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QFrame, QSlider, QLabel, QProgressBar, \
    QVBoxLayout, QCalendarWidget, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt, QBasicTimer, QDate
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.lbl = QLabel(self)
        '''     
        self.p_bar = QProgressBar(self)
        self.btn = QPushButton('Start', self)
        self.step = 0
        self.timer = QBasicTimer()
        self.label = QLabel(self)
        self.square = QFrame(self)
        self.col = QColor(0, 0, 0)
        '''
        self.init_ui6()

    ''' 
    def init_ui1(self):
    
    cb = QCheckBox('Show title', self)
    cb.move(20, 20)
    cb.toggle()
    cb.stateChanged.connect(self.change_title)
    
    self.setGeometry(300, 300, 250, 150)
    self.setWindowTitle('QCheckBox')
    self.show()
    
    def change_title(self, state):
    
    if state == Qt.Checked:
        self.setWindowTitle('QCheckBox')
    else:
        self.setWindowTitle(' ')
    
    def init_ui2(self):
    
    red_b = QPushButton('Red', self)
    red_b.setCheckable(True)
    red_b.move(10, 10)
    
    red_b.clicked[bool].connect(self.set_color)
    
    green_b = QPushButton('Green', self)
    green_b.setCheckable(True)
    green_b.move(10, 60)
    
    green_b.clicked[bool].connect(self.set_color)
    
    blue_b = QPushButton('Blue', self)
    blue_b.setCheckable(True)
    blue_b.move(10, 110)
    
    blue_b.clicked[bool].connect(self.set_color)
    
    self.square.setGeometry(150, 20, 100, 100)
    self.square.setStyleSheet("QWidget { background-color: %s }" %
                              self.col.name())
    
    self.setGeometry(300, 300, 280, 170)
    self.setWindowTitle('Toggle button')
    self.show()
    
    def set_color(self, pressed):
    
    source = self.sender()
    
    if pressed:
        val = 255
    else:
        val = 0
    
    if source.text() == "Red":
        self.col.setRed(val)
    elif source.text() == "Green":
        self.col.setGreen(val)
    else:
        self.col.setBlue(val)
    
    self.square.setStyleSheet("QFrame { background-color: %s }" %
                              self.col.name())
    
    def init_ui3(self):
    
    sld = QSlider(Qt.Horizontal, self)
    sld.setFocusPolicy(Qt.NoFocus)
    sld.setGeometry(30, 40, 100, 30)
    sld.valueChanged[int].connect(self.change_value)
    
    self.label.setPixmap(QPixmap('C:/Document/NXU/HTML/NXUHelper/Pics/NXU.png'))
    self.label.setGeometry(160, 40, 80, 30)
    
    self.setGeometry(300, 300, 280, 170)
    self.setWindowTitle('QSlider')
    self.show()
    
    def change_value(self, value):
    
    if value == 0:
        self.label.setPixmap(QPixmap('C:/Document/NXU/HTML/NXUHelper/Pics/NXU.png'))
    elif 0 < value <= 30:
        self.label.setPixmap(QPixmap('C:/Document/Temporary/exit_PNG18.png'))
    elif 30 < value < 80:
        self.label.setPixmap(QPixmap('C:/Document/NXU/HTML/NXUHelper/Pics/NXU.png'))
    else:
        self.label.setPixmap(QPixmap('C:/Document/Temporary/exit_PNG18.png'))
    
    def init_ui4(self):
    
    self.p_bar.setGeometry(30, 40, 200, 25)
    
    self.btn.move(40, 80)
    self.btn.clicked.connect(self.do_action)
    
    self.setGeometry(300, 300, 280, 170)
    self.setWindowTitle('QProgressBar')
    self.show()
    
    def timerEvent(self, e):
    
    if self.step >= 100:
        self.timer.stop()
        self.btn.setText('Finished')
        return
    
    self.step = self.step + 1
    self.p_bar.setValue(self.step)
    
    def do_action(self):
    
    if self.timer.isActive():
        self.timer.stop()
        self.btn.setText('Start')
    else:
        self.timer.start(100, self)
        self.btn.setText('Stop')
    '''

    def init_ui5(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(False)
        cal.clicked[QDate].connect(self.show_date)

        vbox.addWidget(cal)

        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def show_date(self, date):

        self.lbl.setText(date.toString())

    def init_ui6(self):
        h_box = QHBoxLayout(self)

        top_left = QFrame(self)
        top_left.setFrameShape(QFrame.StyledPanel)
        top_left.setMinimumSize(50, 50)

        top_right = QFrame(self)
        top_right.setFrameShape(QFrame.StyledPanel)
        top_right.setMinimumSize(50, 50)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        bottom.setMinimumSize(50, 50)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(top_left)
        splitter1.addWidget(top_right)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        h_box.addWidget(splitter2)
        self.setLayout(h_box)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

    def on_changed(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
