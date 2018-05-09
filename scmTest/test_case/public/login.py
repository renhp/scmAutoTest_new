# 登录类
import time
from time import sleep

# 其他测试使用
def login(self, username='scm', password='12345678', authcode='验证码'):
    driver = self.driver
    driver.find_element_by_id("accountId").clear()          # 账号
    driver.find_element_by_id("accountId").send_keys(username)
    driver.find_element_by_id("password").clear()           # 密码
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("captchaText").clear()        # 验证码
    driver.find_element_by_id("captchaText").send_keys(authcode)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[5]/div/div/button').click()   # 登录


# 测试登录使用
def login_test(self, username, password, authcode):
    driver = self.driver
    driver.maximize_window()
    self.username = username
    self.password = password
    self.authcode = authcode
    driver.find_element_by_id("accountId").clear()
    driver.find_element_by_id("accountId").send_keys(self.username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(self.password)
    driver.find_element_by_id("captchaText").clear()
    driver.find_element_by_id("captchaText").send_keys(self.authcode)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div/form/div[5]/div/div/button').click()







