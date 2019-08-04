import os
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver

from APP import BASE_PROJECT


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=15, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隔时间
        :return:返回元素的定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=15, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隔时间
        :return:返回元素的定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=15, poll_frequency=1.0):
        """
        点击元素
        :param loc: (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隔时间
        :return:
        """
        self.get_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=15, poll_frequency=1.0):
        """
        输入文本内容
        :param loc: (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param text: 输入文本内容
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隔时间
        :return:
        """
        # 定位
        input_text = self.get_element(loc, timeout, poll_frequency)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    def scroll_screen(self, tag=1):
        """
        滑动屏幕方法
        :param tag: 1:向上 2：向下 3：向左 4：向右
        :return:
        """
        # 等待1-2秒,防止页面未跳转
        import time
        time.sleep(2)

        # 屏幕分辨率
        screen = self.driver.get_window_size()
        # 宽
        width = screen.get("width")
        # 高
        height = screen.get("height")
        # 判断滑动 80% -> 30%
        if tag == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3)
        if tag == 2:
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8)
        if tag == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5)
        if tag == 4:
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5)

    def get_toast(self, toast):
        mess_path = (By.XPATH, "//*[contains(@text,'{}')]".format(toast))
        return self.get_element(mess_path, timeout=3, poll_frequency=0.5).text

    def get_picture(self, name="截图"):
        # 图片名字
        image_name = BASE_PROJECT + os.sep + "image" + os.sep + "%d.png" % int(time.time())
        # 截图
        self.driver.get_screenshot_as_file(image_name)
        with open(image_name, "rb") as f:
            allure.attach(name, f.read(), allure.attach_type.PNG)

    def get_login_btn(self):
        login_btn = (By.XPATH, "//*[contains(@text,'登录')]")
        self.get_element(login_btn)
