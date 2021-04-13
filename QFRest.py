from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QSplashScreen
from Db_Panel import DbPanel
from Login_Panel import LoginPanel
from common.requestTools import SyncRequest
import sys



# 配置文件的内容转换成字典
def loadConfigFile(configFile:str = "config.ini", *args,**kwargs):
  # 把配置文件中的变量赋值给传经来的窗口
  pass

# 判定服务器连接界面和登录界面谁先显示
def showInitPanel(dbPanel: QWidget, loginPanel: QWidget, configFile:str = "config.ini"):
  url = SyncRequest.getServerUrlFromConfig(configFile)
  isReady = SyncRequest.isServerConnected(url)
  firstWindow = None
  if isReady:
    firstWindow = loginPanel
  else:
    firstWindow = dbPanel
  return firstWindow

# 程序入口文件
if __name__ == '__main__':

  app = QApplication(sys.argv)
  splash = QSplashScreen(QPixmap("./resource/img/systemicon/splash.jpg"))
  splash.show()
  app.processEvents()
  splash.showMessage("loading style", Qt.AlignCenter | Qt.AlignBottom, Qt.red)
  print("加载样式文件")
  splash.showMessage("loading language", Qt.AlignCenter | Qt.AlignBottom, Qt.red)
  print("加载多国语言")
  splash.showMessage("loading config file", Qt.AlignCenter | Qt.AlignBottom, Qt.red)
  print("加载配置文件")
  splash.showMessage("loading UI file", Qt.AlignCenter | Qt.AlignBottom, Qt.red)
  print("实例化界面")
  dbPanel = DbPanel()
  loginPanel = LoginPanel()
  splash.showMessage("Start connecting to the server", Qt.AlignCenter | Qt.AlignBottom, Qt.red)
  print("连接服务器")
  window = showInitPanel(dbPanel,loginPanel)


  splash.finish(window)
  window.show()


  # 信号
  # 显示登陆页面的信号
  dbPanel.show_login_panel_signal.connect(loginPanel.show)
  loginPanel.show_db_panel_signal.connect(dbPanel.show)
  # 关闭图片 加载主程序

  sys.exit(app.exec_())