# 供应链管理模块页面
from time import sleep
from scmTest.test_case.public.page import joinmodule
from scmTest.test_case.public.page import elementaction
from selenium.webdriver.support.ui import WebDriverWait
from scmTest.test_case.public import await_ele

"""【==========地点管理，页面元素==============】"""
class AddressManage():

    # 创建对象是直接进入“地点管理页面”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list2")  # 进入“地点管理”模块:库存管理的‘for’属性值为“list2”
        e = self.driver.find_element_by_link_text("地点管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“地点管理”页面
    def joinAddressManage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("地点管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“仓库”
    def optionWarehouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_id("warehouseSelect")     # 点击仓库下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@id="warehouseSelect"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 选择“省份”
    def optionProvince(self, WareHouse=None):  # 传入省份
        e = self.driver.find_element_by_id("f1")     # 点击省份下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取省份名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@id="f1"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入省份或传的是'""'则直接返回省份名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择省份名

    # 选择“城市”
    def optionCity(self, WareHouse=None):  # 传入城市
        e = self.driver.find_element_by_id("cityList")     # 点击城市下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取城市名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@id="cityList"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入城市或传的是'""'则直接返回省份名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择城市名

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="form"]/button[1]')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 获取仓库值组【未使用】
    def getWarehouses(self):
        # 选择对应仓库值【列表中隔一个的基数tr才有需要的元素】
        i = 1
        es = []
        while True:
            try:
                if i % 2 != 0:
                    e = self.driver.find_element_by_xpath('//*[@id="locationTable"]/tr[%s]/td[2]' % i)  # 隔一个找一个
                    es.append(e)
                    print(e.text)
                i += 1
            except:
                return es

    # 获取仓库值(单个查询结果)
    def getWarehouse(self):
        e = self.driver.find_element_by_xpath('//*[@id="locationTable"]/tr[1]/td[2]')
        return e

    # 点击“编辑”
    def clickEdit(self, action=None):
        e = self.driver.find_element_by_link_text('编辑')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 输入“联系人”（编辑/新增）
    def inputContactMan(self, ContactMan=None):
        e = self.driver.find_element_by_name("warehouseContact")
        if ContactMan is None or ContactMan == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, ContactMan)

    # 输入“联系电话”（编辑/新增）
    def inputTelephone(self, Telephone=None):
        e = self.driver.find_element_by_name("warehouseTelephone")
        if Telephone is None or Telephone == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Telephone)

    # 点击“是”（编辑/新增）
    def clickYes(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="locationEditModal"]/div[2]/ul/li[5]/div/div[1]/label/input')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 点击“否”（编辑/新增）
    def clickNo(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="locationEditModal"]/div[2]/ul/li[5]/div/div[2]/label/input')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 输入“仓库地址”（编辑/新增）
    def inputWarehouseAddress(self, WarehouseAddress=None):
        e = self.driver.find_element_by_name("warehouseAddress")
        if WarehouseAddress is None or WarehouseAddress == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, WarehouseAddress)

    # 输入“地点名称”（编辑/新增）
    def inputAddressName(self, AddressName=None):
        e = self.driver.find_element_by_name("warehouseName")
        if AddressName is None or AddressName == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, AddressName)

    # 输入“地点编码”（编辑/新增）
    def inputAddressCode(self, AddressCode=None):
        e = self.driver.find_element_by_xpath('//*[@id="locationEditModal"]/div[2]/ul/li[1]/div/div[1]/div[1]/div/input')
        if AddressCode is None or AddressCode == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, AddressCode)

    # 点击“保存”（编辑/新增）
    def clickSave(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="locationEditModal"]/div[3]/button[1]')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 获取“提示框信息元素”（编辑/新增）//*[@id="tomatoAlert"]/div/h4
    def getAlertInfoElement(self):
        e = self.driver.find_element_by_xpath('//*[@id="tomatoAlert"]/div/h4')
        await_ele.judgeEle(e)  # 点击元素
        return e

    # 点击“关闭”（编辑/新增）
    def clickClose(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="alert"]/div/div/div[3]/button')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 点击“新增地点”
    def clickNewAddress(self, action=None):
        e = self.driver.find_element_by_xpath('//*[@id="form"]/button[2]')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“省份”（新增）
    def optionProvinceNewAdd(self, Province=None):  # 传入省份
        e = self.driver.find_element_by_xpath('//div/div[1]/div/select[@id="f1"]')     # 点击省份下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取省份名组
        provinces = self.driver.find_elements_by_xpath(r'//div/div[1]/div/select[@id="f1"]/option')
        if Province is None or Province == "":       # 如果没有传入省份或传的是'""'则直接返回省份名组
            return provinces
        elementaction.dropDownBox_text(self, provinces, Province)

    # 选择“城市”（新增）
    def optionCityNewAdd(self, City=None):  # 传入城市
        e = self.driver.find_element_by_xpath('//div/div[2]/div/select[@id="f2"]')     # 点击城市下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取城市名组
        sleep(0.5)
        citys = self.driver.find_elements_by_xpath('//div/div[2]/div/select[@id="f2"]/option')
        if City is None or City == "":       # 如果没有传入城市或传的是'""'则直接返回省份名组
            return citys
        elementaction.dropDownBox_text(self, citys, City)

    # 选择“区县”（新增）
    def optionCountyNewAdd(self, County=None):  # 传入区县
        e = self.driver.find_element_by_xpath('//div/div[3]/div/select[@id="f3"]')     # 点击区县下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取城市名组
        countys = self.driver.find_elements_by_xpath(r'//div/div[3]/div/select[@id="f3"]/option')
        if County is None or County == "":       # 如果没有传入区县或传的是'""'则直接返回省份名组
            return countys
        elementaction.dropDownBox_text(self, countys, County)

    # 点击“查看明细”
    def clickSeeDetail(self, action=None):
        e = self.driver.find_element_by_link_text('查看')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 点击“取消”（明细弹框）
    def clickCancel(self, action=None):
        # 查看元素是否为用户可见(返回True或FALSE)
        e = self.driver.find_element_by_xpath('//*[@id="locationEditModal"]/div[3]/button[2]')
        if action is not None:  # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素


