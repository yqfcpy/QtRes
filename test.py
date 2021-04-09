from PyQt5 import QtNetwork
from PyQt5.QtCore import QSettings, QDateTime, QUrl, QUrlQuery, QByteArray, QJsonDocument
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTextEdit

from resource.common.threadTools import TimeThread
from resource.common.qfTools import RequestAsyncTool


class MainWindow(QWidget):
  def __init__(self, parent=None, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.resize(400, 400)
    self.btn = QPushButton(self)
    self.btn.resize(60, 40)
    self.btn.move(340, 360)
    self.btn.setText("测试")
    self.te = QTextEdit(self)
    self.te.resize(400, 340)
    # self.setting = QSettings("cctv.dat",QSettings.InvalidFormat)

    self.timeTd = TimeThread()
    self.timeTd.start()

    self.btn.clicked.connect(self.test6)
    self.timeTd.show_time_signal.connect(self.display_time)

  def display_time(self, time1: QDateTime):
    self.te.setPlainText(time1.toString("yyyy-MM-dd hh:mm:ss"))

  def test6(self):
    dic = {"username":"admin","password":123456}
    path = QUrl("http://localhost:18080/user")
    query = QUrlQuery()
    if 1 != 2 :
      for item in dic.items():
        print(item[0], item[1])
        query.addQueryItem(str(item[0]), str(item[1]))
      path.setQuery(query.query())
      print(path)

  def fun(self, a: int):
    print(type(a), a)

  def test5(self):
    self.sendTd = RequestAsyncTool()
    data = {"username": "admin", "password": "111111"}
    self.sendTd.post("http://localhost:18080/user/login", data)
    self.sendTd.getResult.connect(lambda s: print(s))

  def test3(self):
    url = QUrl("http://localhost:18080/user")
    query = QUrlQuery()
    query.addQueryItem("username", "yqfcpy");
    query.addQueryItem("password", "111111");
    url.setQuery(query.query())
    print(query.query())
    print(url)
    # self.doRequest()

  def test4(self):
    self.doLogin()

  def doLogin(self):
    jsonbody = {"username": "admin", "password": "111111"}
    sendData = QJsonDocument(jsonbody)
    print(sendData.toJson())
    url = "http://localhost:18080/user/login"
    # dic = QByteArray()
    # dic.append("username=admin&")
    # dic.append("password=111111")
    req = QtNetwork.QNetworkRequest(QUrl(url))
    # req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
    self.nam = QtNetwork.QNetworkAccessManager()

    self.nam.finished.connect(self.handleResponse)
    # 使用get请求 如果有参数的话 写一个data 放到get里
    self.nam.post(req, sendData.toJson())

  def doRequest(self):
    print("dorequest方法执行了")
    url = "http://localhost:18080"
    # 创建一个请求
    req = QtNetwork.QNetworkRequest(QUrl(url))

    self.nam = QtNetwork.QNetworkAccessManager()
    self.nam.finished.connect(self.handleResponse)
    # 使用get请求 如果有参数的话 写一个data 放到get里
    self.nam.get(req)

  def test2(self):
    # 字典的配合三元运算符
    server1 = {"server": "127.0.0.1", "port": 5000}
    server2 = {"server": "localhost", "port": 8000}
    addserver = {"server": "127.0.0.1", "port": 5000}
    list1 = [server1, server2]
    # 小于5000 加工资500 大于5000 加工资200
    result = [item for item in list1 if addserver == item]
    if len(result) == 0:
      list1.append(addserver)
    print()
    print(result)

  # def test(self):
  #   isOk = RequestTools.get("http://localhost:18080")
  #   a = {}
  #   print(isOk, type(a))


if __name__ == '__main__':
  import sys

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec_()