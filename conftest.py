# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         10:45

# -------------------------------------
import time
import pytest
from Common.app_driver import BaseDriver
from Common.check_port import release_port

base_driver = None


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device_info", help=None)


@pytest.fixture(scope="session")
def cmd_opt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture(scope="session")
def common_driver(cmd_opt):
    cmd_opt = eval(cmd_opt)
    global base_driver
    base_driver = BaseDriver(cmd_opt)
    time.sleep(1)
    driver = base_driver.get_base_driver()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    release_port(cmd_opt["server_port"])