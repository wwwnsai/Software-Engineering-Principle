import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Github Drawing")
        self.rabbit = QPixmap("Lab5/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([
            QPoint(70,100), QPoint(100,110),
            QPoint(130,100), QPoint(100,150),
        ])

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 360 * 16)

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing2")
        self.rabbit = QPixmap("Lab5/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPie(50, 100, 100, 100, 0, 45 * 16)

        p.setPen(QColor(0, 127, 0))
        p.drawLine(100, 150, 55, 200)
        p.drawLine(100, 150, 145, 200)

        p.setPen(QColor(255, 0, 0))
        p.setBrush(QColor(255, 0, 0))
        p.drawPie(30, 200, 50, 50, 0, 360 * 16)
        p.drawPie(120, 200, 50, 50, 0, 360 * 16)

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Github Drawing 3")
        self.rabbit = QPixmap("lab4/images/rabbit.png")
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100), QPoint(100,130),
            QPoint(130,100), QPoint(100,150)
        ])
        
        p.setPen(QColor(230,191,0))
        p.setBrush(QColor(230,191,0))
        p.drawPie(50,150,100,100,0,180 *16)
        
        p.drawPolygon(
            [QPoint(50,200), QPoint(150,200), QPoint(150,350), QPoint(50,350)]
        )
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()
        
def main():
    app = QApplication(sys.argv)
    w1 = simple_drawing_window1()
    w2 = Simple_drawing_window2()
    w3 = Simple_drawing_window3()
    w1.show()
    w2.show()
    w3.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())