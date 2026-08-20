from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal

class BasePage(QWidget):

    voltarMenu = pyqtSignal()
    def criarBotaoVoltar(self, texto="Voltar ao Menu"):
        botao = QPushButton(texto)
        botao.clicked.connect(self.voltarMenu.emit)
        return botao
