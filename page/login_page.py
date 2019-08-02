from base.Base import Base
from page.pageElements import PageElements


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, user, password):
        self.send_element(PageElements.login_name_id, user)
        self.send_element(PageElements.login_passwd_id, password)
        self.click_element(PageElements.login_btn_id)
