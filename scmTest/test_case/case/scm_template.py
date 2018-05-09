# 模板，后期直接复制该文件
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs




class Aa(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()  # 浏览器对象
        self.base_url = self.conf.getURL()  # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化测试模板完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理测试模板完成')

    # 测试名字
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_template(self):
        u"""测试模板"""
        log = self.logger
        log.info('测试测试模板')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始进行测试')

        sleep(5)




if __name__ == "__main__":
    unittest.main()


