# 调整用例脚本结构，使用外部函数setUpModule()和tearDownModule()启动、关闭浏览器等，提高整体运行时间
import time
from selenium import webdriver
import unittest

driver_a = None
def setUpModule():
    print("整个文件开始时执行")
    global driver_a
    driver_a = webdriver.Chrome()
    driver_a.implicitly_wait(20)
    driver_a.maximize_window()

def tearDownModule():
    print("整个文件结束时执行")
    global driver_a
    driver_a.quit()

class Test(unittest.TestCase):

    # # 整个Test类开始时执行
    # @classmethod
    # def setUpClass(cls):
    #     print("整个Test类开始时执行")
    #     Test.driver_a = webdriver.Chrome()

    # # 整个Test类结束时执行
    # @classmethod
    # def tearDownClass(cls):
    #     print("整个Test类结束时执行")
    #     Test.driver_a.quit()

    # 每个用例的开始时执行
    def setUp(self):
        self.driver = driver_a
        print("====", type(self.driver), "===", self.driver)
        print("开始用例")

    # # 每个用例的结束时执行
    def tearDown(self):
        print("结束用例")

    def test_case1(self):
        print("用例1")
        self.driver.get("http://www.baidu.com")
        time.sleep(5)
        raise NameError("哈哈哈")

    def test_case2(self):
        print("用例2")
        self.driver.get("https://blog.csdn.net/huilan_same/article/details/52329804")
        time.sleep(5)


class Test2(unittest.TestCase):
    # 每个用例的开始时执行
    def setUp(self):
        self.driver = driver_a
        print("====", type(self.driver), "===", self.driver)
        print("开始用例")

    # # 每个用例的结束时执行
    def tearDown(self):
        print("结束用例")

    def test_case1(self):
        print("用例1")
        self.driver.get("http://www.baidu.com")
        time.sleep(3)

    def test_case2(self):
        print("用例2")
        self.driver.get("https://blog.csdn.net/huilan_same/article/details/52329804")
        time.sleep(3)



if __name__ == "__main__":
    unittest.main()
