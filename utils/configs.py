# 读取配置文件类
import configparser
import os
from selenium import webdriver

# 基本目录
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]        # 项目目录
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.ini')                   # 配置文件目录
DATA_PATH = os.path.join(BASE_PATH, 'data')                                     # 测试数据目录
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')                                # 浏览器目标
LOG_PATH = os.path.join(BASE_PATH, 'log')                                       # 日志文件目录
REPORT_PATH = os.path.join(BASE_PATH, 'report')                                 # 测试报告目录
TEST_CASW_PATH = os.path.join(BASE_PATH, 'scmTest', 'test_case', 'case')        # 测试用例目录


# 配置文件操作类，获取配置文件中的信息及某些文件夹目录
class Configs:
    def __init__(self):
        # 读取配置文件
        self.conf = configparser.ConfigParser()
        self.conf.read(CONFIG_FILE)
        self.env = self.conf.get("option", "environment")   # 选择测试环境
        if self.env not in ('test', 'pre', 'pro'):
            raise NameError('配置文件中的"environment=%s"，参数只能=(test/pre/pro)!!!' % self.env)
        self.driver = self.conf.get("option", "browser")    # 选择浏览器对象
        if self.driver not in ('Chrome', 'Firefox', 'IE'):
            raise NameError('配置文件中的"browser=%s"，参数只能=(Chrome/Firefox/IE)!!!' % self.driver)

    # 获取URL
    def getURL(self):
        URL = self.conf.get(self.env, "URL")
        return URL

    # 获取项目目录
    def getBasePath(self):
        return BASE_PATH

    # 获取项目目录
    def getTestCasePath(self):
        return TEST_CASW_PATH

    # 获取测试数据目录
    def getDataPath(self):
        if self.env == 'test':
            return DATA_PATH + r'\test_data'
        if self.env == 'pre':
            return DATA_PATH + r'\pre_data'
        if self.env == 'pro':
            return DATA_PATH + r'\pro_data'

    # 获取测试报告目录
    def getReportPath(self):
        if self.env == 'test':
            return REPORT_PATH + r'\test_report\report_file'
        if self.env == 'pre':
            return REPORT_PATH + r'\pre_report\report_file'
        if self.env == 'pro':
            return REPORT_PATH + r'\pro_report\report_file'

    # 获取测试截图目录
    def getScreenshotPath(self):
        if self.env == 'test':
            return REPORT_PATH + r'\test_report\Screenshot'
        if self.env == 'pre':
            return REPORT_PATH + r'\pre_report\Screenshot'
        if self.env == 'pro':
            return REPORT_PATH + r'\pro_report\Screenshot'

    # 获取cookie文件目录
    def getCookieFilePath(self):
        if self.env == 'test':
            return DATA_PATH + r'\test_data\public_data\cookie.txt'
        if self.env == 'pre':
            return DATA_PATH + r'\pre_data\public_data\cookie.txt'
        if self.env == 'pro':
            return DATA_PATH + r'\pro_data\public_data\cookie.txt'

    # 获取浏览器对象
    def getDriver(self):
        if self.driver == 'Chrome':
            chromeDriver = webdriver.Chrome()  # 谷歌浏览器
            return chromeDriver
        elif self.driver == 'Firefox':
            firefoxDriver = webdriver.Firefox()  # 目前没有装Firefox
            return firefoxDriver
        elif self.driver == 'IE':
            ieDriver = webdriver.Ie()  # IE浏览器
            return ieDriver
        else:
            raise NameError('配置文件中的"browser=%s"，参数只能=(Chrome/Firefox/IE)!!!' % self.driver)

    # 获取日志文件存放目录
    def getLogPath(self):
        if self.env == 'test':
            return LOG_PATH + r'\test_log'
        if self.env == 'pre':
            return LOG_PATH + r'\pre_log'
        if self.env == 'pro':
            return LOG_PATH + r'\pro_log'



if __name__ == "__main__":
    # 测试以上方法
    conf = Configs()
    print(conf.getBasePath())
    print(conf.getURL())
    print(conf.getBasePath())
    print(conf.getDataPath())
    print(conf.getReportPath())
    print(conf.getScreenshotPath())
    print(conf.getTestCasePath())
    print(conf.getDriver())



