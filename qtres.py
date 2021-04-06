from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation, QSettings
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class LoginWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.initUi()

  def initUi(self):
    self.getSystemSettings()
    self.setWindowTitle('我的第一个Qt程序')
    self.resize(500, 300)
    # 把label放到父类里 self就是父类 即主窗口 LoginWindow
    # label = QLabel()
    # label.setParent(self)
    label = QLabel(self)
    label.setText("社会我杰哥，人狠话不多")
    label.move(100,100)
    self.le = QLineEdit(self)
    self.le.setText(self.settings.value("username"))
    # 透明效果
    animation = QPropertyAnimation(self)
    animation.setTargetObject(self)
    animation.setPropertyName(b"windowOpacity")
    animation.setStartValue(1)
    animation.setKeyValueAt(0.5,0)
    animation.setEndValue(1)
    animation.setLoopCount(2)
    animation.setDuration(2000)
    animation.start(QAbstractAnimation.DeleteWhenStopped)

    # 信号：播放反比关闭窗口
    # animation.finished.connect(lambda : self.close())

    # 变大变小效果
    # animation = QPropertyAnimation(self)
    # animation.setTargetObject(self)
    # animation.setPropertyName(b"size")
    # animation.setStartValue(QSize(500,300))
    # animation.setKeyValueAt(0.5,QSize(500,0))
    # animation.setEndValue(QSize(500,300))
    # animation.setLoopCount(5)
    # animation.setDuration(2000)
    # animation.start()

  def getSystemSettings(self):
    self.settings = QSettings("yqfsoft", "QFRestaurante")
  def closeEvent(self,event):
    self.settings.setValue("username",self.le.text())
if __name__ == '__main__':
  import sys
  # 创建QApplication类的实例
  app = QApplication(sys.argv)
  # 创建一个窗口
  window = LoginWindow()
  window.show()
  # 进入程序主循环，窗口不会关闭，并且exit函数确保主循环安全退出
  sys.exit(app.exec_())
