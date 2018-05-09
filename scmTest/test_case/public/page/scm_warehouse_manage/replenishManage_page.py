# 补货管理页面元素
from scmTest.test_case.public import await_ele
from scmTest.test_case.public.page import joinmodule, elementaction

"""【==========补货管理，页面元素==============】"""
class ReplenishManagePage:

    # 创建对象是直接进入“补货管理”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list3")
        e = self.driver.find_element_by_link_text("补货管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“补货管理”页面
    def joinReplenishManage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("补货管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“仓库”
    def optionWarehouse(self, WareHouse=None):
        e = self.driver.find_element_by_name("warehouseCode")
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@name="warehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)

    # 输入“需求单号”
    def inputReplenishNumber(self, ReplenishNumber=None):
        e = self.driver.find_element_by_name("replenishOrderId")
        if ReplenishNumber is None or ReplenishNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, ReplenishNumber)

    # 输入“波次单号”
    def inputOutboundNumber(self, OutboundNumber=None):
        e = self.driver.find_element_by_name("outboundOrderId")
        if OutboundNumber is None or OutboundNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, OutboundNumber)

    # 输入“货柜”
    def inputShop(self, Shop=None):
        e = self.driver.find_element_by_name("shop")
        if Shop is None or Shop == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Shop)

    # 选择“状态”
    def optionState(self, State=None):
        e = self.driver.find_element_by_name("status")
        await_ele.judgeEle(e)  # 点击元素
        CheckStates = self.driver.find_elements_by_xpath(r'//select[@name="status"]/option')
        if State is None or State == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return CheckStates
        elementaction.dropDownBox_text(self, CheckStates, State)

   # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id('searchBtn')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取一组“需求单号”元素
    def getReplenishNumbers(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="mainList"]/tr/td[1]')
        return es

    # 获取一组“波次单号”元素
    def getOutboundNumbers(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="mainList"]/tr/td[2]')
        return es

    # 获取一组“仓库”元素
    def getWareHouses(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="mainList"]/tr/td[3]')
        return es

    # 获取一组“货柜”元素
    def getShops(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="mainList"]/tr/td[4]')
        return es

    # 获取一组“状态”元素
    def getStates(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="mainList"]/tr/td[6]')
        return es








