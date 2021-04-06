from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit
from common.tools import RequestTools
from threading import Thread
from common.threadTools import TimeThread
class MainWindow(QWidget):
  def __init__(self,parent=None,*args,**kwargs):
    super().__init__(parent,*args,**kwargs)
    self.resize(400,400)
    self.btn = QPushButton(self)
    self.btn.resize(60,40)
    self.btn.move(340,360)
    self.btn.setText("测试")
    self.te = QTextEdit(self)
    self.te.resize(400,340)

    self.timeTd = TimeThread()
    self.timeTd.start()

    self.btn.clicked.connect(self.display_time)
    self.timeTd.show_time_signal.connect(self.test)

  def display_time(self,time):
    self.te.setPlainText(time)


if __name__ == '__main__':
  import sys
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec_()