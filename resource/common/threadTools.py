import requests
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
import time

class TimeThread(QThread):
  show_time_signal = pyqtSignal(str)

  def __init__(self):
    super().__init__()

  def run(self):
    while True:
      timeData = QDateTime().currentDateTime()
      current_time = timeData.toString("yyyy-MM-dd hh:mm:ss")
      self.show_time_signal.emit(str(current_time))
      time.sleep(1)

class RequestThread(QThread):
  send_request_signal = pyqtSignal(int)
  end_request_signal = pyqtSignal()

  def __init__(self,url):
    super().__init__()
    self.url = url

  def run(self):
    # try except else组合 try 会出问题的代码 except 找到问题 else出现问题进入else里写入的方法
    try:
      res = requests.get(self.url)
    except:
      print("线程出错")
      self.end_request_signal.emit()
    else:
      self.send_request_signal.emit(res.status_code)