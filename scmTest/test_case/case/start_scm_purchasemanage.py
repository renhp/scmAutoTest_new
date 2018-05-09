# 采购管理模块
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from scmTest.test_case.public.page.PurchaseManage_page import OrderManagePage
from scmTest.test_case.public.page.PurchaseManage_page import SalesReturnManagePage
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs



# 采购管理模块
class PurchaseManage(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()  # 浏览器对象
        self.base_url = self.conf.getURL()  # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化采购管理完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理采购管理完成')

    # 订单管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_OrderManageSee(self):
        u"""scm订单管理_查询"""
        log = self.logger
        log.info('测试订单管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始订单管理_查询测试')
        # 定位“订单管理”
        orderManage = OrderManagePage(driver)
        log.info('已进入订单管理页面')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_PurchaseManage\OrderManageSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取订单管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            orderManage.inputOrderNumber(v.get('OrderNumber'))
            orderManage.optionWarehouse(v.get('Warehouse'))
            orderManage.optionStorageLocation(v.get('StorageLocation'))
            orderManage.inputSupplier(v.get('Supplier'))
            orderManage.optionInventoryState(v.get('InventoryState'))
            orderManage.inputBuyer(v.get('Buyer'))
            orderManage.optionOrderState(v.get('OrderState'))
            orderManage.clickSee()
            sleep(1)
            log.info('开始断言')
            es1 = orderManage.getOrderBasicInfors()
            at.assertValueInTexts(es1, v.get('OrderNumber'), '订单管理查询_采购单号', driver)
            at.assertValueInTexts(es1, v.get('Warehouse'), '订单管理查询_仓库', driver)
            at.assertValueInTexts(es1, v.get('StorageLocationAssert'), '订单管理查询_库位', driver)
            at.assertValueInTexts(es1, v.get('Supplier'), '订单管理查询_供应商', driver)
            es2 = orderManage.getStates()
            at.assertValueInTexts(es2, v.get('InventoryState'), '订单管理查询_入库状态', driver)
            at.assertValueInTexts(es2, v.get('OrderState'), '订单管理查询_订单状态', driver)
            es3 = orderManage.getOthers()
            at.assertValueInTexts(es3, v.get('Buyer'), '订单管理查询_采购员', driver)
            log.info('断言通过')
            orderManage.joinOrderManagePage()

    # 退货管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_B_SalesReturnManageSee(self):
        u"""scm退货管理_查询"""
        log = self.logger
        log.info('测试退货管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始退货管理_查询测试')
        # 定位“退货管理”
        salesReturnManage = SalesReturnManagePage(driver)
        log.info('已进入退货管理页面')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_PurchaseManage\OrderManageSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取退货管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1



if __name__ == "__main__":
    unittest.main()


