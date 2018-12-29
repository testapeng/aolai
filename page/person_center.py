import allure

from base.base_action import BaseAction
import base

"""
负责 个人中心页面逻辑
"""
class Personcenterpage(BaseAction):
    # 魔术方法初始化函数,动态的把driver手机对象传过来
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('点击进入个人中心')
    def click_person_center_setting(self):
        self.click_element(base.person_center_setting_btn)

    #判断一下是否登录成功 如果登录成功返回true 登录失败就返回false
    @allure.step('判断是否登陆成功')
    def is_login_sucess(self):
        try:
            allure.attach('个人中心', '找到全部订单,说明登陆成功')
            self.find_element(base.person_center_all_order)
            return True
        except:
            return False
