# 库存管理模块页面
from scmTest.test_case.public.page import joinmodule
from scmTest.test_case.public.page import elementaction
from selenium.webdriver.support.ui import WebDriverWait
from scmTest.test_case.public import await_ele

"""【==========库存查询，页面元素==============】"""
class StockSee():

    # 创建对象是直接进入“库存查询页面”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list4")        # 进入“库存管理”模块:库存管理的‘for’属性值为“list4”
        e = self.driver.find_element_by_link_text("库存查询")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“库存查询”页面
    def joinStockSee(self, action=None):
        e = self.driver.find_element_by_link_text("库存查询")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 选择“仓库”
    def optionWareHouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_id("wareHouse")
        await_ele.judgeEle(e)           # 点击仓库下拉框
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@id="wareHouse"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 选择“库位”
    def optionStorageLocation(self, StorageLocation=None):    # 传入库位名
        e = self.driver.find_element_by_id("library")
        await_ele.judgeEle(e)       # 点击库位
        # # 选择库位
        storageLocations = self.driver.find_elements_by_xpath(r'//select[@id="library"]/option')
        if StorageLocation is None or StorageLocation == "":       # 如果没有传入库位或传的是'""'则直接返回库位名组
            return storageLocations
        elementaction.dropDownBox_text(self, storageLocations, StorageLocation)     # 选择库位名

    # 输入“商品”
    def inputGoods(self, Goods=None):
        e = self.driver.find_element_by_id("goodsCodeOrName")
        if Goods is None or Goods == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)
        elementaction.inputContent(self, e, Goods)      # 输入商品

    # 输入"品牌"
    def inputBrand(self, Brand=None):
        e = self.driver.find_element_by_id("brandCodeOrName")
        if Brand is None or Brand == '':           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)
        elementaction.inputContent(self, e, Brand)  # 输入品牌

    # 输入“类目”
    def inputCategory(self, Category=None):     # 传入类目
        e = self.driver.find_element_by_id("categoryCodeOrName")
        if Category is None or Category == "":        # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)
        elementaction.inputContent(self, e, Category)  # 输入类目

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id("search")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 点击“导出”
    def clickExport(self, action=None):
        e = self.driver.find_element_by_id("export")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取“列表中的商品”
    def getGoodss(self):
        es = self.driver.find_elements_by_xpath('//*[@id="renderList"]/tr/td[1]/a')  # 需要的元素很混杂，就写这了
        return es



"""【==========效期规则，页面元素==============】"""
class ExpirYrule():

    # 创建对象是直接进入“效期规则页面”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list4")            # 进入“库存管理”模块:库存管理的‘for’属性值为“list4”
        e = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_link_text("效期规则"))
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“效期规则”页面
    def joinExpirYrule(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("效期规则")
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“仓库”
    def optionWareHouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_id("warehouseCode")     # 获取仓库下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//*[@id="warehouseCode"]/option')
        if WareHouse is not None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 输入“商品”
    def inputGoods(self, Goods=None):
        e = self.driver.find_element_by_id("shopName")
        if Goods is None or Goods == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Goods)      # 输入商品

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id("search")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 点击“编辑”
    def clickEdit(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="renderList"]/tr[1]/td[10]/a')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 输入“黄色到期日期”
    def inputDueData_Yellow(self, Due=None):
        e = self.driver.find_element_by_xpath('//*[@id="editBox"]/div/div/div[2]/div/p[2]/input')
        if Due is None or Due == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Due)      # 输入商品

    # 输入“红色到期日期”
    def inputDueData_Red(self, Due=None):
        e = self.driver.find_element_by_xpath('//*[@id="editBox"]/div/div/div[2]/div/p[3]/input')
        if Due is None or Due == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Due)      # 输入商品

    # 点击“确定”
    def clickEnsure(self, action=None):
        e = self.driver.find_element_by_id('submmit')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 点击“取消”
    def clickCancel(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="editBox"]/div/div/div[2]/div/div/button[2]/span')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 获取“弹框中的断言元素”
    def getAssertElemente(self):
        e = self.driver.find_element_by_xpath('//*[@id="tomatoAlert"]/div/h4')
        return e

    # 点击“关闭”
    def clickClose(self, action=None):
        es = self.driver.find_elements_by_xpath('//*[@id="alert"]/div/div/div[3]/button')
        for e in es:
            if e.text == '关闭':
                if action is not None:
                    return e
                await_ele.judgeEle(e)  # 点击元素
                break



