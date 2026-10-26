from serie import Serie
from PySide6.QtWidgets import QApplication, QLabel, QComboBox, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QGridLayout
from PySide6.QtGui import QIcon

class GestionnaireSeries(QMainWindow):

    def __init__(self):

        super().__init__()


        self.serie : list[Serie] = Serie.charger_donnee()
        self.setWindowTitle("Gestion série 2026")
        self.setWindowIcon(QIcon("img.png"))

        self.widget_central = QWidget
        self.depositon_principale = QVBoxLayout
        self.widget_central.setLayout(self.depositon_principale)
        self.setCentralWidget(self.widget_central)


        self.depositon_selection = QVBoxLayout
        self.libele_selection = QLabel("Série: ")
        self.depositon_selection.addWidget(self.libele_selection)
        self.liste_selection = QComboBox

        for serie in self.serie:

            self.liste_selection.addItem(serie.nom, serie)

        self.depositon_edition = QGridLayout()
        self.libelle_nom = QLabel("nom: ")
        self.input_nom = QLineEdit
        self.libelle_annee_sortie = QLabel("Année de sortie:")
        self.input_annee_soritie = QLineEdit
        self.nb_saison = QLabel("Nb de saisons:")
        self.input_nb_saison = QLineEdit

        self.depositon_edition.addWidget(self.libele_selection, 0, 0)
        self.depositon_edition.addWidget(self.input_nom, 0, 1)
        self.depositon_edition.addWidget(self.libelle_annee_sortie, 1, 0 )
        self.depositon_edition.addWidget(self.input_annee_soritie, 1, 1 )
        self.depositon_edition.addWidget(self.input_nb_saison, 1, 1 )







app = QApplication
gs = GestionnaireSeries
gs.show()
app.exec()