# 测试混合型APP：如：淘宝，京东
import unittest,time
from appium import webdriver


def testTaobao():
    # 初始化信息
    desired_caps = {}
    desired_caps["platformName"] = "Android"  # 设备系统
    desired_caps["platformVersion"] = "6.0"
    desired_caps["deviceName"] = "59f88362"
    desired_caps["appPackage"] = "com.taobao.taobao"  # 包名
    desired_caps["appActivity"] = "com.taobao.tao.homepage.MainActivity3"  # ActivityName
    desired_caps["unicodeKeyboard"] = "True"  # 会启用unicodeKeyboard设置的输入法:解决中文输入问题
    desired_caps["resetKeyboard"] = "True"  # 会恢复使用以前的输入法:解决中文输入问题
    desired_caps["automationName"] = "Selendroid"   # 混合型APP特有的

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)   # 启动app

    driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
    # 等待时间
    time.sleep(3)
    # 进入填写信息页后输入要搜索的内容
    driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("adidas")
    time.sleep(3)
    # 点击搜索按钮
    driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
    # 截图
    driver.quit()

testTaobao()

