import time

from page.page import Page
from base.get_driver import get_driver
page_obj=Page(get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity"))
page_obj.get_index_page().click_me_btn()
page_obj.get_choose_login_page().click_login_btn()
time.sleep(1)
page_obj.login_page().login("18701878226","air2311960")
time.sleep(2)
print(page_obj.get_personal_page().get_collect())
page_obj.get_personal_page().click_setting_btn()
page_obj.get_setting_page().setting_quit()
page_obj.driver.quit()