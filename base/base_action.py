from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time, allure

class BaseAction:

    # 当类创建的时候,这个方法就会执行,
    # page测试页面类会调用父类,所以他会传driver
    def __init__(self,driver):
        self.driver = driver

    # 基类的点击方法
    def click_element(self,loc):
        # 点击哪个元素,得先找到元素
        self.find_element(loc).click()


    #  基类的输入方法
    def input_element_content(self,loc,content):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)


    # 公共类的长按
    def long_press(self,loc):
        ys = self.find_element(loc)
        TouchAction(self.driver).long_press(ys).perform()


    # 自己封装的BaseAction类的定位一个元素方式,
    # 底层还是手机对象的定位方式find_element
    # 需要的参数是定位到的元素,以数组格式展示的那种
    def find_element(self, loc):
        # 在找到元素之前都要隐式等待10秒
        self.driver.implicitly_wait(10)
        # 返回的是要用的元素
        return self.driver.find_element(loc[0], loc[1])



    # 自己封装的BaseAction类的定位一组元素方式,注意:是一组
    # 底层还是手机对象的定位方式find_elements
    # 需要的参数是定位到的元素,以数组格式展示的那种
    def find_elements(self, loc):
        # 在找到元素之前都要隐式等待10秒
        self.driver.implicitly_wait(10)
        # 返回的是要用的元素
        return self.driver.find_elements(loc[0], loc[1])

        # 实现滑动业务
    def swipe_screen(self, tag):
        time.sleep(1)
        # 获取当前手机窗口的大小
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width")  # 获取手机宽
        height = screen_size.get("height")  # 获取手机的高
        if tag == 1:  # 向上滚动 两点之间滑动  x轴不变
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:  # 向下滚动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:  # 向左滚动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:  # 向右滚动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)


    # 获取toast弹出的文本信息,注意,这个是获取的实际结果的文本弹出信息
    # 获取的toast的文本消息,实际结果
    @allure.step('获取toast弹出信息')
    def get_toast_message(self, message):
        toast_xpath = "//*[contains(@text,'{}')]".format(message)
        toast_message = self.find_element((By.XPATH, toast_xpath)).text
        return toast_message


    def get_screen(self):
        #截图名称，这个函数一执行，截个图
        # time为什么转成整形，因为time.time是当前系统时间，可能带小数点，
        png_name = "./screen/{}.png".format(int(time.time()))
        self.driver.get_screenshot_as_file(png_name)
        with open(png_name, "rb") as f:
            allure.attach("截图名字", f.read(), allure.attach_type.PNG)


"""
loc代表的是定位的元素,是一个元组,0是定位的方式,1是定位的位置,
返回的是找到的元素
"""





