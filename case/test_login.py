import time

import os, sys

from selenium.common.exceptions import TimeoutException

# sys.path.append(os.getcwd())
import pytest
from base.get_driver import get_driver
from base.get_file_data import get_file_data
from page.page import Page


def get_data():
    login_data = get_file_data("login_data.yml")
    suc_list = []
    fai_list = []
    for i in login_data.keys():
        if login_data.get(i).get("toast"):
            fai_list.append((i, login_data.get(i).get("username"), login_data.get(i).get("passwd"),
                             login_data.get(i).get("toast"),
                             login_data.get(i).get("expect_data")))
        else:
            suc_list.append((i, login_data.get(i).get("username"), login_data.get(i).get("passwd"),
                             login_data.get(i).get("expect_data")))

    return {"success": suc_list, "fail": fai_list}


class TestLogin():
    def setup_class(self):
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.fixture(autouse=True)
    def go_to_login(self):
        self.page_obj.get_index_page().click_me_btn()
        self.page_obj.get_choose_login_page().click_login_btn()
        time.sleep(1)

    @pytest.mark.parametrize(" test_no,,user, passwd,except_data", get_data().get("success"))
    def test_login_success(self, test_no, user, passwd, except_data):
        self.page_obj.login_page().login(user, passwd)
        try:
            # 获取我的收藏
            my_collect = self.page_obj.get_personal_page().get_collect()
            try:
                # 断言
                assert my_collect == except_data
            #   断言成功,点击设置,退出
            except AssertionError:
                # 断言失败
                # 截图
                self.page_obj.login_page().get_picture()
                print(test_no)
                assert False
            finally:
                #  点击设置,退出
                self.page_obj.get_personal_page().click_setting_btn()
                self.page_obj.get_setting_page().setting_quit()

        except TimeoutException:
            print("失败")
            # """失败情况"""
            # 截图
            self.page_obj.login_page().get_picture()
            # 关掉登录页面
            self.page_obj.login_page().close_login_page()
            print(test_no)
            assert False

    @pytest.mark.parametrize(" test_no,,user, passwd,toast,except_data", get_data().get("fail"))
    def test_login_fail(self, test_no, user, passwd, toast, except_data):
        self.page_obj.login_page().login(user, passwd)
        try:
            # """找到toast"""
            # 获取toast消息
            toast_text = self.page_obj.login_page().get_toast(toast)
            try:
                assert toast_text == except_data
            except AssertionError:
                self.page_obj.login_page().get_picture()
                assert False

        except TimeoutException:
            self.page_obj.login_page().get_picture()
            assert False
        finally:
            try:
                # 判断登录按钮
                self.page_obj.login_page().get_login_btn()
                # 关闭登录按钮
                self.page_obj.login_page().close_login_page()

            except TimeoutException:
                self.page_obj.get_personal_page().click_setting_btn()
                # 截图
                self.page_obj.login_page().get_picture()
                self.page_obj.get_setting_page().setting_quit()
                assert False
