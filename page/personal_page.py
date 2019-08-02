from base.Base import Base
from page.pageElements import PageElements


class PersonalPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def get_collect(self):
        return self.get_element(PageElements.person_shopcart_id).text

    def click_setting_btn(self):
        self.click_element(PageElements.person_setting_btn_id)
