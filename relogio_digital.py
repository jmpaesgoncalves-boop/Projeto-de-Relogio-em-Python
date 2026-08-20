#Relógio Digital:

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton)
from PyQt5.QtCore import QTimer, QTime, Qt, pyqtSignal
from base_page import BasePage

class digitalClock(BasePage):
    abrirCron = pyqtSignal()
    abrirAlarm = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relógio Digital")
        self.timeLabel = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)

        self.botaoCron= QPushButton("Cronômetro")
        self.botaoAlarm= QPushButton("Alarme")
        self.botaoCron.clicked.connect(self.abrirCron.emit)
        self.botaoAlarm.clicked.connect(self.abrirAlarm.emit)
        hbox = QHBoxLayout()
        hbox.addWidget(self.botaoCron)
        hbox.addWidget(self.botaoAlarm)
        vbox.addLayout(hbox)
        self.setLayout(vbox)


        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("font-size: 150px;"
                                     "font-family: Arial;"
                                     "color: hsl(136, 89%, 49%);")
        self.setStyleSheet("""
          QWidget{
            background-color: black;           
          }
          QPushButton{
            background-color: lightgray;      
            color: black;
            font-size: 20px;
            padding: 10px;
            border-radius: 8px;          
          } 
        """)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()
        self.timeLabel.raise_()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timeLabel.setText(current_time)
