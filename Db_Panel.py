from PyQt5.QtCore import pyqtSignal, Qt, QThread
from PyQt5.QtWidgets import QWidget, QApplication
from resource.UI.db_panel import Ui_Form
from resource.common.tools import CommonTools, RequestTools
from resource.common.threadTools import RequestThread
import asyncio, requests


class DbPanel(QWidget,Ui_Form):
  # 登陆页面显示信号
  show_login_panel_signal = pyqtSignal()
  # 数据库连接成功信号
  getConnection_signal = pyqtSignal()

  def __init__(self,parent=None,*args,**kwargs):
    super().__init__(parent,*args,**kwargs)
    self.init()

  def init(self):
    self.setupUi(self) # 读取UI
    self.loadConfig() # 读取配置文件
    self.getData() # 获取数据
    self.loadLogicCode() # 读取业务逻辑

  def loadConfig(self):
    self.settingFile = CommonTools.loadConfigFile()

  def getData(self):
    pass

  def loadLogicCode(self):
    server = self.settingFile.value('server/server')
    self.db_panel_server_cb.setCurrentText(server)
    self.db_panel_server_cb.lineEdit().selectAll()
    port=self.settingFile.value('server/port')
    self.db_panel_port_le.setText(port)

  # 槽函数
  # 点击连接按钮的操作
  def db_connect(self):
    try:
      flag = RequestTools.getConnectionState()
    except:
      flag = False
    if flag:
      self.hide()
      self.show_login_panel()


  # 点击测试按钮的操作
  def db_test(self):
    self.db_panel_test_btn.setDisabled(True)
    server = self.db_panel_server_cb.currentText()
    port = self.db_panel_port_le.text()
    if port == "":
      url = "http://" + server
    else:
      url = "http://" + server + ":" + port
    # url = "http://localhost:18080"
    print(url)
    self.server_state = RequestThread(url)
    print("创建线程成功")
    self.server_state.send_request_signal.connect(self.display_state)
    self.server_state.end_request_signal.connect(self.reload_display_state)
    self.server_state.start()
    print("开启线程")

  def display_state(self,state):
    print("显示",state)
    if state == 200:
      self.db_panel_conn_lab.setText("成功")
      print("成功")
    else:
      self.db_panel_conn_lab.setText("失败")
      print("失败")
    self.db_panel_test_btn.setDisabled(False)

  def reload_display_state(self):
    self.db_panel_conn_lab.setText("失败")
    self.db_panel_test_btn.setDisabled(False)

  # 显示服务器状态
  def send_connection_request(self):
    res = requests.get("http://localhost:18080")
    self.server_state = res.status_code
    print(self.server_state)


  # 显示登陆界面
  def show_login_panel(self):
    self.show_login_panel_signal.emit()


  # 设置确定按钮不可用
  def ok_btn_disable(self,content):
    if content =="":
      self.db_panel_yes_btn.setDisabled(True)
    else:
      self.db_panel_yes_btn.setDisabled(False)

  # 热键
  def keyPressEvent(self, event):
    super().keyPressEvent(event)
    if event.key() == Qt.Key_F1 and QApplication.keyboardModifiers() == Qt.ControlModifier:
      self.db_connect()
