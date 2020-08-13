# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         9:36

# -------------------------------------
import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def width(self):
        """获取app的宽度"""
        return self.driver.get_window_size()['width']

    @property
    def height(self):
        """获取app的高度"""
        return self.driver.get_window_size()['height']

    def swipe_left(self, duration=200):
        """向左滑动"""
        self.driver.swipe(self.width * 0.9, self.height * 0.5,
                          self.width * 0.1, self.height * 0.5, duration)

    def swipe_right(self, duration=200):
        """向右滑动"""
        self.driver.swipe(self.width * 0.1, self.height * 0.5,
                          self.width * 0.9, self.height * 0.5, duration)

    def swipe_up(self, duration=200):
        """向上滑动"""

        self.driver.swipe(self.width * 0.5, self.height * 0.9,
                          self.width * 0.5, self.height * 0.1, duration)

    def swipe_down(self, duration=200):
        """向下滑动"""

        self.driver.swipe(self.width * 0.5, self.height * 0.1,
                          self.width * 0.5, self.height * 0.9, duration)

    def swipe(self, direction='down', duration=200, swipes=1):
        """
        屏幕滑动操作
        :param direction: 操作的方向
        :param duration: 持续时间
        :param swipes: 操作次数
        :return:
        """
        for s in range(swipes):
            time.sleep(0.2)
            if direction.lower() == 'left':
                self.swipe_left(duration)
            elif direction.lower() == 'right':
                self.swipe_right(duration)
            elif direction.lower() == 'up':
                self.swipe_up(duration)
            else:
                self.swipe_down(duration)

    def scratchable_latex(self, jgg_elem, location):
        """
        九宫格 解锁操作，移动6个位置
        :param jgg_elem: 九宫格元素
        :param location: 移动的位置
        :return:
        """
        jgg_width = jgg_elem.rect['width']
        jgg_height = jgg_elem.rect['height']
        jgg_x = jgg_elem.rect['x']
        jgg_y = jgg_elem.rect['y']
        # 获取九个点的坐标
        coordinates = [{"x": jgg_x + jgg_width * 1 / 6, "y": jgg_y + jgg_height * 1 / 6},
                       {"x": jgg_x + jgg_width * 3 / 6, "y": jgg_y + jgg_height * 1 / 6},
                       {"x": jgg_x + jgg_width * 5 / 6, "y": jgg_y + jgg_height * 1 / 6},
                       {"x": jgg_x + jgg_width * 1 / 6, "y": jgg_y + jgg_height * 3 / 6},
                       {"x": jgg_x + jgg_width * 3 / 6, "y": jgg_y + jgg_height * 3 / 6},
                       {"x": jgg_x + jgg_width * 5 / 6, "y": jgg_y + jgg_height * 3 / 6},
                       {"x": jgg_x + jgg_width * 1 / 6, "y": jgg_y + jgg_height * 5 / 6},
                       {"x": jgg_x + jgg_width * 3 / 6, "y": jgg_y + jgg_height * 5 / 6},
                       {"x": jgg_x + jgg_width * 5 / 6, "y": jgg_y + jgg_height * 5 / 6}]
        li = []
        for i in location:
            re = int(i) - 1
            li.append(coordinates[re])
        # 执行解锁
        TouchAction(self.driver).press(**li[0]).wait(200). \
            move_to(**li[1]).wait(200). \
            move_to(**li[2]).wait(200). \
            move_to(**li[3]).wait(200). \
            move_to(**li[4]).wait(200).release().perform()

    def zoom(self):
        """
        放大操作
        :return:
        """
        action1 = TouchAction(self.driver)  # 第一个手势
        action2 = TouchAction(self.driver)  # 第二个手势
        zoom_action = MultiAction(self.driver)  # 放大手势
        action1.press(self.width * 0.4, self.height * 0.4).wait(500). \
            move_to(self.width * 0.2, self.height * 0.2).release()
        action2.press(self.width * 0.6, self.height * 0.6).wait(500). \
            move_to(self.width * 0.8, self.height * 0.8).release()
        zoom_action.add(action1, action2)  # 两个动作同时进行
        zoom_action.perform()  # 执行操作

    def pinch(self):
        """缩小操作"""
        action1 = TouchAction(self.driver)  # 第一个手势
        action2 = TouchAction(self.driver)  # 第二个手势
        pinch_action = MultiAction(self.driver)  # 缩小手势
        action1.press(self.width * 0.2, self.height * 0.2).wait(500). \
            move_to(self.width * 0.4, self.height * 0.4).release()
        action2.press(self.width * 0.8, self.height * 0.8).wait(500). \
            move_to(self.width * 0.6, self.height * 0.6).release()
        pinch_action.add(action1, action2)  # 两个动作同时进行
        pinch_action.perform()  # 执行操作

    def get_elem_toast(self, msg):
        """获取弹窗元素"""
        return self.driver.find_element(*(MobileBy.XPATH, '//*[contains(@text,{})]'.format(msg)))

    def find_element(self, locator: tuple, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(lambda driver: driver.find_element(*locator))
            return element
        except (NoSuchElementException, TimeoutException):
            print('no found element {} by {}', format(locator[1], locator[0]))


if __name__ == '__main__':
    pass