"""【==========效期预警，页面元素==============】"""
class ExpirWarn():

    # 创建对象是直接进入“效期预警页面”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list4")  # 进入“库存管理”模块:库存管理的‘for’属性值为“list4”
        e = self.driver.find_element_by_link_text("效期预警")
        await_ele.judgeEle(e, second=20)        # 点击元素

    # 进入“效期预警”页面
    def joinExpirWarn(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("效期预警")
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e, second=20)  # 点击元素

    # 选择“仓库”
    def optionWareHouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_id("warehouseCode")     # 获取仓库下拉框元素
        await_ele.judgeEle(e, second=20)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//*[@id="warehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 输入“商品”
    def inputGood(self, Goods=None):
        e = self.driver.find_element_by_name("goods")
        if Goods is None or Goods == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e, second=20)  # 点击元素
        elementaction.inputContent(self, e, Goods)      # 输入商品

    # 输入“货柜”
    def inputShop(self, Shops=None):
        e = self.driver.find_element_by_name("shop")
        if Shops is None or Shops == '':           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e, second=20)  # 点击元素
        elementaction.inputContent(self, e, Shops)      # 输入商品

    # 选择“标记”颜色
    def optionSign(self, Sign=None):  # 传入标记
        e = self.driver.find_element_by_name("sign")     # 获取标记下拉框元素
        await_ele.judgeEle(e, second=20)  # 点击元素
        # 获取标记名组
        Signs = self.driver.find_elements_by_xpath(r'//*[@name="sign"]/option')
        if Sign is None or Sign == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return Sign
        elementaction.dropDownBox_text(self, Signs, Sign)     # 选择仓库名

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id("search")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e, second=20)  # 点击元素

    # 点击“导出”
    def clickExport(self, action=None):
        e = self.driver.find_element_by_id("export")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e, second=20)  # 点击元素

    # 获取查询列表中的商品组(断言时用
    def getGoods(self):
        es = self.driver.find_elements_by_xpath('//*[@id="renderList"]/tr/td[1]')
        return es

    # 获取查询列表中的仓库

    # 获取查询列表中的货柜

    # 获取查询列表中的标记颜色



"""【==========下架规则_类目，页面元素==============】"""
class CategoryRule():

    # 创建对象是直接进入“下架规则_类目”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list4")  # 进入“库存管理”模块:库存管理的‘for’属性值为“list4”
        e = self.driver.find_element_by_link_text("下架规则")
        await_ele.judgeEle(e, second=20)  # 进入“下架规则_类目”页面

    # 进入“下架规则_类目”页面
    def joinCategoryRule(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("下架规则")
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)       # 点击元素

    # 输入“类目”
    def inputCategory(self, Category=None):  # 传入类目
        e = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_name("categorySecondCode"))
        if Category is None or Category == "":  # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Category)  # 输入类目

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id("search")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 点击“加号”
    def clickPlus(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="renderList"]/tr[1]/td[1]/label')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 获取规则值(值为周一至周五)
    def getRule(self, WareHouse):
        if WareHouse is None or WareHouse == '':  # 如果没有传入值，则进行操作，有传值则返回元素
            raise NameError('必须传入仓库“编码”参数')
        s = '//*[@id="renderListSm0"]/tr[@data-code="%s"]/td[2]' % WareHouse
        # 选择对应仓库下的效期值
        e = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(s))
        print(e.text)
        return e.text

    # 选择对应仓库点击“编辑”
    def optionClickEdit(self, WareHouse):      # 传入仓库编码
        if WareHouse is None or WareHouse == '':  # 如果没有传入值，则进行操作，有传值则返回元素
            raise NameError('必须传入仓库“编码”参数')
        s = '//*[@id="renderListSm0"]/tr[@data-code="%s"]/td[5]/button' % WareHouse
        e = self.driver.find_element_by_xpath(s)        # 选择对应仓库下的编辑
        await_ele.judgeEle(e)  # 点击元素

    # 选择“下架频率”
    def setRule(self, week, Rule=None):
        rules = self.driver.find_elements_by_xpath('//*[@id="week"]/div[%s]/div[2]/a' % week)
        if Rule is None or Rule == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return rules
        elementaction.dropDownBox_text(self, rules, Rule)  # 选择规则

    # 点击“保存”
    def clickSave(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="saleOrderDetail"]/div/div/div[3]/button[1]')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素



