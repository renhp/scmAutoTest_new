# 模板，后期直接复制该文件
import unittest
import time
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs
from scmTest.test_case.public.page.supplychainmanage_page import AddressManage
from scmTest.test_case.public.page.supplychainmanage_page import RadiateManage


# 供应链管理模块
class SupplyChainManage(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()  # 浏览器对象
        self.base_url = self.conf.getURL()  # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化供应链管理完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理供应链管理完成')

    # 地点管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_locationManageSee(self):
        u"""scm地点管理_查询"""
        log = self.logger
        log.info('测试地点管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始地点管理_查询测试')
        # 定位“库存管理”
        addressmanage = AddressManage(driver)  # 创建对象,直接进入页面
        log.info('已进入地点管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_SupplyChainManage\LocationManageSee_data.xlsx')
        seevalues = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取地点管理_查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in seevalues:
            log.info('第 %d 组测试数据' % i)
            i += 1
            addressmanage.optionWarehouse(v.get('Warehouse'))       # 选择仓库
            addressmanage.optionCity(v.get('City'))                 # 选择城市
            log.info('已输入完查询信息')
            addressmanage.clickSee()            # 点击查询
            sleep(1.5)
            e = addressmanage.getWarehouse()       # 获取查询结果中的仓库元素
            log.info('已输查询到信息，开始断言')
            av = v.get('AssertValue1') + '\n' + v.get('AssertValue2')       # 拼接断言值
            print(av)
            at.assertText(e, av, '地点管理_查询', driver)
            log.info('断言通过')
            sleep(1)
            addressmanage.joinAddressManage()       # 再次进入地址管理页面

    # 地点管理_编辑
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_B_locationManageEdit(self):
        u"""scm地点管理_编辑"""
        log = self.logger
        log.info('测试地点管理_编辑')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始地点管理_编辑测试')
        # 定位“库存管理”
        addressmanage = AddressManage(driver)  # # 创建对象,直接进入页面
        log.info('已进入地点管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_SupplyChainManage\LocationManageEdit_data.xlsx')
        edit_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取地点管理_编辑测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in edit_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            addressmanage.optionWarehouse(v.get('Warehouse'))  # 选择仓库
            log.info('已输入完查询信息')
            addressmanage.clickSee()        # 点击查询
            sleep(0.5)                      # 必须有
            addressmanage.clickEdit()       # 点击编辑
            log.info('已进入编辑弹框')
            addressmanage.inputContactMan(v.get('ContactMan'))      # 输入联系人
            addressmanage.inputTelephone(v.get('inputTelephone'))   # 输入电话
            addressmanage.clickSave()       # 点保存
            sleep(1)      # 必须加等待时间，因为元素以存在，当时内容为空，等待一会才有内容
            e = addressmanage.getAlertInfoElement()    # 获取操作提示信息元素
            log.info('已编辑完成，开始断言')
            at.assertText(e, '操作成功!', '地点管理_编辑', driver)
            log.info('断言通过')
            sleep(0.5)
            addressmanage.clickClose()      # 关闭提示信息弹框
            sleep(0.5)
            addressmanage.joinAddressManage()  # 再次进入地址管理页面

    # 地点管理_新增
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_C_locationManageNewAddress(self):
        u"""scm地点管理_编辑"""
        log = self.logger
        log.info('测试地点管理_新增')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始地点管理_新增测试')
        # 定位“库存管理”
        addressmanage = AddressManage(driver)  # 创建对象,直接进入页面
        log.info('已进入地点管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_SupplyChainManage\LocationManageNewAddress_data.xlsx')
        edit_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取地点管理_新增测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in edit_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            addressmanage.clickNewAddress()     # 点击“新增地点”
            log.info('已进入新增弹框，开始填写信息')
            now_time = time.strftime("%M%S", time.localtime())  # 获取当前系统时间
            AddressCode = v.get('AddressCode') + now_time       # 拼接仓库编码
            AddressName = v.get('AddressName') + now_time       # 拼接仓库名称
            # print(AddressCode)
            addressmanage.inputAddressCode(AddressCode)
            addressmanage.inputAddressName(AddressName)
            addressmanage.inputWarehouseAddress(v.get('WarehouseAddress'))
            addressmanage.inputContactMan(v.get('ContactMan'))
            addressmanage.inputTelephone(v.get('Telephone'))
            addressmanage.optionProvinceNewAdd(v.get('ProvinceNewAdd'))
            addressmanage.optionCityNewAdd(v.get('CityNewAdd'))
            addressmanage.optionCountyNewAdd(v.get('CountyNewAdd'))
            addressmanage.clickYes()     # 设为可用
            sleep(0.5)
            addressmanage.clickSave()
            sleep(0.5)  # 必须加等待时间，因为元素以存在，当时内容为空，等待一会才有内容
            e = addressmanage.getAlertInfoElement()  # 获取操作提示信息元素
            log.info('已新增完成，开始断言')
            at.assertText(e, '操作成功!', '地点管理_编辑', driver)
            log.info('断言通过')
            sleep(0.5)
            addressmanage.clickClose()      # 关闭提示信息弹框
            sleep(0.5)
            addressmanage.joinAddressManage()  # 再次进入地址管理页面

    # 地点管理_查询明细
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_D_locationManageSeeDetail(self):
        u"""scm地点管理_查询明细"""
        log = self.logger
        log.info('测试地点管理_查询明细')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始地点管理_查询明细测试')
        # 定位“库存管理”
        addressmanage = AddressManage(driver)  # 创建对象,直接进入页面
        log.info('已进入地点管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_SupplyChainManage\LocationManageSee_data.xlsx')
        seeDetail_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取地点管理_查询明细测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in seeDetail_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            Warehouse = v.get('Warehouse')
            addressmanage.optionWarehouse(Warehouse)  # 选择仓库
            # addressmanage.optionProvince(v.get('Province'))  # 选择省份
            addressmanage.optionCity(v.get('City'))  # 选择城市
            log.info('已输入完查询信息')
            addressmanage.clickSee()            # 点击查询
            sleep(0.5)
            addressmanage.clickSeeDetail()      # 点击查看明细
            sleep(1)
            e = addressmanage.inputAddressName()    # 获取地址名称元素：不传值时，返回元素
            log.info('已查询到明细，开始断言')
            at.assertAttribute(e, Warehouse, 'value', '地点管理_查询明细', driver)
            log.info('断言通过')
            addressmanage.clickCancel()         # 点击取消，便于下一组测试数据测试
            log.info('已点几取消')
            sleep(1)
            addressmanage.joinAddressManage()  # 再次进入地址管理页面

    # 辐射管理_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_E_radiateManageSee(self):
        u"""scm辐射管理_查询"""
        log = self.logger
        log.info('测试辐射管理_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始辐射管理_查询测试')
        # 定位“库存管理”
        radiateManage = RadiateManage(driver)
        log.info('已进入地点管理模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_SupplyChainManage\RadiateManageSee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取地点管理_查询明细测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            radiateManage.optionWarehouse(v.get('Warehouse'))
            radiateManage.inputShop(v.get('ShopName'))
            radiateManage.optionCity(v.get('City'))
            radiateManage.optionShopType(v.get('ShopType'))
            radiateManage.optionShopState(v.get('ShopState'))
            log.info('已输入信息，开始查询')
            radiateManage.clickSee()
            sleep(1)
            e = radiateManage.getShopName()
            log.info('已查询到结果，开始断言')
            at.assertText(e, v.get('ShopName'), '辐射管理_查询', driver)
            log.info('断言通过')
            sleep(1)
            radiateManage.joinRadiateManage()





"""【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【"""
if __name__ == "__main__":
    unittest.main()















