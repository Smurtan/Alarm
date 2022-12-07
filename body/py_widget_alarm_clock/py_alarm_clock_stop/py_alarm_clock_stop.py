from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class PyAlarmClockStop(QDialog):
    def __init__(
            self,
            alarm_clock=None,
            sound=None
    ):
        super().__init__(alarm_clock)

        self._alarm_clock = alarm_clock
        self.sound = sound

        self.stop_button = QPushButton()
        self.stop_button.setText("Stop")
        self.stop_button.clicked.connect(self.stopMusic)

        try:
            self.sound.play()
        except AttributeError:
            print('Вы потеряли песню!')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stop_button)
        self.setLayout(self.layout)

    def stopMusic(self) -> None:
        self.sound.stop()
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = PyAlarmClockStop()
    window.show()
    app.exec()