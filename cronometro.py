#Cronometro

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt
from sympy.physics.units import hours, milliseconds
from base_page import BasePage

class stopWatch(BasePage):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cronometro")
        self.time = QTime(0, 0, 0, 0)
        self.timeLabel = QLabel("00:00:00")
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)

        self.timeLabel.setAlignment(Qt.AlignCenter)
        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        vbox.addWidget(self.criarBotaoVoltar())

        self.setStyleSheet("""
          QPushButton, QLabel{
            font-size: 30px;
            padding:20px;
            font-weight:bold;
            font-family: calibri;
          }
          QLabel{
            font-size:120px;
            background-color: skyblue;
            border-radius: 20px;
          }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.updateDisplay)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.timeLabel.setText(self.formatTime(self.time))

    def formatTime(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec()
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

    def updateDisplay(self):
        self.time = self.time.addMSecs(10)
        self.timeLabel.setText(self.formatTime(self.time))
