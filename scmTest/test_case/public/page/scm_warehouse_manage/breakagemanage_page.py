# 报损管理页面元素
from scmTest.test_case.public import await_ele
from scmTest.test_case.public.page import joinmodule, elementaction

"""【==========报损管理，页面元素==============】"""
class BreakageManagePage:

    # 创建对象是直接进入“报损管理”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list3")
        e = self.driver.find_element_by_link_text("报损管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“报损管理”页面
    def joinBreakageManage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("报损管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“仓库”
    def optionWarehouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_name("warehouseCode")     # 点击仓库下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@name="warehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 选择“审核状态”
    def optionAuditState(self, AuditState=None):
        e = self.driver.find_element_by_name("auditStatus")
        await_ele.judgeEle(e)
        AuditStates = self.driver.find_elements_by_xpath(r'//select[@name="auditStatus"]/option')
        if AuditState is None or AuditState == "":       # 如果没有传入值或传的是'""'则直接返回库位名组
            return AuditStates
        elementaction.dropDownBox_text(self, AuditStates, AuditState)

    # 选择“出库状态”
    def optionStockRemovalState(self, StockRemovalState=None):
        e = self.driver.find_element_by_name("outStatus")
        await_ele.judgeEle(e)
        StockRemovalStates = self.driver.find_elements_by_xpath(r'//select[@name="outStatus"]/option')
        if StockRemovalState is None or StockRemovalState == "":       # 如果没有传入值或传的是'""'则直接返回库位名组
            return StockRemovalStates
        elementaction.dropDownBox_text(self, StockRemovalStates, StockRemovalState)

    # 输入“报损单号”
    def inputBreakageNumber(self, AllotNumber=None):
        e = self.driver.find_element_by_name("reportbadNumber")
        if AllotNumber is None or AllotNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, AllotNumber)

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id('search')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取“报损单号”元素
    def getBreakageNumbers(self):
        es = self.driver.find_elements_by_xpath('//*[@id="renderList"]/tr/td[1]')
        return es
