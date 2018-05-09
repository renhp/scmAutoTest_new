# 报损管理模块
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from scmTest.test_case.public.page.scm_warehouse_manage.breakagemanage_page import BreakageManagePage
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs



# 报损管理
class BreakageManage(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()  # 浏览器对象
        self.base_url = self.conf.getURL()  # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化报损管理完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理报损管理完成')

    # 报损管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_breakageManage_see(self):
        u"""scm报损管理_查询"""
        log = self.logger
        log.info('测试报损管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始报损管理_查询测试')
        # 定位“报损管理”
        breakageManage = BreakageManagePage(driver)
        log.info('已进入报损管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_warehouse_manage\BreakageManage\BreakageManageSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取报损管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            breakageManage.optionWarehouse(v.get('warehouseCode'))
            breakageManage.optionAuditState(v.get('auditStatus'))
            breakageManage.optionStockRemovalState(v.get('outStatus'))
            breakageManage.inputBreakageNumber(v.get('BreakageNumber'))
            breakageManage.clickSee()
            sleep(1)
            es = breakageManage.getBreakageNumbers()
            at.assertTexts(es, v.get('BreakageNumber'), '报损管理_查询', driver)
            breakageManage.joinBreakageManage()
            sleep(0.5)





if __name__ == "__main__":
    unittest.main()


