# 采购管理模块页面元素
from scmTest.test_case.public.page import joinmodule
from scmTest.test_case.public.page import elementaction
from selenium.webdriver.support.ui import WebDriverWait
from scmTest.test_case.public import await_ele


"""【==========订单管理，页面元素==============】"""
class OrderManagePage:

    # 创建对象是直接进入“订单管理”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list1")
        e = self.driver.find_element_by_link_text("订单管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“订单管理”页面
    def joinOrderManagePage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("订单管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 输入“采购单号”
    def inputOrderNumber(self, OrderNumber=None):
        e = self.driver.find_element_by_name("orderNumber")
        if OrderNumber is None or OrderNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, OrderNumber)

    # 选择“仓库”
    def optionWarehouse(self, WareHouse=None):
        e = self.driver.find_element_by_name("warehouseCode")
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@name="warehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)

    # 选择“库位”
    def optionStorageLocation(self, StorageLocation=None):    # 传入库位名
        e = self.driver.find_element_by_name("locationCode")
        await_ele.judgeEle(e)
        storageLocations = self.driver.find_elements_by_xpath(r'//select[@name="locationCode"]/option')
        if StorageLocation is None or StorageLocation == "":       # 如果没有传入库位或传的是'""'则直接返回库位名组
            return storageLocations
        elementaction.dropDownBox_text(self, storageLocations, StorageLocation)     # 选择库位名

    # 输入“供应商”
    def inputSupplier(self, Supplier=None):
        e = self.driver.find_element_by_name("supplierName")
        if Supplier is None or Supplier == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Supplier)

    # 选择“入库状态”
    def optionInventoryState(self, InventoryState=None):
        e = self.driver.find_element_by_name("storageStatus")
        await_ele.judgeEle(e)  # 点击元素
        InventoryStates = self.driver.find_elements_by_xpath(r'//select[@name="storageStatus"]/option')
        if InventoryState is None or InventoryState == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return InventoryStates
        elementaction.dropDownBox_text(self, InventoryStates, InventoryState)

    # 输入“采购员”
    def inputBuyer(self, Buyer=None):
        e = self.driver.find_element_by_name("opUser")
        if Buyer is None or Buyer == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Buyer)

    # 选择“订单状态”
    def optionOrderState(self, OrderState=None):
        e = self.driver.find_element_by_name("auditStatus")
        await_ele.judgeEle(e)  # 点击元素
        OrderStates = self.driver.find_elements_by_xpath(r'//select[@name="auditStatus"]/option')
        if OrderState is None or OrderState == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return OrderStates
        elementaction.dropDownBox_text(self, OrderStates, OrderState)

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id('cgManagesearchBtn')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取“采购单基本信息”元素组
    def getOrderBasicInfors(self):
        es = self.driver.find_elements_by_xpath('//*[@id="orderList"]/tr/td[2]/ul')
        return es

    # 获取“状态”元素组
    def getStates(self):
        es = self.driver.find_elements_by_xpath('//*[@id="orderList"]/tr/td[3]/ul')
        return es

    # 获取“其他”元素组
    def getOthers(self):
        es = self.driver.find_elements_by_xpath('//*[@id="orderList"]/tr/td[6]/ul')
        return es



"""【==========退货管理，页面元素==============】"""
class SalesReturnManagePage(object):

    # 创建对象是直接进入“退货管理”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list1")
        e = self.driver.find_element_by_link_text("退货管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“退货管理”页面
    def joinOrderManagePage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("退货管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 输入“采购单号”
    def inputOrderNumber(self, OrderNumber=None):
        e = self.driver.find_element_by_name("purchaseNumber")
        if OrderNumber is None or OrderNumber == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, OrderNumber)

    # 选择“仓库”
    def optionWarehouse(self, WareHouse=None):
        e = self.driver.find_element_by_name("warehouseCode")
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@name="warehouseCode"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)

    # 输入“供应商”
    def inputSupplier(self, Supplier=None):
        e = self.driver.find_element_by_name("supplier")
        if Supplier is None or Supplier == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Supplier)

    # 选择“出库状态”
    def optionStockRemovalState(self, StockRemovalState=None):
        e = self.driver.find_element_by_name("outStatus")
        await_ele.judgeEle(e)  # 点击元素
        StockRemovalStates = self.driver.find_elements_by_xpath(r'//select[@name="outStatus"]/option')
        if StockRemovalState is None or StockRemovalState == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return StockRemovalStates
        elementaction.dropDownBox_text(self, StockRemovalStates, StockRemovalState)

    # 选择“订单状态”
    def optionOrderState(self, OrderState=None):
        e = self.driver.find_element_by_name("backStatus")
        await_ele.judgeEle(e)  # 点击元素
        OrderStates = self.driver.find_elements_by_xpath(r'//select[@name="backStatus"]/option')
        if OrderState is None or OrderState == "":       # 如果没有传入或传的是'""'则直接返回元素名组
            return OrderStates
        elementaction.dropDownBox_text(self, OrderStates, OrderState)

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id('search')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)

    # 获取“退货单基本信息”元素组
    def getOrderBasicInfors(self):
        es = self.driver.find_elements_by_xpath('//*[@id="orderList"]/tr/td[1]/ul')
        return es

    # 获取“状态”元素组
    def getStates(self):
        es = self.driver.find_elements_by_xpath('//*[@id="orderList"]/tr/td[2]/ul')
        return es



