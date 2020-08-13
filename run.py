# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         10:18

# -------------------------------------
import os
import threading
import time
from multiprocessing import Pool
import pytest
from config.root_config import ROOT_DIR

"""多设备启动文件"""

device_infos = [
    {"title": "Emulator_one", "server_host": "127.0.0.1", "server_port": "4723", },
    {"title": "Emulator_two", "server_host": "127.0.0.1", "server_port": "4725", }
]
detail_report_path = ROOT_DIR + "\\report\\html"
xml_report_path = ROOT_DIR + "\\report\\xml"


def timer(func):
    """函数运行耗时装饰器"""

    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"总耗时：{end_time - start_time} s")

    return inner


# @timer
def main(device_info):
    pytest.main(["--cmdopt={}".format(device_info),
                 "--alluredir", xml_report_path, "-vs"])
    os.system("allure generate %s -o %s --clean" % (xml_report_path, detail_report_path))


if __name__ == '__main__':
    # 创建进程池
    with Pool(len(device_infos)) as pool:
        pool.map(main, device_infos)
        pool.close()
        pool.join()

    # threads = []  # 存储所有线程池
    # for i in device_infos:
    #     t = threading.Thread(target=main, args=(i,))
    #     t.start()
    #     threads.append(t)
    #     time.sleep(2)
    # for th in threads:
    #     th.join()  # 等待子线程
