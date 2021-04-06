from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from resource.UI.login_panel import Ui_Form
from resource.common.tools import CommonTools


class LoginPanel(QWidget,Ui_Form):
  show_db_panel_signal = pyqtSignal()

  def __init__(self,parent=None,*args,**kwargs):
    super().__init__(parent,*args,**kwargs)
    self.init()

  def init(self):
    self.setupUi(self)  # 读取UI
    self.loadConfig() # 读取配置文件
    self.getData()  # 获取数据
    self.loadLogicCode()  # 读取业务逻辑
    self.loadSignal()  # 监听信号和槽

  def loadConfig(self):
    pass

  def loadConfig(self):
    self.settingFile = CommonTools.loadConfigFile()

  def getData(self):
    pass

  def loadLogicCode(self):
    pass

  def loadSignal(self):
    pass

  def show_db_panel(self):
    self.show_db_panel_signal.emit()
    self.hide()

