# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         10:29

# -------------------------------------


import subprocess
import time
from config.root_config import LOG_DIR


def appium_start(host, port, log_name):
    """
    启动appium server
    :param host:
    :param port:
    :param log_name:
    :return:
    """
    # 指定bp端口号
    bootstrap_port = str(port + 1)
    # cmd命令
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    # 去掉 “/b”，即可以打开cmd弹窗运行
    # cmd = 'start  appium -a ' + host+' -p '+str(port) +' -bp '+ str(bootstrap_port)
    # 打印输入的cmd命令，及时间
    print("%s at %s " % (cmd, time.ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open(LOG_DIR + '/appium_log/' + f'{log_name}.log', 'w',encoding='utf8'),
                     stderr=subprocess.STDOUT)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    # appium_start(host, port)

