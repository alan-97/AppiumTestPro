# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         10:34

# -------------------------------------
import os
"""环境路径配置"""
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(ROOT_DIR, "log")
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
CONFIG_PATH = os.path.join(CONFIG_DIR, "cap.yaml")