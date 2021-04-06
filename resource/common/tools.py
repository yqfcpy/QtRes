from PyQt5.QtCore import QSettings
import requests
import json

class CommonTools:

  # 创建一个变量保存 保存到文件
  @staticmethod
  def loadConfigFile(path="config.ini"):
    setting = QSettings(path, QSettings.IniFormat)
    return setting

  # 创建一个变量保存 保存到注册表
  @staticmethod
  def loadConfigRegedit(name="yqfsoft",subname="restaurant"):
    setting = QSettings(name, subname)
    return setting

class RequestTools:

  time_out = 10000  # 请求超时时间

  def __init__(self, url=None, data=None, headers=None):
    self.url = url
    self.data = data
    self.headers = headers

  # get请求
  def get(self):
    try:
      req = requests.get(self.url, params=self.data, headers=self.headers, timeout=self.time_out)
    except Exception as e:  # 请求报错
      res = {'status': 0, 'err_msg': e.args}  # 0代表请求失败
    else:  # 请求成功
      try:
        res = req.json()  # 1 返回json类型数据
      except Exception as e:
        res = {'status': 2, 'data': req.text}  # 2返回非json类型数据
    return res

  # post请求
  def post(self):
    try:
      req = requests.post(self.url, data=self.data, headers=self.headers, timeout=self.time_out)
    except Exception as e:  # 请求报错
      res = {'success': False, 'code': 0, 'message': e.args}  # 0代表请求失败
    else:  # 请求成功
      try:
        res = req.json() # 1 返回json类型数据
      except Exception as e:
        res = {'status': 2, 'data': req.text}  # 2返回非json类型数据
    return res

  # 测试服务器状态
  @classmethod
  def getConnectionState(cls):
    url = cls.getUrl()
    try:
      res = requests.get(url)
    except:
      pass

    if res.status_code == 200:
      return True
    else:
      return False

  # 获取服务器地址和端口号 http://localhost:18080
  @staticmethod
  def getUrl(path = "config.ini"):
    setting = QSettings(path, QSettings.IniFormat)
    server = setting.value("server/server")
    port = setting.value("server/port")
    url = "http://" + server + ":" + port
    return url