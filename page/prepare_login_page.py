import allure

from base.base_action import BaseAction
import base
"""
注册页面 
"""

class Preparelogin(BaseAction):
    # 魔术方法初始化函数,动态的把driver手机对象传过来
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('点击已有账号')
    def click_exist_account(self):
        self.click_element(base.sign_in_exit_account_id)