from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class RegExpValidator:

  @staticmethod
  def getPortValidator():
    pattern = QRegExp('^([1-9]|[1-9]\\d{3}|[1-6][0-5][0-5][0-3][0-5])$')
    portValidator = QRegExpValidator(pattern)
    return portValidator
