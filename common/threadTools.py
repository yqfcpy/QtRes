from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
import time


class TimeThread(QThread):
  show_time_signal = pyqtSignal(QDateTime)

  def __init__(self):
    super().__init__()

  def run(self):
    while True:
      current_time = QDateTime().currentDateTime()
      self.show_time_signal.emit(current_time)
      time.sleep(1)
