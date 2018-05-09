from appium import webdriver
import time

def testTaobao():
    # 初始化信息
    desired_caps = {}
    desired_caps["platformName"] = "Android"        # 设备系统
    desired_caps["platformVersion"] = "6.0"
    # desired_caps["platformVersion"] = "7.0"         # 设备系统版本
    # desired_caps["deviceName"] = "HuaWeiP9"
    desired_caps["deviceName"] = "MI5"              # 设备名称
    # desired_caps["deviceName"] = "59f88362"
    # desired_caps['app'] = apk_path + '\\app\\shoujibaidu.apk'         # 测试apk包的路径:如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
    desired_caps["appPackage"] = "com.taobao.taobao"            # 包名
    desired_caps["appActivity"] = "com.taobao.tao.homepage.MainActivity3"       # ActivityName
    # desired_caps["appActivity"] = "com.taobao.tao.detail.activity.DetailActivity"
    desired_caps['AppWaitActivity'] = '.ui.startup.role.RoleActivity'       # 试试
    desired_caps["unicodeKeyboard"] = "True"        # 会启用unicodeKeyboard设置的输入法:解决中文输入问题
    desired_caps["resetKeyboard"] = "True"          # 会恢复使用以前的输入法:解决中文输入问题

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
    a = driver.find_element_by_id("com.taobao.taobao:id/searchbtn")
    a.get_attribute()
    a.get_property()

    driver.quit()


def testJingdong():
    # 初始化信息
    desired_caps = {}
    desired_caps["platformName"] = "Android"        # 设备系统
    desired_caps["platformVersion"] = "7.0"         # 设备系统版本
    desired_caps["deviceName"] = "MI5"              # 设备名称
    desired_caps["appPackage"] = "com.jingdong.app.mall"            # 包名
    desired_caps["appActivity"] = "com.jingdong.app.mall.MainFrameActivity"       # ActivityName
    desired_caps["unicodeKeyboard"] = "True"        # 解决中文输入问题
    desired_caps["resetKeyboard"] = "True"          # 解决中文输入问题
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)   # 启动app

    driver.find_element_by_id("qu").click()
    # 等待时间
    time.sleep(3)
    # 进入填写信息页后输入要搜索的内容
    driver.find_element_by_id("layout_horizontal").send_keys("adidas")
    time.sleep(3)
    # 点击搜索按钮
    driver.find_element_by_id("search_btn").click()
    # 截图
    driver.quit()

def testTaobao_HUAWEI():
    # 初始化信息
    desired_caps = {}
    desired_caps["platformName"] = "Android"        # 设备系统
    # desired_caps["platformVersion"] = "6.0"
    desired_caps["platformVersion"] = "7.0"         # 设备系统版本
    # desired_caps["deviceName"] = "HuaWeiP9"
    # desired_caps["deviceName"] = "MI5"              # 设备名称
    desired_caps["deviceName"] = "59f88362"
    # desired_caps['app'] = apk_path + '\\app\\shoujibaidu.apk'         # 测试apk包的路径:如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
    desired_caps["appPackage"] = "com.taobao.taobao"            # 包名
    desired_caps["appActivity"] = "com.taobao.tao.homepage.MainActivity3"       # ActivityName
    # desired_caps["appActivity"] = "com.taobao.tao.detail.activity.DetailActivity"
    desired_caps['AppWaitActivity'] = '.ui.startup.role.RoleActivity'       # 试试
    desired_caps["unicodeKeyboard"] = "True"        # 解决中文输入问题
    desired_caps["resetKeyboard"] = "True"          # 解决中文输入问题
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
# testJingdong()


