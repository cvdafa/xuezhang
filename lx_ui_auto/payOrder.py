from selenium import webdriver
import time
import requests

url_login_index = 'https://iot-agmgnt-test.chj.cloud/aisp-account-api/aisp-account-api/v1-0/login'
url_order_index ='https://www-test.lixiang.com/mall/order.html'
# , "X-CHJ-Deviceid":Test.tonken
#先登录保存cookie

wb = requests.post(url_login_index,headers={"content-Type":"application/json;charset=UTF-8"},json={"loginType":3,"mobile":'13211113333',"smsCode":"1111"},verify=False)
print(update(wb.cookies))
