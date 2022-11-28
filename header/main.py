from PyQt6.QtCore import *
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *

from header.button import PyCloseButton


class Ui_Header:
    def __init__(self, parent):
        self.header = QFrame(parent)
        self.header.setGeometry(QRect(0, 0, 620, 230))
        self.header.setProperty("class", "header")

        self.close_button = PyCloseButton(self.header)
        self.close_button.setGeometry(137, 0, 340, 45)

        self.font_time = QFont()
        self.font_time.setFamily("Segoe UI")
        self.font_time.setPointSize(75)

        self.time_label = QLabel("00:00", self.header)
        self.time_label.setGeometry(QRect(190, 80, 240, 85))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.time_label.setFont(self.font_time)
        self.time_label.setProperty("class", "time_label")
