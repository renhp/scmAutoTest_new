# 补货管理模块
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from scmTest.test_case.public.page.scm_warehouse_manage.replenishManage_page import ReplenishManagePage
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs


# 补货管理
class ReplenishManage(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()  # 浏览器对象
        self.base_url = self.conf.getURL()  # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化补货管理完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理补货管理完成')

    # 补货管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_ReplenishManageSee(self):
        u"""scm补货管理_查询"""
        log = self.logger
        log.info('测试补货管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始补货管理_查询测试')
        # 定位“补货管理”
        replenishManage = ReplenishManagePage(driver)
        log.info('已进入补货管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_warehouse_manage\ReplenishManage\ReplenishManageSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取补货管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            replenishManage.optionWarehouse(v.get('Warehouse'))
            replenishManage.inputReplenishNumber(v.get('ReplenishNumber'))
            replenishManage.inputOutboundNumber(v.get('OutboundNumber'))
            replenishManage.inputShop(v.get('Shop'))
            replenishManage.optionState(v.get('State'))
            replenishManage.clickSee()
            sleep(1)
            log.info('开始断言')
            es1 = replenishManage.getReplenishNumbers()
            at.assertValueInTexts(es1, v.get('ReplenishNumber'), '补货管理查询_需求单号', driver)
            es2 = replenishManage.getOutboundNumbers()
            at.assertValueInTexts(es2, v.get('OutboundNumber'), '补货管理查询_波次单号', driver)
            es3 = replenishManage.getWareHouses()
            at.assertValueInTexts(es3, v.get('Warehouse'), '补货管理查询_仓库', driver)
            es5 = replenishManage.getShops()
            at.assertValueInTexts(es5, v.get('Shop'), '补货管理查询_货柜', driver)
            es6 = replenishManage.getStates()
            at.assertValueInTexts(es6, v.get('State'), '补货管理查询_状态', driver)
            log.info('断言通过')
            replenishManage.joinReplenishManage()




if __name__ == "__main__":
    unittest.main()



