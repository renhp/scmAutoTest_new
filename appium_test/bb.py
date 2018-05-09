# app自动化
from appium import webdriver
from selenium.webdriver import DesiredCapabilities

# capabilities = DesiredCapabilities()
'''用于指导测试环境'''
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = "WINDOWS"  # 指定操作系统
capabilities['version'] = "10"   # 指定操作系统版本
print('===', capabilities)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
print(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()

driver.quit()


