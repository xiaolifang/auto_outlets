from page.index_page import IndexPage
from page.choose_login_page import ChooseLoginPage
from page.setting_page import SettingPage
from page.personal_page import PersonalPage
from page.login_page import LoginPage


class Page():
    def __init__(self, driver):
        self.driver = driver

    def get_index_page(self):
        return IndexPage(self.driver)

    def get_choose_login_page(self):
        return ChooseLoginPage(self.driver)

    def get_setting_page(self):
        return SettingPage(self.driver)

    def get_personal_page(self):
        return PersonalPage(self.driver)

    def login_page(self):
        return LoginPage(self.driver)
