from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CircualProgressBar(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = QColor(10, 2, 15)
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.progress_color = QColor(10, 2, 15)
        self.enable_shadow = True

        self.resize(self.width, self.height)
    
    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)

        rect = QRect(0, 0, width, height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        pen = QPen()
        pen.setColor(self.progress_color)
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -180 * 16, -value * 16)

        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, str(self.value) + self.suffix)
        paint.end()

    def setValue(self, value):
        self.value = value
        self.update()
    
