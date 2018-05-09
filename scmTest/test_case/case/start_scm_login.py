# 测试登录
import unittest
import re
import time
from scmTest.test_case.public import login
from scmTest.test_case.public.asserts import Asserts
from utils.configs import Configs
from utils.logs import Logs


# 测试登录模块
class Login(unittest.TestCase):
    def setUp(self):
        self.log = Logs.getLogger()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.conf = Configs()   # 创建配置对象
        self.log.info('登录测试初始化完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.log.info('清理登录完成')

    # scm登录测试
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_login(self):
        u"""scm登录测试"""
        log = self.log
        log.info('测试登录')
        data_path = self.conf.getDataPath()              # 获取登录测试数据路径
        file_path = data_path + r'\scm_login\login_data.txt'
        path = self.conf.getScreenshotPath()        # 获取截图路径
        f = open(file_path, "r")
        log.info('已获得测试数据文件')
        ups = []
        try:
            lines = f.readlines()       # 一次性读取整个文件，并安行为单位分成列表
            for line in lines:
                li = re.split(',', line)
                ups.append(li)
        finally:
            f.close()
        log.info('已获得测试数据')
        i = 1
        for up in ups:
            log.info('第 %d 组测试数据' % i)
            i = i + 1
            self.driver = self.conf.getDriver()     # 浏览器对象
            self.base_url = self.conf.getURL()      # 获取URL
            driver = self.driver
            driver.get(self.base_url)
            log.info('已进入登录页面')
            # 调用登录模块
            login.login_test(self, up[0], up[1], up[2])
            time.sleep(2)
            log.info('已调用登录模块,断言登录')
            # 判断是否登录是否正确
            now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
            try:
                e = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/span')
                at = Asserts()      # 创建断言对象
                at.assertText(e, up[3], '账号不匹截图', driver)  # text断言一个元素
            except:
                driver.get_screenshot_as_file(path + '\\' + up[4] + '[' + now_time + '].png')  # 截图操作
                print('登录失败截图成功')
                print(path)
            log.info('断言通过')
            time.sleep(1)
            driver.quit()


if __name__ == "__main__":
    unittest.main()

