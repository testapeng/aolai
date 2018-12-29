import os, sys
sys.path.append(os.getcwd())
import pytest, base
from page.navigation_page import Navigationpage
from base.base_driver import init_driver
from base.read_yaml_data import read_yaml_data
import time


# 获取模拟的yaml数据
def get_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    # print(data)
    # 获取所有的键,i就是单独的键
    for i in data.keys():
        # 通过键取它的值,是花括号一堆数据,里面有想要的数据
        data2 = data.get(i)
        # 通过键取对应的值
        name = data2.get("username")
        passwd = data2.get("password")
        tag = data2.get("tag")
        except_msg = data2.get("except_msg")
        get_toast_msg = data2.get("get_toast_msg")
        # 改造成自己想要的格式,定义一个列表,给他们追加到列表里
        data_list.append((name, passwd, tag, except_msg, get_toast_msg))
    #  在循环外面返回列表,切记
    return data_list


class Testlogin:
    # 初始化导航类
    def setup_class(self):
        # 1.初始化driver对象
        self.driver = init_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        # 2.初始化导航对象
        self.navigation_page = Navigationpage(self.driver)

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    # 测试登录业务
    @pytest.mark.parametrize("username,password", get_data())
    def test_login(self, username, password):
        # 1.点击我的
        # 2.使用导航类实例对象,调用它里面的我的页面实例对象,
        # 其实就已经是我的页面的实例对象,这样可以调用我的页面的方法
        self.navigation_page.get_home_page_obj().click_my()
        # 2.点击已有账号
        self.navigation_page.get_preparelogin_page_obj().click_exist_account()
        # 3.输入用户名密码 点击登录,全三步都一样,都是要执行的,到第四部开始两种业务逻辑
        self.navigation_page.get_login_page_obj().click_login(username, password)
        # # 4.先按照正确的写,分开的写,最后在合并
        # 判断全部订单是否存在,如果存在就为真,否则就为假,现在只考虑正向的数据
        # login_static = self.navigation_page.get_person_center_page_obj().is_login_sucess()
        # assert login_static
        self.navigation_page.get_person_center_page_obj().click_person_center_setting()

        self.navigation_page.get_setting_page_obj().quit_account()

    # 函数返回了几个,你就写几个参数,参数要对等,实参和形参要一致
    @pytest.mark.parametrize("username,password,except_msg,get_toast_msg,", get_data())
    def test_login2(self, get_toast_msg,username,password,except_msg):
        # 1.点击我的
        # 2.使用导航类实例对象,调用它里面的我的页面实例对象,
        # 其实就已经是我的页面的实例对象,这样可以调用我的页面的方法
        self.navigation_page.get_home_page_obj().click_my()
        # 2.点击已有账号
        self.navigation_page.get_preparelogin_page_obj().click_exist_account()
        # 3.输入用户名密码 点击登录,
        self.navigation_page.get_login_page_obj().click_login(username, password)







