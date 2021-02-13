from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == '__main__':
  app = QApplication(sys.argv) #创建QApplication类的实例
  window = QWidget() #创建一个窗口
  window.resize(500,300) #设置窗口的尺寸
  window.move(400,400) #移动窗口
  window.setWindowTitle('我的第一个Qt程序') #设置窗口的标题
  window.show() #显示窗口
  sys.exit(app.exec_()) #进入程序主循环，窗口不会关闭，并且exit函数确保主循环安全退出