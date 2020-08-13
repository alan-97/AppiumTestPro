# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         11:23

# -------------------------------------

import socket
import os


def check_port(host, port):
    """检测指定的端口是否被占用"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError:
        print('port %s is available! ' % port)
        return True
    else:
        print('port %s already be in use !' % port)
        return False


def release_port(port):
    """释放指定的端口"""
    cmd_find = 'netstat -aon | findstr {}'.format(port)  # 查找对应端口的pid
    # 返回命令执行后的结果
    result = os.popen(cmd_find).read()
    if str(port) and 'LISTENING' in result:
        # 获取端口对应的pid进程
        i = result.index('LISTENING')
        start = i + len('LISTENING') + 7
        end = result.index('\n')
        pid = result[start:end]
        cmd_kill = 'taskkill -f -pid %s' % pid  # 关闭被占用端口的pid
        os.popen(cmd_kill)
        print(f'释放进程端口:{port}')
    else:
        print('port %s is available !' % port)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    release_port(4723)
    release_port(4725)
    if not check_port(host, port):
        print("端口被占用")
        release_port(port)
