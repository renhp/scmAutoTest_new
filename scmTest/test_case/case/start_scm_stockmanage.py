# 库存管理
import unittest
from time import sleep
from scmTest.test_case.public import joinscm
from scmTest.test_case.public import jumplogin
from scmTest.test_case.public.asserts import Asserts
from scmTest.test_case.public.page.stockmanage_page import StockSee
from scmTest.test_case.public.page.stockmanage_page import ExpirYrule
from scmTest.test_case.public.page.stockmanage_page import ExpirWarn
from scmTest.test_case.public.page.stockmanage_page import CategoryRule
from scmTest.test_case.public.page.stockmanage_page import GoodsRule
from scmTest.test_case.public.page.stockmanage_page import ShopStock
from utils.configs import Configs
from utils.readfiles import ExcelReader
from utils.logs import Logs


# 库存管理模块
class StockManage(unittest.TestCase):
    def setUp(self):
        self.logger = Logs.getLogger()
        self.conf = Configs()
        self.driver = self.conf.getDriver()         # 浏览器对象
        self.base_url = self.conf.getURL()          # 获取URL
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
        self.logger.info('初始化库存管理完成')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        self.logger.info('清理库存管理完成')

    # 库存查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_A_stockSee(self):
        u"""scm库存查询"""
        log = self.logger
        log.info('测试库存查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始库存查询测试')
        # 定位“库存管理”
        stokesee = StockSee(driver)  # 创建对象,直接进入库存查询页
        log.info('已进入库存查询模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_stockmanage\stocksee_data.xlsx')
        seevalues = rf.getTestData      # 调用此方法时不需要加括号
        log.info('以获取库存查询测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in seevalues:
            log.info('第 %d 组测试数据' % i)
            i = i + 1
            stokesee.optionWareHouse(v.get("ChangKu"))  # 选择仓库
            stokesee.optionStorageLocation(v.get("KuWei"))  # 选择库位
            # 输入查询条件
            stokesee.inputGoods(v.get("goods"))
            stokesee.inputBrand(v.get("brand"))
            stokesee.inputCategory(v.get("category"))
            log.info('数据输入完成')
            stokesee.clickSee()  # 点击查询
            sleep(1)
            log.info('进行断言')
            # 断言查询是否正确
            es = stokesee.getGoodss()  # 需要的元素很混杂，就写这了
            at.assertAttributes(es, v.get("goodscode"), 'data-goodscode', '库存查询',
                                driver)  # attribute断言一组元素一个断言值【最好用商品编码查，防止模糊查询】
            # at.assertAttribute(es[0], v.get("goodscode"), 'data-goodscode', '库存查询', driver)  # attribute断言一个元素一个断言值
            # at.assertAttributess(es, ts, 'data-goodscode', '库存查询', driver)  # attribute断言一组元素一组断言值,【注意元素个数和断言值每次循环需要一一对应】
            log.info('断言通过')
            stokesee.joinStockSee()  # 再次点击库存查询，以备后期循环查询使用

    # 库存导出
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_B_stockExport(self):
        u"""scm库存导出"""
        log = self.logger
        log.info('测试库存导出')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始库存导出测试')
        # 定位“库存管理”
        stokesee = StockSee(driver)  # 创建对象,直接进入库存查询页
        log.info('已进入库存查询模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_stockmanage\stocksee_data.xlsx')
        see_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('已获取库存导出测试数据')
        i = 1
        for v in see_values:
            log.info('第 %d 组测试数据' % i)
            i = i + 1
            # 选择仓库
            stokesee.optionWareHouse(v.get("ChangKu"))  # 选择仓库
            stokesee.optionStorageLocation(v.get("KuWei"))  # 选择库位
            # 输入查询条件
            stokesee.inputGoods(v.get("goods"))
            stokesee.inputBrand(v.get("brand"))
            stokesee.inputCategory(v.get("category"))
            log.info('已输入测试数据')
            stokesee.clickSee()  # 点击查询
            stokesee.clickExport()     # 点击导出
            log.info('已导出')
            sleep(0.5)
            stokesee.joinStockSee()  # 再次点击库存查询，以备后期循环查询使用

    # 效期规则
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_C_expirYrule(self):
        u"""scm效期规则"""
        log = self.logger
        log.info('测试效期规则')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始效期规则测试')
        # 定位“库存管理”
        expiryrule = ExpirYrule(driver)          # 创建效期规则对象，同时进入效期规则页面
        log.info('已进入效期规则模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_stockmanage\expiryrule_data.xlsx')
        expir_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('以获取效期规则测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in expir_values:
            log.info('第 %d 组测数据' % i)
            i = i + 1
            expiryrule.optionWareHouse(v.get("ChangKu"))    # 选择仓库
            expiryrule.inputGoods(v.get("goods"))         # 输入商品名称
            log.info('已输入测试数据')
            expiryrule.clickSee()               # 点击查询
            sleep(1)
            expiryrule.clickEdit()              # 点击编辑
            log.info('已进入编辑效期页面')
            sleep(1.5)
            expiryrule.inputDueData_Yellow(v.get("DueYellow"))      # 效期值_黄色
            expiryrule.inputDueData_Red(v.get("DueRed"))            # 效期值_红色
            log.info('已输入效期数据')
            sleep(0.5)
            expiryrule.clickEnsure()                # 点击确认，提交编辑数据
            sleep(1)
            log.info('判断是否设置成功')
            # 判断是否设置成功，若失败则截图
            e = expiryrule.getAssertElemente()      # 获取弹框中的断言元素
            at.assertText(e, v.get("AssertValue"), '效期设置失败截图', driver)  # text断言一个元素
            log.info('断言通过')
            expiryrule.clickClose()     # 点击关闭弹框
            sleep(0.5)
            expiryrule.joinExpirYrule()


    # 效期预警
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_D_expirWarn(self):
        u"""scm效期预警"""
        log = self.logger
        log.info('测试效期预警')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始效期预警测试')
        # 定位“库存管理”
        expirwarn = ExpirWarn(driver)
        log.info('已进入效期预警模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_stockmanage\expirwarn_data.xlsx')
        expir_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('已获取效期预警测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for ev in expir_values:
            log.info('第 %d 组测试数据' % i)
            i = i + 1
            expirwarn.optionWareHouse(ev.get('ChangKu'))            # 选择仓库
            expirwarn.inputGood(ev.get('goods'))                    # 输入商品名称
            expirwarn.inputShop(ev.get('shopName'))                 # 输入货柜
            expirwarn.optionSign(ev.get('colour'))                  # 选择颜色
            log.info('已输入测试数据')
            expirwarn.clickSee()                            # 点击查询
            sleep(1.5)
            log.info('断言测试')
            # 断言查询商品名称
            es = expirwarn.getGoods()
            av = ev.get('assert_code') + '\n' + ev.get('assert_goods')     # 获取断言数据
            at.assertTexts(es, av, '效期预警', driver)      # text断言一组元素一个断言值
            # at.assertTextss(es, rs, '效期预警', driver)        # text断言一组元素一组断言值
            # at.assertText(e, r, '效期预警', driver)      # text断言一个元素
            log.info('断言通过')
            sleep(1)
            expirwarn.joinExpirWarn()            # 定位效期预警

    # 下架规则_类目
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_1E_categoryRule(self):
        u"""scm下架规则_类目"""
        log = self.logger
        log.info('测试下架规则_类目')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始下架规则_类目测试')
        # 定位“下架规则”
        category_rule = CategoryRule(driver)
        log.info('已进入下架规则_类目模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_stockmanage\categoryrule_data.xlsx')
        rule_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('已获取效期预警测试数据')
        i = 1
        for rv in rule_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            category_rule.inputCategory(rv.get('category'))     # 输入类目
            category_rule.clickSee()        # 点击查询
            log.info('已进行查询')
            sleep(0.5)
            category_rule.clickPlus()       # 点击“+”展开明细
            rule1 = category_rule.getRule(rv.get('ChangKuCode'))    # 获取已有的规则值
            category_rule.optionClickEdit(rv.get('ChangKuCode'))    # 点击编辑所选仓库
            log.info('已进入设置下架下架规则弹框')
            sleep(0.5)
            category_rule.setRule(rv.get('Week'), rv.get('Rule'))   # 设置下架规则
            category_rule.clickSave()                               # 点击保存
            log.info('已设置完成')
            sleep(2.5)
            rule2 = category_rule.getRule(rv.get('ChangKuCode'))    # 获取新的规则值
            log.info('开始断言')
            at = Asserts()  # 创建断言对象
            at.assertChangeText(rv.get('Week1') + rv.get('Rule'), rule1, rule2, '下架规则_类目', driver)  # 断言
            log.info('断言通过')
            category_rule.joinCategoryRule()      # 重新进行下架规则_类目页面

    # 下架规则_商品
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_1F_goodsRule(self):
        u"""scm下架规则_商品"""
        log = self.logger
        log.info('测试下架规则_商品')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始下架规则_商品测试')
        # 定位“下架规则”
        goods_rule = GoodsRule(driver)
        log.info('已进入下架规则_类目模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_stockmanage\goodsrule_data.xlsx')
        rule_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('已获取效期预警测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for rv in rule_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            goods_rule.inputGoods(rv.get('Goods'))      # 输入商品
            goods_rule.clickSee()       # 点击查询
            log.info('已进行查询')
            goods_rule.clickPlus()      # 点击“+”号
            rule1 = goods_rule.getRule(rv.get('ChangKuCode'))               # 获取已有规则
            goods_rule.optionClickEdit(rv.get('ChangKuCode'))       # 点击对应仓库下的编辑
            log.info('已进入下架规则设置弹框')
            sleep(0.5)
            goods_rule.setRule(rv.get('Week'), rv.get('Rule'))                      # 设置规则
            goods_rule.clickSave()      # 点击保存
            log.info('已设置完成')
            sleep(1)
            rule2 = goods_rule.getRule(rv.get('ChangKuCode'))  # 获取新规则
            log.info('开始断言')
            at.assertChangeText(rv.get('Week1') + rv.get('Rule'), rule1, rule2, '下架规则_商品', driver)   # 断言
            log.info('断言通过')
            # 无需重新进入

    # 货柜库存_查询
    # @unittest.skip("跳过这条用例执行")    # 跳过这个用例
    def test_1F_shopStockSee(self):
        u"""scm货柜库存_查询"""
        log = self.logger
        log.info('测试货柜库存_查询')
        driver = self.driver
        driver.get(self.base_url)
        jumplogin.jumpLogin(self)  # 跳过登录，跳过验证码,若已有cookie信息已过期则调用等模块
        log.info('已跳过登录')
        joinscm.joinScm(self)  # 进入scm
        joinscm.joinScmIframe(self)  # 跳入scm_iframe
        log.info('已进入scm_iframe')
        """========开始测试内容====================================================="""
        log.info('开始货柜库存_查询测试')
        # 定位“下架规则”
        shop_stock = ShopStock(driver)
        log.info('已进入货柜库存模块')
        # 获取测试用例数据（需要传入测试用例数据文件再各环境中的测试目录）
        rf = ExcelReader(r'\scm_stockmanage\ShopStockSee_data.xlsx')
        shop_stock_values = rf.getTestData  # 调用此方法时不需要加括号
        log.info('已获取效期预警测试数据')
        i = 1
        at = Asserts()  # 创建断言对象
        for v in shop_stock_values:
            log.info('第 %d 组测试数据' % i)
            i += 1
            shop_stock.inputGoods(v.get('Goods'))
            shop_stock.inputShop(v.get('Shop'))
            shop_stock.inputBrand(v.get('Brand'))
            shop_stock.inputCategory(v.get('Category'))
            shop_stock.optionCity(v.get('City'))
            shop_stock.optionShopType(v.get('ShopType'))
            shop_stock.optionShopStatus(v.get('ShopStatus'))
            shop_stock.clickSee()
            log.info('已查询到货柜库存')
            sleep(0.5)
            goodsNames = shop_stock.getGoodsName()
            assert_value = v.get('Assert1') + '\n' + v.get('Assert2')
            at.assertTexts(goodsNames, assert_value, '货柜库存查询', driver)
            sleep(1)
            shop_stock.joinShopStock()







"""【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【【"""
if __name__ == "__main__":
    unittest.main()