"""【==========下架规则_商品，页面元素==============】"""
class GoodsRule():

    # 创建对象是直接进入“下架规则_商品”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list4")  # 进入“库存管理”模块:库存管理的‘for’属性值为“list4”
        e = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_link_text("下架规则"))
        await_ele.judgeEle(e)  # 进入“下架规则_类目”页面
        e1 = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_link_text("商品维度"))
        await_ele.judgeEle(e1, second=20)  # 进入“下架规则_商品”页面

    """此处不需要重新进入"""
    # 进入“下架规则_商品”页面
    def joinGoodsRule(self, action=None):
        e = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_link_text("下架规则"))
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e, second=20)   # 进入“下架规则_类目”页面
        e1 = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_link_text("商品维度"))
        await_ele.judgeEle(e1, second=20)  # 进入“下架规则_商品”页面

    # 输入“商品”
    def inputGoods(self, Goods=None):  # 传入商品
        e = self.driver.find_element_by_name("goodsCode")
        if Goods is None or Goods == "":  # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e, second=20)       # 判断元素是否可以点击
        elementaction.inputContent(self, e, Goods)  # 输入商品

    # 点击“查询”
    def clickSee(self, action=None):
        s = "search"
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return self.driver.find_element_by_id(s)
        await_ele.getAwaitEle('id', s, self.driver, second=20)  # 判断元素是否可以点击

    # 点击“加号”
    def clickPlus(self, action=None):
        s = '//*[@id="renderList"]/tr[1]/td[1]/label'
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return self.driver.find_element_by_xpath(s)
        await_ele.getAwaitEle('xpath', s, self.driver, second=20)  # 判断元素是否可以点击

    # 获取规则值(值为周一至周五)
    def getRule(self, WareHouse):
        if WareHouse is None or WareHouse == '':  # 如果没有传入值，则进行操作，有传值则返回元素
            raise NameError('必须传入仓库“编码”参数')
        s = '//*[@id="renderListSm0"]/tr[@data-code="%s"]/td[2]' % WareHouse
        # 选择对应仓库下的效期值
        e = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(s))
        print(e.text)
        return e.text

    # 选择对应仓库点击“编辑”
    def optionClickEdit(self, WareHouse):      # 传入仓库编码
        if WareHouse is None or WareHouse == '':  # 如果没有传入值，则进行操作，有传值则返回元素
            raise NameError('必须传入仓库“编码”参数')
        s = '//*[@id="renderListSm0"]/tr[@data-code="%s"]/td[5]/button' % WareHouse
        # 选择对应仓库下的编辑（隐式等待，默认间隔0.5s，可不传值）
        await_ele.getAwaitEle('xpath', s, self.driver, second=20)  # 判断元素是否可以点击

    # 选择“下架频率”
    def setRule(self, week, Rule=None):
        rules = self.driver.find_elements_by_xpath('//*[@id="week"]/div[%s]/div[2]/a' % week)
        if Rule is None or Rule == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return rules
        elementaction.dropDownBox_text(self, rules, Rule)  # 选择规则

    # 点击“保存”
    def clickSave(self, action=None):
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return self.driver.find_element_by_xpath('//*[@id="saleOrderDetail"]/div/div/div[3]/button[1]')
        await_ele.getAwaitEle('xpath', '//*[@id="saleOrderDetail"]/div/div/div[3]/button[1]', self.driver, second=20)  # 判断元素是否可以点击



