from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class RegExpValidator:

  @staticmethod
  def getPortValidator():
    pattern = QRegExp('^([1-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$')
    portValidator = QRegExpValidator(pattern)
    return portValidator
