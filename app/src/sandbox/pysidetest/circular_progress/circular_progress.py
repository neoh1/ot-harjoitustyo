from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class CircularProgress(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.value = 0
        self.width = 250
        self.height = 250
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x8BD149  # light green GBR
        self.max_value = 100  # 100% progress
        self.font_family = "Segoe UI"
        self.font_size = 24  #12
        self.suffix = "%"
        self.text_color = 0x8BD149

    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

        # default size
        self.resize(self.width, self.height)

    def set_value(self, vlue):
        self.value = value
        # re-render progress bar
        self.repaint()

    def paintEvent(self, event):
        # rendering widget
        # PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width  # -width makes sure line stays visible and isnt cut
        margin = self.progress_width / 2
        # link angle of progress bar with value hence divide by max_value 100
        value = self.value * 360 / self.max_value

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        # ADD ANTIALIASING TO SMOOTHEN PIXELATED EDGES
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)  # remove border
        paint.drawRect(rect)

        # WIDTH AND STYLE OF PROGRESS BAR
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        # Set ROUND CAP
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # CREATE ARC OF PROGRESS BAR
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value *
                      16)  # 360 ARK is equal to 360*16 in Qt  # -90*16

        # CREATE TEXT
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # CLOSE PAINTER
        paint.end()
