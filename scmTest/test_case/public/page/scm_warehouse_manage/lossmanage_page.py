# 损益管理页面元素
from scmTest.test_case.public import await_ele
from scmTest.test_case.public.page import joinmodule, elementaction


"""【==========损益管理，页面元素==============】"""
class LossManagePage:

    # 创建对象是直接进入“损益管理”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list3")
        e = self.driver.find_element_by_link_text("损溢管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“报损管理”页面
    def joinLossManage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("损溢管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“发货仓库”
    def optionWarehouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_name("warehouseCode")     # 点击仓库下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@name="warehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 输入“货柜”
    def inputShop(self, Shop=None):
        e = self.driver.find_element_by_name("shop")
        if Shop is None or Shop == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Shop)

    # 输入“需求单号”
    def inputReplenishNumber(self, ReplenishNumber=None):
        e = self.driver.find_element_by_name("replenishOrderId")
        if ReplenishNumber is None or ReplenishNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, ReplenishNumber)

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id('search')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取“发货仓库”元素
    def getWarehouses(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="renderList"]/tr/td[3]')
        return es

    # 获取“货柜”元素
    def getShops(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="renderList"]/tr/td[4]')
        return es

    # 获取“需求单号”元素
    def getReplenishNumbers(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="renderList"]/tr/td[2]')
        return es


