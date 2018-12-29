from page.home_page import Homepage
from page.login_page import Loginpage
from page.person_center import Personcenterpage
from page.prepare_login_page import Preparelogin
from page.setting_page import Settingpage


"""
负责 
获取home_page, 
login_page,
person_center_page ,
setting_page,
prepare_login_page的实例对象,
这样就可以使用他们的函数方法了
"""
class Navigationpage:
    # 初始化的时候 谁调用我 就给他一个driver手机对象
    def __init__(self, driver):
        self.driver = driver

        # 获取home_page我的实例对象
    def get_home_page_obj(self):
        return Homepage(self.driver)

        # 获取login_page登录的实例对象
    def get_login_page_obj(self):
        return Loginpage(self.driver)

        # 获取person_center_page个人中心的实例对象
    def get_person_center_page_obj(self):
        return Personcenterpage(self.driver)

        # 获取setting_center_page设置按钮的实例对象

    def get_setting_page_obj(self):
        return Settingpage(self.driver)

        # 获取prepare_login_page已有账户的实例对象
    def get_preparelogin_page_obj(self):
        return Preparelogin(self.driver)