"""【==========辐射管理，页面元素==============】"""
class RadiateManage():

    # 创建对象是直接进入“地点管理页面”模块
    def __init__(self, driver):
        self.driver = driver
        joinmodule.joinModule(self, "list2")  # 进入“地点管理”模块:库存管理的‘for’属性值为“list2”
        e = self.driver.find_element_by_link_text("辐射管理")
        await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素

    # 进入“辐射管理”页面
    def joinRadiateManage(self, action=None):
        driver = self.driver
        e = driver.find_element_by_link_text("辐射管理")
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 选择“仓库”
    def optionWarehouse(self, WareHouse=None):  # 传入仓名
        e = self.driver.find_element_by_id("warehouseSelect")     # 点击仓库下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取仓库名组
        wareHouses = self.driver.find_elements_by_xpath(r'//select[@id="warehouseSelect"]/option')
        if WareHouse is None or WareHouse == "":       # 如果没有传入仓库或传的是'""'则直接返回仓库名组
            return wareHouses
        elementaction.dropDownBox_text(self, wareHouses, WareHouse)     # 选择仓库名

    # 输入“货柜”
    def inputShop(self, Shop=None):
        e = self.driver.find_element_by_name("shopNoOrName")
        if Shop is None or Shop == "":           # 如果传入了值，则进行操作，没有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素
        elementaction.inputContent(self, e, Shop)

    # 选择“省份”
    def optionProvince(self, Province=None):  # 传入省份
        e = self.driver.find_element_by_xpath('//*[@id="f1"]')     # 点击省份下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取省份名组
        provinces = self.driver.find_elements_by_xpath(r'//*[@id="f1"]/option')
        if Province is None or Province == "":       # 如果没有传入省份或传的是'""'则直接返回省份名组
            return provinces
        elementaction.dropDownBox_text(self, provinces, Province)

    # 选择“城市”
    def optionCity(self, City=None):  # 传入城市
        e = self.driver.find_element_by_id("cityList")     # 点击城市下拉框
        await_ele.judgeEle(e)  # 点击元素
        # 获取城市名组
        citys = self.driver.find_elements_by_xpath('//*[@id="cityList"]/option')
        if City is None or City == "":       # 如果没有传入城市或传的是'""'则直接返回省份名组
            return citys
        elementaction.dropDownBox_text(self, citys, City)

    # 选择“区县”
    def optionCounty(self, County=None):  # 传入区县
        e = self.driver.find_element_by_xpath('//*[@id="f3"]')     # 点击区县下拉框
        await_ele.judgeEle(e)  # 点击元素
        countys = self.driver.find_elements_by_xpath(r'//*[@id="f3"]/option')
        if County is None or County == "":       # 如果没有传入区县或传的是'""'则直接返回省份名组
            return countys
        elementaction.dropDownBox_text(self, countys, County)

    # 选择“货柜类型”
    def optionShopType(self, ShopType=None):  # 传入区县
        e = self.driver.find_element_by_id('shopType')     # 点击区县下拉框
        await_ele.judgeEle(e)  # 点击元素
        ShopTypes = self.driver.find_elements_by_xpath(r'//*[@id="shopType"]/option')
        if ShopType is None or ShopType == "":       # 如果没有传入区县或传的是'""'则直接返回省份名组
            return ShopTypes
        elementaction.dropDownBox_text(self, ShopTypes, ShopType)

    # 选择“货柜类型”
    def optionShopState(self, ShopState=None):  # 传入区县
        e = self.driver.find_element_by_id('shopStatus')     # 点击区县下拉框
        await_ele.judgeEle(e)  # 点击元素
        ShopStates = self.driver.find_elements_by_xpath(r'//*[@id="shopStatus"]/option')
        if ShopState is None or ShopState == "":       # 如果没有传入区县或传的是'""'则直接返回省份名组
            return ShopStates
        elementaction.dropDownBox_text(self, ShopStates, ShopState)

    # 点击“查询”
    def clickSee(self, action=None):
        e = self.driver.find_element_by_id('searchBtn')
        if action is not None:          # 如果没有传入值，则进行操作，有传值则返回元素
            return e
        await_ele.judgeEle(e)  # 点击元素

    # 获取仓库值(单个查询结果)
    def getShopName(self):
        e = self.driver.find_element_by_xpath('//tbody[@id="userList"]/tr/td[4]')
        return e








