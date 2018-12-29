import allure

from base.base_action import BaseAction

import base
"""
负责 首页  分类 购物车  我的  业务
"""

class Homepage(BaseAction):
    # 魔术方法初始化函数,动态的把driver手机对象传过来
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击我的')
    def click_my(self):
        self.click_element(base.home_my_button)