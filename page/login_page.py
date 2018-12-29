import allure

from base.base_action import BaseAction
import base

"""
负责登录页面的业务
"""
class Loginpage(BaseAction):
    # 魔术方法初始化函数,动态的把driver手机对象传过来
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('登录业务')
    def click_login(self,name,pwd):
        allure.attach('登录','输入账户')
        self.input_element_content(base.login_username_id,name)
        allure.attach('登录', '输入密码')
        self.input_element_content(base.login_password_id,pwd)
        allure.attach('登录', '点击登录')
        self.click_element(base.login_login_in_btn)

    #关闭登录页面
    def close_login_page(self):
        self.click_element(base.login_login_out_btn)
