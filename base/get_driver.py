from appium import webdriver


def get_driver(pack, activ):
    """

    :param pack: APP包名
    :param activ: 页面名
    :return: driver对象
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'sanxing'
    desired_caps['appPackage'] = pack
    desired_caps['appActivity'] = activ
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['automationName'] = 'Uiautomator2'
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
