from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from resource.UI.login_panel import Ui_Form


class LoginPanel(QWidget,Ui_Form):
  show_db_panel_signal = pyqtSignal()

  def __init__(self,parent=None,*args,**kwargs):
    super().__init__(parent,*args,**kwargs)
    self.init()

  def init(self):
    self.setupUi(self)  # 读取UI
    self.getData()  # 获取数据
    self.run()  # 读取业务逻辑

  def getData(self):
    pass

  def run(self):
    pass


  def show_db_panel(self):
    self.show_db_panel_signal.emit()
    self.hide()

