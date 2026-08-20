import sys

from PyQt5.QtWidgets import QMainWindow,QStackedWidget, QApplication
from PyQt5.QtGui import QIcon
from relogio_digital import digitalClock
from cronometro import stopWatch
from AlarmeUI import Alarm

class JanelaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relógio")
        self.setWindowIcon(QIcon("assets/iconeRelogio.jpg"))
        self.setGeometry(500, 250, 500, 450)

        self.relogio = digitalClock()
        self.cronometro = stopWatch()
        self.alarme = Alarm()

        self.stack= QStackedWidget()
        self.stack.addWidget(self.relogio)
        self.stack.addWidget(self.cronometro)
        self.stack.addWidget(self.alarme)

        self.setCentralWidget(self.stack)

        self.relogio.abrirCron.connect(
            lambda: self.stack.setCurrentWidget(self.cronometro)
        )
        self.relogio.abrirAlarm.connect(
            lambda: self.stack.setCurrentWidget(self.alarme)
        )

        self.cronometro.voltarMenu.connect(
            lambda: self.stack.setCurrentWidget(self.relogio)
        )
        self.alarme.voltarMenu.connect(
            lambda: self.stack.setCurrentWidget(self.relogio)
        )

        self.stack.setCurrentWidget(self.relogio)

if __name__=="__main__":
    app = QApplication(sys.argv)
    janela=JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())