"""【==========货柜库存_查询，页面元素==============】"""
class ShopStock():

    # 创建对象是直接进入“下架规则_商品”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list4")  # 进入“库存管理”模块:库存管理的‘for’属性值为“list4”
        await_ele.getAwaitEle('link_text', "货柜库存", self.driver, second=20)  # 判断元素是否可以点击

    # 进入“下架规则”页面
    def joinShopStock(self, action=None):
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return self.driver.find_element_by_link_text("货柜库存")
        await_ele.getAwaitEle('link_text', "货柜库存", self.driver, second=20)  # 判断元素是否可以点击

    # 输入“商品”
    def inputGoods(self, Goods=None):
        await_ele.getAwaitEle('id', "goods", self.driver, second=20)  # 判断元素是否可以点击
        e = self.driver.find_element_by_id("goods")
        if Goods is None or Goods == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        elementaction.inputContent(self, e, Goods)

    # 输入“货柜”
    def inputShop(self, Shop=None):
        await_ele.getAwaitEle('id', "shop", self.driver, second=20)  # 判断元素是否可以点击
        e = self.driver.find_element_by_id("shop")
        if Shop is None or Shop == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        elementaction.inputContent(self, e, Shop)

    # 输入“品牌”
    def inputBrand(self, Brand=None):
        await_ele.getAwaitEle('id', "brand", self.driver, second=20)  # 判断元素是否可以点击
        e = self.driver.find_element_by_id("brand")
        if Brand is None or Brand == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        elementaction.inputContent(self, e, Brand)

    # 输入“类目”
    def inputCategory(self, Category=None):
        await_ele.getAwaitEle('id', "category", self.driver, second=20)        # 判断元素是否可以点击
        e = self.driver.find_element_by_id("category")
        if Category is None or Category == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        elementaction.inputContent(self, e, Category)

    # 选择“城市”
    def optionCity(self, City=None):
        await_ele.getAwaitEle('id', "cityList", self.driver, second=20)        # 判断元素是否可以点击
        Citys = self.driver.find_elements_by_xpath(r'//*[@id="cityList"]/option')
        if City is not None or City == "":  # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return Citys
        elementaction.dropDownBox_text(self, Citys, City)

    # 选择“货柜类型”
    def optionShopType(self, ShopType=None):
        await_ele.getAwaitEle('id', "shopType", self.driver, second=20)        # 判断元素是否可以点击
        ShopTypes = self.driver.find_elements_by_xpath(r'//*[@id="shopType"]/option')
        if ShopType is not None or ShopType == "":  # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return ShopTypes
        elementaction.dropDownBox_text(self, ShopTypes, ShopType)

    # 选择“城市”
    def optionShopStatus(self, ShopStatus=None):
        await_ele.getAwaitEle('id', "shopStatus", self.driver, second=20)      # 判断元素是否可以点击
        ShopStatuss = self.driver.find_elements_by_xpath(r'//*[@id="shopStatus"]/option')
        if ShopStatus is not None or ShopStatus == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return ShopStatuss
        elementaction.dropDownBox_text(self, ShopStatuss, ShopStatus)

    # 点击“查询”
    def clickSee(self, action=None):
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return self.driver.find_element_by_id("search")
        await_ele.getAwaitEle('id', "search", self.driver, second=20)  # 判断元素是否可以点击

    # 获取“商品名称”元素
    def getGoodsName(self):
        es = self.driver.find_elements_by_xpath('//*[@id="renderList"]/tr/td[2]')
        return es



