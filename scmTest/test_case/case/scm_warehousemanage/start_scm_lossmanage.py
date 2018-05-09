# 模板，后期直接复制该文件
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from scmTest.test_case.public.page.scm_warehouse_manage.breakagemanage_page import BreakageManagePage
from scmTest.test_case.public.page.scm_warehouse_manage.lossmanage_page import LossManagePage
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs



# 损益管理
class LossManage(unittest.TestCase):
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

    # 损益管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_lossManageSee(self):
        u"""scm损益管理_查询"""
        log = self.logger
        log.info('测试损益管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始损益管理_查询测试')
        # 定位“损益管理”
        lossManage = LossManagePage(driver)
        log.info('已进入损益管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_warehouse_manage\LossManage\LossManageSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取损益管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            lossManage.optionWarehouse(v.get('Warehouse'))
            lossManage.inputShop(v.get('Shop'))
            lossManage.inputReplenishNumber(v.get('ReplenishNumber'))
            lossManage.clickSee()
            sleep(1)
            log.info('查询到信息，开始断言')
            es = lossManage.getWarehouses()
            at.assertValueInTexts(es, v.get('Warehouse'), '损益管理查询_仓库', driver)
            es2 = lossManage.getShops()
            at.assertValueInTexts(es2, v.get('Shop'), '损益管理查询_货柜', driver)
            es3 = lossManage.getReplenishNumbers()
            at.assertValueInTexts(es3, v.get('ReplenishNumber'), '损益管理查询_需求单号', driver)
            log.info('断言通过')
            lossManage.joinLossManage()
            sleep(0.5)




if __name__ == "__main__":
    unittest.main()


