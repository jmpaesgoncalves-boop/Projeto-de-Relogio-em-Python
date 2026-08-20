# Alarme:

import sys
import pygame
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QRadioButton, QButtonGroup, QLineEdit, QVBoxLayout
)
from PyQt5.QtCore import QTimer, QTime
from base_page import BasePage

class Alarm(BasePage):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarme")

        self.soundFile1 = "assets/Would It Matter - Rose Campbell.mp3"
        self.soundFile2 = "assets/Wildfire - Jessie Villa.mp3"
        self.soundFile3 = "assets/Wooden Train Whistle.mp3"

        self.sound = self.soundFile3
        self.alarmTime = None

        self.initUI()

    def initUI(self):

        self.labelMusic = QLabel("Escolha a música de seu alarme:")

        self.radio1 = QRadioButton("1. Would It Matter - Rose Campbell")
        self.radio2 = QRadioButton("2. Wildfire - Jessie Villa")
        self.radio3 = QRadioButton("3. Apito de Trem - (Padrão)")

        self.radio3.setChecked(True)

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.radio1)
        self.buttonGroup.addButton(self.radio2)
        self.buttonGroup.addButton(self.radio3)

        self.labelTime = QLabel(
            "Coloque o seu alarme no formato (HH:MM:SS):"
        )

        self.timeInput = QLineEdit()
        self.timeInput.setPlaceholderText("Ex.: 07:30:00")

        self.button = QPushButton("Definir Alarme")

        self.status = QLabel("")

        layout = QVBoxLayout()

        layout.addWidget(self.labelMusic)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)

        layout.addWidget(self.labelTime)
        layout.addWidget(self.timeInput)

        layout.addWidget(self.button)
        layout.addWidget(self.status)
        layout.addWidget(self.criarBotaoVoltar())

        self.setLayout(layout)

        self.button.clicked.connect(self.set_alarm)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_alarm)

    def set_alarm(self):

        if self.radio1.isChecked():
            self.sound = self.soundFile1
            self.status.setText("'Would It Matter' escolhida")

        elif self.radio2.isChecked():
            self.sound = self.soundFile2
            self.status.setText("'Wildfire' escolhida")

        elif self.radio3.isChecked():
            self.sound = self.soundFile3
            self.status.setText("'Apito' escolhido")

        alarm_time = self.timeInput.text()

        try:
            self.alarmTime = QTime.fromString(alarm_time, "HH:mm:ss")

            if not self.alarmTime.isValid():
                raise ValueError

        except ValueError:
            self.status.setText(
                "Horário inválido. Use o formato HH:MM:SS."
            )
            return

        self.status.setText(
            f"Alarme posto para as {alarm_time}"
        )

        self.timer.start(1000)

    def check_alarm(self):

        current_time = QTime.currentTime()

        if current_time.toString("HH:mm:ss") == \
                self.alarmTime.toString("HH:mm:ss"):
            self.status.setText("ESTÁ NA HORA!")

            pygame.mixer.init()
            pygame.mixer.music.load(self.sound)
            pygame.mixer.music.play()

            self.timer.stop()
