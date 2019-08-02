from base.Base import Base
from page.pageElements import PageElements


class IndexPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_me_btn(self):
        self.click_element(PageElements.home_my_btn_id)