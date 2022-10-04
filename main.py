import sys

from PyQt6.QtCore import QSize, QTimer, QRect, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
QMainWindow, QApplication, QFrame, QLabel
)


class MainWindow(QMainWindow):

    """The class describes the main application window"""

    def __init__(self):

        """Contains settings of the main window and widgets"""

        super(MainWindow, self).__init__()

        # window size
        self.setMinimumSize(QSize(620, 620))
        self.setMaximumSize(QSize(620, 620))

        # external content container
        self.container = QFrame()

        self.circle_bg = QFrame(self.container)
        self.circle_bg.setMinimumSize(QSize(620, 620))
        self.circle_bg.setMaximumSize(QSize(620, 620))
        self.circle_bg.setProperty("class", "circle_bg")

        self.header = QFrame(self.circle_bg)
        self.header.setGeometry(QRect(0, 0, 620, 270))
        self.header.setProperty("class", "header")

        self.font_time = QFont()
        self.font_time.setFamily("Segoe UI")
        self.font_time.setPointSize(75)

        self.time_label = QLabel(self.header)
        #self.time_label.setGeometry(QRect(195, 47, 290, 130))
        self.time_label.setFont(self.font_time)
        self.time_label.setText('00:00')
        self.time_label.setProperty("class", "time_label")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.alarm_clock_area = QFrame(self.circle_bg)
        self.alarm_clock_area.setGeometry(QRect(0, 270, 620, 350))
        self.alarm_clock_area.setProperty("class", "alarm_clock_area")



        self.setCentralWidget(self.container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    with open("styles.css", "r") as file:
        app.setStyleSheet(file.read())
    window.show()

    app.exec()
