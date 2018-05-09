# 调拨管理模块
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from scmTest.test_case.public.page.scm_warehouse_manage.allotmanage_page import AllotManagePage
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs



# 调拨管理
class AllotManage(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()  # 浏览器对象
        self.base_url = self.conf.getURL()  # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化调拨管理完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理调拨管理完成')

    # 调拨管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_allotManageSee(self):
        u"""scm调拨管理_查询"""
        log = self.logger
        log.info('测试调拨管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始调拨管理_查询测试')
        # 定位“调拨管理”
        allotManage = AllotManagePage(driver)
        log.info('已进入调拨管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_warehouse_manage\AllotManage\AllotManageSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取调拨管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            allotManage.optionOutWarehouse(v.get('OutWarehouse'))
            allotManage.optionOutStorageLocation(v.get('OutStorageLocation'))
            allotManage.optionJoinWarehouse(v.get('JoinWarehouse'))
            allotManage.optionJoinStorageLocation(v.get('JoinStorageLocation'))
            allotManage.optionAllotType(v.get('AllotType'))
            allotManage.inputAllotNumber(v.get('AllotNumber'))
            allotManage.optionAllotNumberState(v.get('AllotNumberState'))
            allotManage.optionOutPutState(v.get('OutPutState'))
            log.info('已输入完信息')
            allotManage.clickSee()
            sleep(1)
            log.info('获取短信信息')
            es = allotManage.getAllotNumbers()
            log.info('开始断言')
            at.assertValueInTexts(es, v.get('OutWarehouse'), '调拨管理查询_调出仓库', driver)
            at.assertValueInTexts(es, v.get('OutStorageLocation'), '调拨管理查询_调出仓库', driver)
            at.assertValueInTexts(es, v.get('JoinWarehouse'), '调拨管理查询_调入仓库', driver)
            at.assertValueInTexts(es, v.get('JoinStorageLocation'), '调拨管理查询_调入库位', driver)
            at.assertValueInTexts(es, v.get('AllotNumber'), '调拨管理查询_调拨单号', driver)
            log.info('断言通过')
            allotManage.joinAllotManage()
            sleep(0.5)




if __name__ == "__main__":
    unittest.main()


