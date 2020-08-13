# -------------------------------------

# Description:  AppiumTestPro
# Author:       ALan
# Time:         14:45

# -------------------------------------
import time
from appium.webdriver.common.mobileby import MobileBy
from Common.basepage import BasePage


class TestGesture(object):
    def test_login(self, common_driver):
        """登录"""
        driver = BasePage(common_driver)
        time.sleep(3)
        driver.swipe(direction='left', swipes=3)  # 滑动屏幕
        # 进入首页
        home_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_start')
        driver.find_element(home_btn).click()
        time.sleep(2)
        login_btn = (MobileBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().textContains(\"注册/登录\").resourceId(\"com.xxzb.fenwoo:id/btn_login\")')
        driver.find_element(login_btn).click()
        time.sleep(2)
        driver.find_element((MobileBy.ID, 'com.xxzb.fenwoo:id/et_phone')).send_keys('18684720553')
        time.sleep(2)
        driver.find_element((MobileBy.ID, 'com.xxzb.fenwoo:id/btn_next_step')).click()
        driver.find_element((MobileBy.ID, 'com.xxzb.fenwoo:id/et_pwd')).send_keys('python')
        driver.find_element((MobileBy.ID, 'com.xxzb.fenwoo:id/btn_next_step')).click()

    def test_gesture_password(self, common_driver):
        """绘制手势密码"""
        driver = common_driver
        base = BasePage(driver)
        time.sleep(3)
        driver.start_activity(app_package="com.xxzb.fenwoo",
                              app_activity=".activity.user.CreateGesturePwdActivity")
        commit_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/right_btn')
        password_gesture = (MobileBy.ID, 'com.xxzb.fenwoo:id/gesturepwd_create_lockview')
        element_commit = base.find_element(commit_btn)
        element_commit.click()
        password_element = base.find_element(password_gesture)
        base.scratchable_latex(password_element, '14789')
        time.sleep(5)


if __name__ == '__main__':
    pass
