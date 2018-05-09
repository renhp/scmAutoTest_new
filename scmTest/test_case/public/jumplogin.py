# 跳过登录:若cookie信息已经过期，则调用等模块
import re
import time
from scmTest.test_case.public import login
from utils.configs import Configs


# 跳过登录【脚本调试无问题后使用】
def jumpLogin(self):
    driver = self.driver
    try:
        # 文件中读取cookie
        conf = Configs()
        file_path = conf.getCookieFilePath()    # 获取cookie.txt文件目录

        f = open(file_path, 'r')
        s = f.readline()
        f.close()
        c = re.split(',', s)
        cookie = {'name': c[0], 'value': c[1]}
        # 添加cookie信息
        driver.add_cookie({'name': cookie.get('name'), 'value': cookie.get('value')})
        driver.get(self.base_url)
        es = driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/ul/li')
        es[0].click()  # 判断是否已跳过登录，若没有则此处会报错，进而调用登录模块
    except:
        login.login(self)               # 调用登录模块
        time.sleep(0.5)
        ckl = driver.get_cookies()      # 将最新cookie写入cookie.txt文件
        for ckd in ckl:                 # 注:(ckl:为列表，其中放的字典；ck_c:为字典)
            pass
        s = ckd['name'] + ',' + ckd['value']    # 拼接cookie信息
        f = open(file_path, 'w')        # 写入最新cookie的name和value
        f.write(s)
        f.close()
