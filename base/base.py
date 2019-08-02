from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,loc,timeout=10,poll_frequency=1.0):
        WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))
