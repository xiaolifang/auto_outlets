import time

from selenium.webdriver.common.by import By
from base.Base import Base
from page.page import Page
from base.get_driver import get_driver

page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))
page_obj.get_index_page().click_me_btn()
page_obj.get_choose_login_page().click_login_btn()
time.sleep(1)
page_obj.login_page().login("18701878226", "air2111960")
# 获取toast消息
# mess_path = (By.XPATH, "//*contains[@text,'登录密码错误']")
# print(page_obj.login_page().get_element(mess_path).text)
print(page_obj.login_page().get_toast("登录密码错误"))
# time.sleep(2)
# print(page_obj.get_personal_page().get_collect())
# page_obj.get_personal_page().click_setting_btn()
# page_obj.get_setting_page().setting_quit()
# page_obj.driver.quit()
