from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('http://scm.fanqiebianli.com/scmp/#/goods')

driver.find_element_by_xpath('//*[@id="accountId"]').send_keys('hongxiaonan')
driver.find_element_by_id('password').send_keys(12345678)
sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/form/button').click()

print('test')
print('test-2')
print('test-3')
print('test-4')

