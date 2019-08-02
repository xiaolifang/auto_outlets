from base.Base import Base
from page.pageElements import PageElements


class SettingPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def setting_quit(self, tag=1):
        self.scroll_screen()
        self.click_element(PageElements.setting_logout_btn_id)
        if tag == 1:
            self.click_element(PageElements.setting_acc_logout_btn_id)
        if tag == 0:
            self.click_element(PageElements.setting_dis_logout_btn_id)
