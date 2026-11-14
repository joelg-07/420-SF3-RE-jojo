from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout, QWidget


class Equation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Equation au hazard")

        self.bouton = QPushButton(text="Bouton1")
        self.bouton.pressed.connect(self.handle_button_ok)

        self.libelle = QLabel("Cliquez pour une équation")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.libelle)
        main_layout.addWidget(self.bouton)

        main_container = QWidget()
        main_container.setLayout(main_layout)
        self.setCentralWidget(main_container)

    def handle_button_ok(self):
        print("click!")


# Création de l'application
app = QApplication()
# Creation de la fenêtre (la classe ci-haut)
Equation = Equation()
Equation.show()
# execution
app.exec()
