# 等待元素【效果不佳】
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime


# 判断元素是否可以点击，【推荐使用】
def judgeEle(e, second=15, await_second=0.5):
    t = 0
    starttime = datetime.datetime.now()
    while t <= second:
        endtime = datetime.datetime.now()
        t = (endtime - starttime).seconds
        try:
            e.click()
            break
        except:
            print('点击元素失败----点击相隔时长', t, '===', e)
            time.sleep(await_second)  # 如果点击失败，隔await_second秒后在次点击
            pass
    if t > second:
        raise NameError('点击元素失败:已经超过设置时间')


# 判断元素是否可以点击
def getAwaitEle(locate_mode, locate_value, driver, second=15):
    """
        locate_mode：定位方式(单个元素、一组元素(一组元素不适用))，locate_value：定位值，
        使用方式如：
            e = getAwaitEle('xpath', '//*[@id="m_gzt$Menu"]/li[2]/a', driver)
            es = getAwaitEle('xpaths', '//*[@id="m_gzt$Menu"]/li[2]/a', driver)
    """

    lm = ['id', 'xpath', 'link_text', 'partial_link_text', 'name', 'tag_name', 'class_name', 'css_selector']
    if locate_mode not in lm:
        raise NameError('定位方式不正确，必须为:', lm)

    elif locate_mode == 'id':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_id(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    elif locate_mode == 'xpath':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_xpath(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    elif locate_mode == 'link_text':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_link_text(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    elif locate_mode == 'partial_link_text':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_partial_link_text(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    elif locate_mode == 'name':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_name(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    elif locate_mode == 'tag_name':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_tag_name(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    elif locate_mode == 'class_name':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_class_name(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    elif locate_mode == 'css_selector':
        t = 0
        starttime = datetime.datetime.now()
        while t <= second:
            endtime = datetime.datetime.now()
            t = (endtime - starttime).seconds
            try:
                driver.find_element_by_css_selector(locate_value).click()
                break
            except:
                print('点击元素失败: == %s,' % locate_value, '  ==点击相隔时长', t)
        if t > second:
            raise NameError('点击元素失败:已经超过设置时间')

    """一组元素:不适用"""
    # # 一组元素
    # elif locate_mode == 'ids':
    #     locator = (By.ID, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_id(locate_value)
    #
    # elif locate_mode == 'xpaths':
    #     locator = (By.XPATH, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_xpath(locate_value)
    #
    # elif locate_mode == 'link_texts':
    #     locator = (By.LINK_TEXT, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_link_text(locate_value)
    #
    # elif locate_mode == 'partial_link_texts':
    #     locator = (By.PARTIAL_LINK_TEXT, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_partial_link_text(locate_value)
    #
    # elif locate_mode == 'names':
    #     locator = (By.NAME, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_name(locate_value)
    #
    # elif locate_mode == 'tag_names':
    #     locator = (By.TAG_NAME, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_tag_name(locate_value)
    #
    # elif locate_mode == 'class_names':
    #     locator = (By.CLASS_NAME, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_class_name(locate_value)
    #
    # elif locate_mode == 'css_selectors':
    #     locator = (By.CSS_SELECTOR, locate_value)
    #     WebDriverWait(driver, 6, 1).until(EC.presence_of_element_located(locator))
    #     return driver.find_elements_by_class_name(locate_value)




