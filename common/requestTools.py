from PyQt5 import QtNetwork
from PyQt5.QtCore import QSettings, QUrl, QJsonDocument, pyqtSignal, QObject, QUrlQuery
import json, requests


class SyncRequest:

  # get请求
  @staticmethod
  def get(url: str, query: dict = None, **kwargs):
    try:
      result = requests.get(url, params=query, **kwargs)
    except:  # 请求报错
      errorResult = {'success': False, 'code': 0, 'message': 'Local Exception'}  # 0代表本地异常请求失败 服务器宕机
      return errorResult
    else:  # 请求成功
      return result.json()

  # post请求
  @staticmethod
  def post(url: str, query: dict = None, **kwargs):
    try:
      result = requests.post(url, params=query, **kwargs)
    except:  # 请求报错
      errorResult = {'success': False, 'code': 0, 'message': 'Local Exception'}  # 0代表本地异常请求失败 服务器宕机
      return errorResult
    else:  # 请求成功
      return result.json()

  # 读取服务器地址
  @staticmethod
  def getServerUrlFromConfig(configFile: str):
    setting = QSettings(configFile, QSettings.IniFormat)
    server = setting.value("server/server")
    port = setting.value("server/port")
    if port == "":
      url = "http://" + server
    else:
      url = "http://" + server + ":" + port
    return url

  # 读取服务器地址
  @staticmethod
  def getServerUrl(server: str, port: str):
    if port == "" and port == None:
      url = "http://" + server
    else:
      url = "http://" + server + ":" + port
    return url

  # 连接是否成功
  @staticmethod
  def isServerConnected(url: str):
    try:
      res = requests.get(url)
    except:
      return False
    else:
      if res.json() != None:
        return True
      else:
        return False


class AsyncRequest(QObject):
  getResult = pyqtSignal(dict)

  def __init__(self):
    super().__init__()

  def get(self, url: str, param: dict = None):
    # 创建一个请求
    path = QUrl(url)
    req = QtNetwork.QNetworkRequest(path)
    if param != None:
      query = QUrlQuery()
      for item in param.items():
        query.addQueryItem(item[0], str(item[1]))
      url.setQuery(query.query())
    self.nam = QtNetwork.QNetworkAccessManager()
    self.nam.finished.connect(self.handleResponse)
    # 使用get请求 如果有参数的话 写一个data 放到get里
    self.nam.get(req)

  def post(self, url: str, jsonBody: dict, param: dict = None):
    path = QUrl(url)
    sendData = QJsonDocument(jsonBody)
    req = QtNetwork.QNetworkRequest(path)
    if param != None:
      queryParams = QUrlQuery()
      for item in param.items():
        queryParams.addQueryItem(item[0], str(item[1]))
      url.setQuery(queryParams.query())
    # 设置头信息是json这里可以不写
    # req.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, "application/json")
    self.nam = QtNetwork.QNetworkAccessManager()
    self.nam.finished.connect(self.handleResponse)
    self.nam.post(req, sendData.toJson())

  def handleResponse(self, reply):
    # replay是发出信号后的返回值
    er = reply.error()
    # 如果返回值没有错误的话 执行
    if er == QtNetwork.QNetworkReply.NoError:
      bytes_string = reply.readAll()
      bytes_string_to_json = json.loads(str(bytes_string, "utf-8"))
      self.result = bytes_string_to_json
    else:
      errorResult = {'success': False, 'code': 0, 'message': 'Local Exception'}
      self.result = errorResult
    self.getResult.emit(self.result)
