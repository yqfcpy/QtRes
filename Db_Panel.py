from PyQt5.QtCore import pyqtSignal, Qt, QSettings, QRegExp
from PyQt5.QtWidgets import QWidget, QApplication
from resource.UI.db_panel import Ui_Form
from common.requestTools import SyncRequest, AsyncRequest
from common.regExpTools import RegExpValidator
from common import logger

log = logger.loggerConfig()

class DbPanel(QWidget, Ui_Form):
  # 登陆页面显示信号
  show_login_panel_signal = pyqtSignal()

  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.init()

  def init(self):
    self.setupUi(self)  # 读取UI
    self.run()  # 读取业务逻辑

  def run(self):
    self.setWindowTitle("服务器连接")
    self.settingFile = QSettings("config.ini", QSettings.IniFormat)
    self.settingRegedit = QSettings("yqfsoft", "restaurant")

    self.server = self.settingFile.value('server/server')
    self.db_panel_server_cb.setCurrentText(self.server)
    self.db_panel_server_cb.lineEdit().selectAll()
    self.port = self.settingFile.value('server/port')
    self.db_panel_port_le.setText(self.port)

    self.serverList: set = self.settingRegedit.value('server_list')

    # 验证
    # 设置端口范围 1-65535
    self.db_panel_port_le.setValidator(RegExpValidator.getPortValidator())



  # 槽函数
  # 点击连接按钮的操作
  def db_connect(self):
    self.db_panel_yes_btn.setDisabled(True)
    self.getTestConnection(1)

  # 点击测试按钮的操作
  def db_test(self):
    self.db_panel_test_btn.setDisabled(True)
    self.getTestConnection(2)

  # 服务器地址改变
  def server_changed(self, server):
    self.server = server

  # 端口改变
  def port_changed(self, port):
    self.port = port

  # 服务器检测 枚举 1是点击确定运行的方法 2是点击测试运行的方法
  def getTestConnection(self,runNum:int):
    url = SyncRequest.getServerUrl(self.server, self.port)
    log.info(url)
    self.request = AsyncRequest()
    res = self.request.get(url)
    if runNum == 1:
      self.request.getResult.connect(self.clickBtnYesToDo)
    else:
      self.request.getResult.connect(self.clickBtnTestToDo)

  def clickBtnYesToDo(self,state):
    log.info(state)
    if state['code'] != 0:
      self.db_panel_conn_lab.setText("成功")
      self.db_panel_conn_lab.setStyleSheet('color:green;')
      self.close()
      self.show_login_panel_signal.emit()
      log.info("成功")
    else:
      self.db_panel_conn_lab.setText("失败")
      self.db_panel_conn_lab.setStyleSheet('color:red;')
      log.info("失败")
    self.db_panel_yes_btn.setDisabled(False)


  def clickBtnTestToDo(self, state):
    log.info(state)
    if state['code'] != 0:
      self.db_panel_conn_lab.setText("成功")
      self.db_panel_conn_lab.setStyleSheet('color:green;')
      log.info("成功")
    else:
      self.db_panel_conn_lab.setText("失败")
      self.db_panel_conn_lab.setStyleSheet('color:red;')
      log.info("失败")
    self.db_panel_test_btn.setDisabled(False)

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
