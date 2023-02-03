import PyQt5
import requests
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PIL import Image, ImageOps, ImageFilter
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QImage
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('pyqt_design.ui', self)
        pixmap = QPixmap("Map.png")
        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())
        self.start.clicked.connect(self.tart)

    def tart(self):
        try:
            coord1 = float(self.coord1.text())
        except ValueError:
            coord1 = 0.0
        try:
            coord2 = float(self.coord2.text())
        except ValueError:
            coord2 = 0.0
        image = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&z=12&size=450,450&l=map")
        out = open("Map.png", "wb")
        out.write(image.content)
        out.close()
        pixmap = QPixmap("Map.png")
        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())