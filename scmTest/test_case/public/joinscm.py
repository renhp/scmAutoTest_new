# 进入scm模块
from scmTest.test_case.public import await_ele


# 进入scm
def joinScm(self):
    driver = self.driver
    es = driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/ul/li')
    # 点击SCM
    for e in es:
        if e.text == "SCM":     # 获取标签的值，判断是否为SCM
            await_ele.judgeEle(e, second=20, await_second=0.3)  # 点击元素
            break

# 进入scmIframe
def joinScmIframe(self):
    driver = self.driver
    driver.switch_to.frame(driver.find_element_by_id('iframe'))

