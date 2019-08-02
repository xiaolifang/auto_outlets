from base.Base import Base
from base.get_driver import get_driver
from page.pageElements import PageElements


class ChooseLoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        self.click_element(PageElements.choice_login_exits_account_id)


if __name__ == '__main__':
    aa = ChooseLoginPage(get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity"))
    aa.click_login_btn()
