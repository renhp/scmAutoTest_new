# 其他出库页面元素
from scmTest.test_case.public import await_ele
from scmTest.test_case.public.page import joinmodule, elementaction


"""【==========其他出库，页面元素==============】"""
class OtherOutboundPage:

    # 创建对象是直接进入“其他出库”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list3")
        e = self.driver.find_element_by_link_text("其他出库")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“其他出库”页面
    def joinOtherOutbound(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("其他出库")
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

    # 选择“审核状态”
    def optionCheckState(self, CheckState=None):
        e = self.driver.find_element_by_name("auditStatus")
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        CheckStates = self.driver.find_elements_by_xpath(r'//select[@name="auditStatus"]/option')
        if CheckState is None or CheckState == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return CheckStates
        elementaction.dropDownBox_text(self, CheckStates, CheckState)

    # 选择“出库状态”
    def optionStockRemovalState(self, StockRemovalState=None):
        e = self.driver.find_element_by_name("outStatus")
        await_ele.judgeEle(e)
        StockRemovalStates = self.driver.find_elements_by_xpath(r'//select[@name="outStatus"]/option')
        if StockRemovalState is None or StockRemovalState == "":  # 如果没有传入值或传的是'""'则直接返回库位名组
            return StockRemovalStates
        elementaction.dropDownBox_text(self, StockRemovalStates, StockRemovalState)

    # 输入“其它出库单号”
    def inputOtherOrderNumber(self, OtherOrderNumber=None):
        e = self.driver.find_element_by_name("otherorderNumber")
        if OtherOrderNumber is None or OtherOrderNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, OtherOrderNumber)

   # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id('search')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取一组“其它出库单号”元素
    def getOtherOrderNumbers(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="renderList"]/tr/td[1]')
        return es

    # 获取一组“审核状态”元素
    def getCheckStates(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="renderList"]/tr/td[2]')
        return es

    # 获取一组“出库状态”元素
    def getStockRemovalStates(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="renderList"]/tr/td[3]')
        return es

    # 获取一组“发货仓库”元素
    def getWarehouses(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="renderList"]/tr/td[4]')
        return es



