# 元定位
from appium import webdriver
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'     # APP的名字
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)


driver.find_element_by_name("1").click()            # name定位:Node Detail 中的text就是name属性名
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()     # id定位:Node Detail 中的resource-id就是id属性名
driver.find_element_by_class_name("android.widget.Button").click()          # class定位:Node Detail 中的text就是class属性名，很容易相同
driver.find_element_by_name("del").click()
# driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.Button[3]").click() 【出错】      # xpath定位:Node Detail
# driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.Button").click() 【出错】    # xpath定位:Node Detail
driver.find_element_by_xpath("//android.widget.Button[contains(@text,'9')]").click()       # xpath定位:Node Detail
driver.find_element_by_xpath("//android.widget.Button[contains(@text,'5')]").click()             # xpath定位:Node Detail
driver.find_element_by_accessibility_id("plus").click()     # 【拓展方法】 其实，我们的核心是要找到元素的contentDescription属性。它就是元素的 content-desc 。
driver.find_element_by_android_uiautomator("new UiSelector().text(\"6\")").click()      # 【拓展方法】也就是说一个元素的任意属性都可以通过android uiautomator方法来进行定位，但要保证这种定位方式的唯一性。
driver.find_element_by_android_uiautomator("new UiSelector().description(\"equals\")").click()  # 【拓展方法】也就是说一个元素的任意属性都可以通过android uiautomator方法来进行定位，但要保证这种定位方式的唯一性。
# 上面这一条：description对应的是content-desc属性名

# driver.findElement(By.id("com.android.calculator2:id/formula"))
driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_name("delete").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_6").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()

sleep(4)
driver.quit()

