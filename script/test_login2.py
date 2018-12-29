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
    @pytest.mark.parametrize("username, password, tag, except_msg, get_toast_msg ", get_data())
    def test_login(self, username, password, tag, except_msg, get_toast_msg):
        # 1.点击我的
        # 2.使用导航类实例对象,调用它里面的我的页面实例对象,
        # 其实就已经是我的页面的实例对象,这样可以调用我的页面的方法
        self.navigation_page.get_home_page_obj().click_my()
        # 2.点击已有账号
        self.navigation_page.get_preparelogin_page_obj().click_exist_account()
        # 3.输入用户名密码 点击登录,全三步都一样,都是要执行的,到第四部开始两种业务逻辑
        self.navigation_page.get_login_page_obj().click_login(username, password)
        # 4.合并代码，当tag的状态是1时，走正向的业务（滑动退出关闭浏览器）
        # else时走错误的业务，就是获取屏幕中的toast弹出消息，拿实际结果和预期结果做比对，
        # 然后关闭页面走下一条,走完判断后还要做校验，判断它是否真的实现了业务
        if tag == 1:
            try:
                # 捕获怀疑的代码，如果有一句有问题，下面的都不走了，断言也不走，直接走except处理
                # 判断全部订单是否存在,如果存在说明校验成功
                login_static = self.navigation_page.get_person_center_page_obj().is_login_sucess()
                # 断言状态是否为真，为真滑动退出走下一条，为假截图
                # 点击设置按钮
                self.navigation_page.get_person_center_page_obj().click_person_center_setting()
                # 滑动退出
                self.navigation_page.get_setting_page_obj().quit_account()
                # 断言它是否正确,如果为true，不走后面的截图代码，为false，走后面的截图代码
                assert login_static,self.navigation_page.get_login_page_obj().get_screen()

            except:
                # 如果上面try写的有问题,直接跳到except执行代码
                self.navigation_page.get_login_page_obj().get_screen()
                self.navigation_page.get_login_page_obj().close_login_page()

        else:
            try:
                # 怀疑这段代码,用get_toast_mag这个方法获取屏幕上世纪的toast弹出信息文本
                toast_massgae = self.navigation_page.get_login_page_obj().get_toast_message(get_toast_msg)
                # 出现问题,截个图,没有出现问题不截图
                assert toast_massgae == except_msg,self.navigation_page.get_login_page_obj().get_screen()
            finally:
                # 不管有没有问题都关闭登录页面
                self.navigation_page.get_login_page_obj().close_login_page()

            # 4.写错误的,只写错误类,获取它的toast吐司的弹出文本,吐司只能通过xpath获取,写到公共类里面
            # 这里参数不能写预期结果,因为这样它会一直正确,预期==预期不行,只能预期和实际结果对比
            # toast_msg = self.navigation_page.get_setting_page_obj().get_toast_message(get_toast_msg)
            # 断言屏幕实际的弹出消息与预期的弹出消息
            # assert toast_msg == except_msg


















