# 其他出库模块
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from scmTest.test_case.public.page.scm_warehouse_manage.otherOutbound_page import OtherOutboundPage
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs



# 其他出库
class OtherOutbound(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()  # 浏览器对象
        self.base_url = self.conf.getURL()  # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化其他出库完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理其他出库完成')

    # 其他出库_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_OtherOutboundSee(self):
        u"""scm其他出库_查询"""
        log = self.logger
        log.info('测试其他出库_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始其他出库_查询测试')
        # 定位“其他出库”
        otherOutbound = OtherOutboundPage(driver)
        log.info('已进入损益管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_warehouse_manage\OtherOutbound\OtherOutboundSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取损益管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            otherOutbound.optionWarehouse(v.get('Warehouse'))
            otherOutbound.optionCheckState(v.get('CheckState'))
            otherOutbound.optionStockRemovalState(v.get('StockRemovalState'))
            otherOutbound.inputOtherOrderNumber(v.get('OtherOrderNumber'))
            otherOutbound.clickSee()
            sleep(1)
            log.info('开始断言')
            es1 = otherOutbound.getOtherOrderNumbers()
            at.assertValueInTexts(es1, v.get('OtherOrderNumber'), '其他出库查询_单号', driver)
            es2 = otherOutbound.getCheckStates()
            at.assertValueInTexts(es2, v.get('CheckState'), '其他出库查询_审核状态', driver)
            es3 = otherOutbound.getStockRemovalStates()
            at.assertValueInTexts(es3, v.get('StockRemovalState'), '其他出库查询_出库状态', driver)
            es4 = otherOutbound.getWarehouses()
            at.assertValueInTexts(es4, v.get('Warehouse'), '其他出库查询_仓库', driver)
            log.info('断言通过')
            otherOutbound.joinOtherOutbound()



if __name__ == "__main__":
    unittest.main()


