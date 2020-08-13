# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         14:32

# -------------------------------------
import logging
import os
from logging.handlers import RotatingFileHandler
from config.root_config import LOG_DIR


LOG_PATH = LOG_DIR + '/Pro_log'


class MyLog(object):
    """日志收集"""

    def __new__(cls, *args, **kwargs):
        # 创建一个日志收集器对象
        my_log = logging.getLogger('my_log')
        my_log.setLevel('DEBUG')
        # 创建日志输出格式
        fm = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s',
                               '%Y-%m-%d %H:%M:%S')
        # 创建控制台输出渠道
        sh = logging.StreamHandler()
        sh.setLevel('INFO')
        sh.setFormatter(fm)

        # 创建文件输出渠道
        # 按文件大小轮转
        base_filename = os.path.join(LOG_PATH, 'my_log.log')  # 文件的命名
        fh = RotatingFileHandler(base_filename, encoding='utf-8', mode='a', maxBytes=1024 * 1024, backupCount=3)
        fh.setLevel('DEBUG')
        fh.setFormatter(fm)
        # 将输出渠道与日志收集器对接
        my_log.addHandler(sh)
        my_log.addHandler(fh)
        return my_log


log = MyLog()
log.debug('==')
if __name__ == '__main__':
    pass
