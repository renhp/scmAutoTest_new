# 调拨管理页面元素
from scmTest.test_case.public import await_ele
from scmTest.test_case.public.page import joinmodule, elementaction

"""【==========调拨管理，页面元素==============】"""
class AllotManagePage:

    # 创建对象是直接进入“调拨管理”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list3")
        e = self.driver.find_element_by_link_text("调拨管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“调拨管理”页面
    def joinAllotManage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("调拨管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“调出仓库”
    def optionOutWarehouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_id("outWarehouseCode")     # 点击仓库下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@id="outWarehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 选择“调入仓库”
    def optionJoinWarehouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_id("inWarehouseCode")     # 点击仓库下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@id="inWarehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 选择“调出库位”
    def optionOutStorageLocation(self, StorageLocation=None):    # 传入库位名
        e = self.driver.find_element_by_id("outLocationCode")
        await_ele.judgeEle(e)       # 点击库位
        # 选择库位
        storageLocations = self.driver.find_elements_by_xpath(r'//select[@id="outLocationCode"]/option')
        if StorageLocation is None or StorageLocation == "":       # 如果没有传入库位或传的是'""'则直接返回库位名组
            return storageLocations
        elementaction.dropDownBox_text(self, storageLocations, StorageLocation)     # 选择库位名

    # 选择“调入库位”
    def optionJoinStorageLocation(self, StorageLocation=None):    # 传入库位名
        e = self.driver.find_element_by_id("inLocationCode")
        await_ele.judgeEle(e)       # 点击库位
        # 选择库位
        storageLocations = self.driver.find_elements_by_xpath(r'//select[@id="inLocationCode"]/option')
        if StorageLocation is None or StorageLocation == "":       # 如果没有传入库位或传的是'""'则直接返回库位名组
            return storageLocations
        elementaction.dropDownBox_text(self, storageLocations, StorageLocation)     # 选择库位名

    # 选择“调拨类型”
    def optionAllotType(self, AllotType=None):    # 调拨类型
        e = self.driver.find_element_by_id("allotType")
        await_ele.judgeEle(e)       # 点击调拨类型
        # 选择调拨类型
        AllotTypes = self.driver.find_elements_by_xpath(r'//select[@id="allotType"]/option')
        if AllotType is None or AllotType == "":       # 如果没有传入调拨类型或传的是'""'则直接返回库位名组
            return AllotTypes
        elementaction.dropDownBox_text(self, AllotTypes, AllotType)     # 调拨类型

    # 输入“调拨单号”
    def inputAllotNumber(self, AllotNumber=None):
        e = self.driver.find_element_by_id("orderNum")
        if AllotNumber is None or AllotNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, AllotNumber)

    # 选择“调拨单状态”
    def optionAllotNumberState(self, AllotNumberState=None):    # 调拨单状态
        e = self.driver.find_element_by_id("auditStatus")
        await_ele.judgeEle(e)       # 点击调拨单状态
        # 选择调拨单状态
        AllotNumberStates = self.driver.find_elements_by_xpath(r'//select[@id="auditStatus"]/option')
        if AllotNumberState is None or AllotNumberState == "":       # 如果没有传入值或传的是'""'则直接返回库位名组
            return AllotNumberStates
        elementaction.dropDownBox_text(self, AllotNumberStates, AllotNumberState)     # 调拨单状态

    # 选择“出入库状态”
    def optionOutPutState(self, OutPutState=None):  # 出入库状态
        e = self.driver.find_element_by_id("storageStatus")
        await_ele.judgeEle(e)  # 点击出入库状态
        # 选择出入库状态
        OutPutStates = self.driver.find_elements_by_xpath(r'//select[@id="storageStatus"]/option')
        if OutPutState is None or OutPutState == "":  # 如果没有传入值或传的是'""'则直接返回库位名组
            return OutPutStates
        elementaction.dropDownBox_text(self, OutPutStates, OutPutState)  # 出入库状态

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[9]/button')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 点击“新建”
    def clickCreate(self, action=None):
        e = self.driver.find_element_by_link_text('新建')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 点击“查看明细”（列表中）
    def clickSeeDetail(self, action=None):
        e = self.driver.find_element_by_xpath('//button[@id="listRender"]/tr[1]/td[6]/button')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取“调拨单号”（调拨单基本信息）【可断言单号是否在字符串中即可】
    def getAllotNumbers(self):
        es = self.driver.find_elements_by_xpath('//tbody[@id="listRender"]/tr/td[1]')
        return es


