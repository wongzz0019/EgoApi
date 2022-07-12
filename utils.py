# 初始化日志的函数
import logging
import os.path
from logging import handlers


def init_logging():
    # 1.创建一个日志器：如果不写日志器的名称，那么会使用默认的日志器root
    logger = logging.getLogger()
    # 2.设置日志的等级
    logger.setLevel(logging.INFO)
    # 3.设置处理器
    # 控制台处理器：控制把日志输出到控制台
    sf = logging.StreamHandler()
    # 文件处理器：控制把日志输出到外部文件当中，需要提前定义文件的路径和文件名称
    # __file__ :是当前文件(utils.py)的路径; os.path.abspath(__file__):格式化路径; os.path.dirname:当前文件的父级目录
    logname = os.path.dirname(os.path.abspath(__file__)) + '/log/ego.log'
    fh = logging.handlers.TimedRotatingFileHandler(logname, when='M', interval=1, backupCount=7, encoding='utf-8')
    # 4.设置格式化器：指打印日志时的格式内容
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 5.将格式化器添加到处理器当中（文件处理器和控制台处理器都要添加）
    sf.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 6.将处理器添加到日志器当中
    logger.addHandler(sf)
    logger.addHandler(fh)


