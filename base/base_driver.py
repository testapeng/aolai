from appium import webdriver
# 调用这个方法,返回一个手机对象driver

# 这里面的参数是我通过脚本传过来的,
# 导的base基类里面的初始文件,
# 想修改包名和启动项只需要改base公共类里的包名和启动名
def init_driver(app_Package,app_Activity):
    # 初始化代码,前置代码
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '666666'
    # 支持Toast,吐司,就是弹出特效的文本
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['appPackage'] = app_Package
    desired_caps['appActivity'] = app_Activity

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 创建手机对象
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)