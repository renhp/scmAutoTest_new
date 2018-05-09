# 断言类
import time
from utils.configs import Configs

class Asserts():
    # 初始化根路径
    def __init__(self):
        # 得到相应截图目录
        conf = Configs()
        self.path = conf.getScreenshotPath()


    """====【【【【===断言元素的text(元素值）===】】】】=======】】】】】=======】】】】】】】"""
    # text断言一个元素
    def assertText(self, e, t, screenshotName, driver):
        # e:一个元素，t:一个断言预期结果, screenshotName:截图名称, driver:驱动
        print('元素内容为：', e.text)
        result = t + ':失败!!!'
        if e.text != t:             # 若失败直接抛异常
            now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
            driver.get_screenshot_as_file(self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
            print(screenshotName + '截图成功!!!')
            raise NameError(result)


    # text断言一组元素一个断言值
    def assertTexts(self, es, t, screenshotName, driver):
        # es:一组元素，t:一个断预期结果, screenshotName:截图名称, driver:驱动
        for e in es:
            print('内容为：', e.text)
            result = t + ':失败!!!'
            if e.text != t:  # 若失败直接抛异常
                now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
                driver.get_screenshot_as_file(self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
                print(screenshotName + '截图成功!!!')
                raise NameError(result)


    # text断言一组元素一组断言值
    def assertTextss(self, es, ts, screenshotName, driver):
        # es:一组元素，ts:一组断预期结果, screenshotName:截图名称, driver:驱动
        for i in range(len(es)):
            print('内容为：', es[i].text)
            result = ts[i] + ':失败!!!'
            if es[i].text != ts[i]:     # 若失败直接抛异常
                now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
                driver.get_screenshot_as_file(self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
                print(screenshotName + '截图成功!!!')
                raise NameError(result)


    """====【【【【===断言元素的attributes(元素值）===】】】】=======】】】】】=======】】】】】】】"""
    # attributes断言一个元素一个断言值
    def assertAttribute(self, e, t, attributeName, screenshotName, driver):
        print('内容为：', e.get_attribute(attributeName))
        result = t + ':失败!!!'
        if e.get_attribute(attributeName) != t:
            now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
            driver.get_screenshot_as_file(
                self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
            print(screenshotName + '截图成功!!!')
            raise NameError(result)


    # attributes断言一组元素一个断言值
    def assertAttributes(self, es, t, attributeName, screenshotName, driver):
        for e in es:
            print('内容为：', e.get_attribute(attributeName))
            result = t + ':失败!!!'
            if e.get_attribute(attributeName) != t:
                now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
                driver.get_screenshot_as_file(
                    self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
                print(screenshotName + '截图成功!!!')
                raise NameError(result)


    # attributes断言一组元素一组断言值
    def assertAttributess(self, es, ts, attributeName, screenshotName, driver):
        for i in range(len(es)):
            print('内容为：', es[i].get_attribute(attributeName))
            result = ts[i] + ':失败!!!'
            print(i)
            print(ts)
            if es[i].get_attribute(attributeName) != ts[i]:
                now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
                driver.get_screenshot_as_file(
                    self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
                print(screenshotName + '截图成功!!!')
                raise NameError(result)


    """====【【【【===用例中断言，只配配合截图===】】】】=======】】】】】=======】】】】】】】"""
    # 只配合截图
    def screenshot(self, screenshotName, driver):
        now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        driver.get_screenshot_as_file(
            self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
        print(screenshotName + '截图成功!!!')


    """====【【【【===用例中断言，只配配合截图===】】】】=======】】】】】=======】】】】】】】"""
    # 断言设置前后元素text中的部分值改变（如:下架规则设置中的规则值)
    def assertChangeText(self, t, changeText1, changeText2, screenshotName, driver):
        """t:断言值"""
        result = screenshotName + ':失败!!!'
        if t in changeText1:
            if t not in changeText2:
                pass
            else:
                self.screenshot(result, driver)
                raise NameError(result)
        elif t not in changeText1:
            if t in changeText2:
                pass
            else:
                self.screenshot(result, driver)
                raise NameError(result)



    """====【【【【===断言元素值中是否有需要的值===】】】】=======】】】】】=======】】】】】】】"""
    # text断言一个元素

    # text断言一组元素一个断言值
    def assertValueInTexts(self, es, r, screenshotName, driver):
        # es:一组元素，r:一个断预期结果, screenshotName:截图名称, driver:驱动
        for e in es:
            s = e.text
            print('内容为：', s)
            result = r + ':失败!!!'
            if r not in s:  # 若失败直接抛异常
                now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
                driver.get_screenshot_as_file(self.path + '\\' + screenshotName + '[' + now_time + '].png')  # 截图操作
                print(screenshotName + '截图成功!!!')
                raise NameError(result)



    # text断言一组元素一组断言值

