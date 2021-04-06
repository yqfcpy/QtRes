from PyQt5.QtCore import QTranslator
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QSplashScreen
from Db_Panel import DbPanel
from Login_Panel import LoginPanel
from resource.common.tools import RequestTools

# 程序入口文件
if __name__ == '__main__':
  import sys

  app = QApplication(sys.argv)

  dbPanel = DbPanel()
  loginPanel = LoginPanel()

  try:
    conn = RequestTools.getConnectionState()
  except:
    conn = False

  if conn:
    loginPanel.show()
  else:
    dbPanel.show()

  # 槽

  # 信号
  # 显示登陆页面的信号
  dbPanel.show_login_panel_signal.connect(loginPanel.show)
  loginPanel.show_db_panel_signal.connect(dbPanel.show)
  # 关闭图片 加载主程序

  sys.exit(app.exec_())
