from PyQt5.QtCore import pyqtSignal, Qt, QSettings, QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QApplication
from resource.UI.db_panel import Ui_Form
from common.qfTools import SyncRequestTool


class DbPanel(QWidget, Ui_Form):
  # 登陆页面显示信号
  show_login_panel_signal = pyqtSignal()
  # 测试连接结束信号
  connectionIsReady = pyqtSignal()

  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.init()

  def init(self):
    self.setupUi(self)  # 读取UI
    self.getData()  # 获取数据
    self.run()  # 读取业务逻辑

  def getConfigFile(self, setting):
    pass

  def getData(self):
    pass

  def run(self):
    self.settingFile = QSettings("config.ini", QSettings.IniFormat)
    self.settingRegedit = QSettings("yqfsoft", "restaurant")

    self.server = self.settingFile.value('server/server')
    self.db_panel_server_cb.setCurrentText(self.server)
    self.db_panel_server_cb.lineEdit().selectAll()
    self.port = self.settingFile.value('server/port')
    self.db_panel_port_le.setText(self.port)

    self.serverList: set = self.settingRegedit.value('server_list')

    self.connectionIsReady.connect(self.save_item_to_server_list)
    # 验证
    # 设置端口范围 1-65535
    pattern = QRegExp('^([1-9]|[1-9]\\d{3}|[1-6][0-5][0-5][0-3][0-5])$')
    portValidator = QRegExpValidator(pattern)
    self.db_panel_port_le.setValidator(portValidator)

  # 槽函数
  # 点击连接按钮的操作
  def db_connect(self):
    self.db_panel_yes_btn.setDisabled(True)
    self.checkConnection()

  # 点击测试按钮的操作
  def db_test(self):
    self.db_panel_test_btn.setDisabled(True)
    self.checkConnection()

  # 服务器地址改变
  def server_changed(self, server):
    self.server = server

  # 端口改变
  def port_changed(self, port):
    self.port = port

  # 服务器检测
  def checkConnection(self):
    url = SyncRequestTool.getServerUrl(self.server, self.port)

  def display_state(self, state: bool):
    if state:
      self.db_panel_conn_lab.setText("成功")
      self.connectionIsReady.emit()
      print("成功")
    else:
      self.db_panel_conn_lab.setText("失败")
      print("失败")
    self.thread_finish()

  def thread_finish(self):
    self.db_panel_test_btn.setDisabled(False)
    self.db_panel_yes_btn.setDisabled(False)

  def save_item_to_server_list(self):
    saveItem = {"server": self.server, "port": self.port}
    self.serverList.add(saveItem)
    self.settingRegedit.setValue("server_list", self.serverList)

  # 显示登陆界面
  def show_login_panel(self):
    self.show_login_panel_signal.emit()

  # 热键
  def keyPressEvent(self, event):
    super().keyPressEvent(event)
    if event.key() == Qt.Key_F1 and QApplication.keyboardModifiers() == Qt.ControlModifier:
      self.db_connect()
