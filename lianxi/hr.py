import requests
import urllib

url_debugLogin='http://hr-test.it.chehejia.com:18000/debuglogin?user_id=5923'
response_login = requests.get(url_debugLogin)
h = response_login.headers
# print(h)

url_myStaff = 'http://hr-test.it.chehejia.com:18000/portal/my/staff?staff_id=5923'
# param = {'staff_id':'5923'}
# header = {'laravel_session':'eyJpdiI6InA3Y2pmXC9XT1E2MmpUaWo5dzhPZWpnPT0iLCJ2YWx1ZSI6ImRuSmFrVVp1VXZBUHZ4ZXZ0WmNReTJzcW5nUGlHN2wxZkNyMHgxdjdzdHJ5MFNWK3VcL29sM3hxcm5yaFwvUEdkSUxrbTVhVElhcXBvTG00S0JSbHJBQ2lWQ1hqWXNwNlwvdkxVeUNwRzlxRmRVVTJsTHZBck1Da1IrXC9FY1JRZFNjTiIsIm1hYyI6IjM4YmNlZDNjYmE1MDRiZWQxOTJiMGVhOTlmNzViMTgwYTZkYzYwNGZjOTAzMDlkNWE5MzIwMzZmMzZmYmQxZTQifQ%3D%3D'}
response_staff = requests.get(url=url_myStaff,headers=h)
print(response_staff.text)

