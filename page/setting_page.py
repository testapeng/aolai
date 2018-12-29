import allure

from base.base_action import BaseAction
import base
"""
负责 设置页面相关逻辑
"""
class Settingpage(BaseAction):
    # 魔术方法初始化函数,动态的把driver手机对象传过来
    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    @allure.step('点击退出')
    def quit_account(self):
        # 1.滑动页面低端 才会看见退出按钮 才能找到元素.想看下面的,向上滚动(往上滑动),想看上面的,向下滚动(往下滑动)
        allure.attach('退出账户', '滑动到底部,向上滑的')
        self.swipe_screen(1)
        # 2.点击退出按钮
        allure.attach('退出账户', '点击退出按钮')
        self.click_element(base.setting_center_login_out_btn)
        # 3.点击弹出对话框确定按钮[dialog_confirm_btn对话确认按钮]
        allure.attach('退出账户', '点击确认按钮')
        self.click_element(base.setting_center_login_dialog_confirm_btn)
