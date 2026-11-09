from PySide6.QtCore import QDate
from PySide6.QtWidgets import QGridLayout, QApplication, QMainWindow, QPushButton, QWidget, QLabel, \
    QHBoxLayout, QVBoxLayout, QMenuBar, QMenu, QCalendarWidget
from PySide6.QtGui import QPixmap, QAction
class fenetre (QMainWindow):
    def __init__(self):
        super().__init__()

        fenetre = QMainWindow()
        self.setCentralWidget(fenetre)
        self.setWindowTitle("Filtre radioctif 2000")
        icone = QPixmap("img.png")
        self.setWindowIcon(icone)
        disposotion = QVBoxLayout()
        self.setLayout(disposotion)

        self.barre_menu = QMenuBar()
        self.menu = QMenu("Fichier")
        self.barre_menu.addMenu(self.menu)
        self.setMenuBar(self.barre_menu)

        self.action_exporter = QAction(parent=self)
        self.action_exporter.setText("Exporter graphique")
        self.action_exporter.triggered.connect(self.exporter)
        self.menu.addAction(self.action_exporter)

        self.menu.addSeparator()

        self.action_quitter = QAction(parent=self)
        self.action_quitter.setText("Quitter")
        self.action_quitter.triggered.connect(self.quitter)
        self.menu.addAction(self.action_quitter)

        calendrier = QCalendarWidget()

        disposotion.addWidget(calendrier)





    def quitter(self):
        pass

    def exporter(self):
            pass

if __name__ == "__main__":
    app = QApplication()
    fp = fenetre()
    fp.show()
    app.exec()
