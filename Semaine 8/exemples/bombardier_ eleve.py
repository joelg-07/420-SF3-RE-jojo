from PySide6.QtCore import QObject, QVariantAnimation, QPointF, QEasingCurve, Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QApplication, QLabel, QVBoxLayout



class Fenetre_jeux (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animation d'un pixmap avec un easing curve")
        self.scene = QGraphicsScene(0, 0, 800, 600, self)
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)
        self.timer = QTimer()
        self.timer.timeout.connect(self.mise_a_jour)
        self.timer.setInterval(70)
        self.timer.start()

        image_avion = QPixmap("images/airplane.png")
        image_avion = image_avion.scaled(128, 64)
        self.avion = QGraphicsPixmapItem(image_avion)
        x,y = 0,30
        self.avion.setPos(QPointF(x,y))
        self.scene.addItem(self.avion)

        # objectif de tir
        image_avion = QPixmap("images/target.png")
        image_target = image_avion.scaled(128, 100)
        self.target = QGraphicsPixmapItem(image_target)
        self.target.setPos(QPointF(300, 500))
        self.scene.addItem(self.target)

        #bombe
        image_bombe = QPixmap("images/nuclear-bomb.png")
        image_bombe = image_bombe.scaled(64, 64)
        self.bombe = QGraphicsPixmapItem(image_bombe)
        self.bombe.setPos(QPointF(0, 30))
        self.scene.addItem(self.bombe)

    def mise_a_jour(self):
            self.avion.pos().setX(self.avion.pos().x() + 20)

            self.bombe.pos().setX(self.bombe.pos().x() + 10)
            self.avion.pos().setY(self.bombe.pos().y() + 20)


if __name__ == "__main__":
    app = QApplication()
    fa = Fenetre_jeux()
    fa.show()
    app.exec()











