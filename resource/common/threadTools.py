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

# class RequestThread(QThread):
#   send_request_signal = pyqtSignal(bool)
#
#   def __init__(self,url: str):
#     super().__init__()
#     self.url = url
#
#   def run(self):
#     # try except else组合 try 会出问题的代码 except 找到问题 else出现问题进入else里写入的方法
#     try:
#       res = RequestTools.isServerConnected(self.url)
#     except:
#       print("线程出错")
#     else:
#       self.send_request_signal.emit(res)
