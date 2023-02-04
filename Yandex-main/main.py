import PyQt5
import requests
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


    
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.z = 12
        uic.loadUi('pyqt_design.ui', self)
        pixmap = QPixmap("Map.png")
        self.coord12 = 36.241424
        self.coord22 = 51.730848
        self.coord1.setText(str(self.coord12))
        self.coord2.setText(str(self.coord22))
        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())
        self.start.clicked.connect(self.button)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            if self.z < 12:
                self.z += 1
        if event.key() == QtCore.Qt.Key_PageDown:
            if self.z > 1:
                self.z -= 1
        if event.key() == QtCore.Qt.Key_D:
            if self.coord12 <= 179.95:
                self.coord1.setText(str(round(self.coord12 + 0.05, 5)))
        if event.key() == QtCore.Qt.Key_S:
            if self.coord22 >= -88.95:
                self.coord2.setText(str(round(self.coord22 - 0.05, 5)))
        if event.key() == QtCore.Qt.Key_A:
            if self.coord12 >= -179.95:
                self.coord1.setText(str(round(self.coord12 - 0.05, 5)))
        if event.key() == QtCore.Qt.Key_W:
            if self.coord22 <= 88.95:
                self.coord2.setText(str(round(self.coord22 + 0.05, 5)))
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
        if self.coord12 >= 179.95:
            self.coord12 = 180
        if self.coord12 <= -179.95:
            self.coord12 = -180
        if self.coord22 <= -88.95:
            self.coord22 = -85
        if self.coord22 >= 88.95:
            self.coord22 = 85
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
    ex.button()
    ex.show()
    sys.exit(app.exec_())