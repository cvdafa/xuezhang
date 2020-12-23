# 访问官网
from selenium import webdriver
import time
url = 'https://www-test.lixiang.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
# 点击官网的登录
driver.find_element_by_xpath("/html/body/header[1]/div[2]/div[2]/ul[2]/li[14]/a").click()
time.sleep(1)
login_index_uid = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/input")
# 填入账号和密码
login_index_uid.click()
login_index_uid.send_keys('13211113333')
time.sleep(2)
login_index_password = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div[1]/input")
login_index_password.click()
login_index_password.send_keys('1111')
time.sleep(2)

# 点击去登录
login_button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[6]/div")
login_button.click()
time.sleep(3)

# 首页点击立即订购
dinggou = driver.find_element_by_xpath('//*[@id="article-0"]/div[1]/div/a[2]')
dinggou.click()
time.sleep(3)
#点击交付中心
driver.find_element_by_class_name('form-select-value').click()
time.sleep(3)
# #选择五元桥中心
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/span').click()
time.sleep(4)

#默认全款预定订单
driver.find_element_by_xpath('//*[@id="confirm"]/div[1]/div[9]/p').click()
time.sleep(2)

#同意隐私协议
driver.find_element_by_xpath('//*[@id="bottom"]/div/div[1]/div[1]').click()
time.sleep(2)

#立即支付
driver.find_element_by_xpath('//*[@id="bottom"]/div/div[2]/div[2]').click()
time.sleep(2)

#确认支付弹框
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]').click()

#出现扫码支付---创建订单成功






