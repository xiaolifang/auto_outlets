from base.Base import Base
from page.pageElements import PageElements


class ChooseLoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        self.click_element(PageElements.choice_login_exits_account_id)
