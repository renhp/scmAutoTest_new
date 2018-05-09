# 选择/进入不同模块
from selenium.webdriver.support.ui import WebDriverWait
import datetime

# 进入模块
def joinModule(self, module=None, second=20):
    # 等待模块出现
    t = 0
    starttime = datetime.datetime.now()
    while t <= 10:
        try:
            self.driver.find_element_by_xpath(r'//div[@id="menuLeftList"]')
            break
        except:
            print('模块组未加载出来')
            pass
        endtime = datetime.datetime.now()
        t = (endtime - starttime).seconds
        if t > 10:
            raise NameError('等待模块出现失败:已经超过设置时间')
        break

    # 进入“module”模块
    es = self.driver.find_elements_by_xpath(r'//div[@id="menuLeftList"]/label')
    if module is None:          # 如果传入了值，则进行操作，没有传值则返回一组元素
        return es
    for e in es:
        if e.get_attribute('for') == module:  # 属性
            t = 0
            starttime = datetime.datetime.now()
            while t <= second:
                endtime = datetime.datetime.now()
                t = (endtime - starttime).seconds
                try:
                    e.click()
                    break
                except:
                    # print('点击元素失败: == %s,' % module, '  ==点击相隔时长', t)
                    pass
            if t > second:
                raise NameError('点击元素失败:已经超过设置时间')
            break



