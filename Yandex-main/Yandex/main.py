import PyQt5
import requests
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


    
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.z = 5
        uic.loadUi('Yandex\\pyqt_design.ui', self)
        pixmap = QPixmap("Map.png")
        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())
        self.start.clicked.connect(self.button)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            if self.z < 12:
                self.z += 1
                self.button()
        if event.key() == QtCore.Qt.Key_PageDown:
            if self.z > 1:
                self.z -= 1
                self.button()
        event.accept()

    def button(self):
        try:
            self.coord12 = float(self.coord1.text())
        except ValueError:
            self.coord12 = 0.0
        try:
            self.coord22 = float(self.coord2.text())
        except ValueError:
            self.coord22 = 0.0
        self.tart(self.coord12, self.coord22)
    def tart(self, coord1, coord2):
        image = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&z={self.z}&size=450,450&l=map")
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