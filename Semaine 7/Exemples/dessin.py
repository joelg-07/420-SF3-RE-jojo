from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPainter, QPixmap, QColorConstants, QPen, QBrush, QColor, QPainterPath
from PySide6.QtCore import QSize, Qt, QRectF


class QPainterEx(QMainWindow):

    def __init__(self):
        super().__init__()

        self.etiquette_centrale = QLabel()
        # Création d'un canevas d'une largeur de 800 pixels et d'une hauteur de 600 pixels
        canevas = QPixmap(QSize(800, 600))
        # Remplir le canevas d'une couleur
        # QColorConstants contient un ensemble de couleurs prédéfinies
        canevas.fill(QColorConstants.White)

        self.etiquette_centrale.setPixmap(canevas)
        self.setCentralWidget(self.etiquette_centrale)
        self.dessiner()

    def dessiner (self):
        canevas = self.etiquette_centrale.pixmap()
        painter = QPainter(canevas)
        crayon = QPen()
        crayon.setWidth(30)
        pinceau = QBrush()
        pinceau.setStyle(Qt.BrushStyle.SolidPattern)
        pinceau.setColor(QColorConstants.DarkGray)
        crayon.setBrush(pinceau)
        painter.setPen(crayon)

        crayon2 = QPen()


        yeuxd = QRectF(300.0, 300.0, 20.2, 10.0 )
        yeuxg = QRectF(500.0, 300.0, 20.2, 10.0 )
        forme_visage = QRectF(200.0,150.0, 500.0,100.0)


        painter.drawRect(yeuxd)
        painter.drawRect(yeuxg)
        painter.drawEllipse(forme_visage)



        self.etiquette_centrale.setPixmap(canevas)











app = QApplication()
qp = QPainterEx()
qp.show()
app.exec()


