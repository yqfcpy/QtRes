import logging
import logging.config
import os


# 日志的格式
# 复杂格式    ‘\’是换行键
standard_format = '[%(asctime)s] - [%(levelname)s] - [%(message)s] - [%(threadName)s:%(thread)d] - '\
                  '[task_id:%(name)s] - [%(filename)s:%(lineno)d]'
# 标准的格式
simple_format = '[%(levelname)s] - [%(message)s] - [%(filename)s:%(lineno)d] - [%(asctime)s]'
# 简单格式
id_simple_format = '[%(levelname)s] - [%(message)s] - [%(asctime)s]'
# 日志路径 注意这里写上日志的名字
logFile_path = os.getcwd() + '/log/' + "syslog.log"

dictConfig = {
  'version': 1,
  'disable_existing_loggers': False,
  # 格式
  'formatters': {
    # 复杂的format格式
    'standard': {
      'format': standard_format
    },
    'simple': {
      'format': simple_format
    },
    'simple2': {
      'format': id_simple_format
    }
  },
  # 'filter': {
  #   # 过滤这里写
  # },
  'handlers': {
    # 打印终端的日志
    'console': {
      'formatter': 'simple',
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
    },
    # 打印到文件的
    'default': {
      'formatter': 'standard',
      'level': 'WARNING',
      'class': 'logging.handlers.RotatingFileHandler',
      # 日志文件的路径
      'filename': logFile_path,
      # 最大文件大小 10mb
      'maxBytes': 10 * 1024 * 1024,
      # 最大文件数
      'backupCount': 5,
      'mode': 'w',
      'encoding': 'utf-8'
    }
  },
  'loggers': {
    # 这个yqfsoftlog也可以不写直接就是 ''
    'yqfsoftlog': {
      # 设置handler对象
      'handlers': ['console', 'default'],
      'level': logging.DEBUG,
      'propagate': True
    }
  }
}


def loggerConfig(logFile_path=None):
  if logFile_path:
    dictConfig['handlers']['default']['filename'] = logFile_path
  logging.config.dictConfig(dictConfig)
  logger = logging.getLogger("yqfsoftlog")
  return logger
