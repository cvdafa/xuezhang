import requests
import time
import urllib
import unittest


url_code = 'http://finance-test.it.chehejia.com:18000/finance/budget/submit/department'
data = {'budget_type':'费用预算',
        'is_submit':0,
        'search':{}}
cookies = {'cna':'xTTFF+mRJzQCActdfWb+7zxE',
          'xlly_s':'1',
          'laravel_session':'eyJpdiI6IjBHWlZHU0hhQ1pGU25SZWhTb0xZSnc9PSIsInZhbHVlIjoienBpb0lqMmZpM2J3VVkyZVRGRmp6K3J6anBteDdhaTMyTUJpZlkrbEQwK0FYbmxKVWVLV3doektzSGRuMnJkRSIsIm1hYyI6IjU5MjczMGM5ZWQxZTZhM2M2ZGM1ODlhOGVjNjlmMjNhNDBjMTFiNTIyZTQyMmUyMzUyMzlmYzFhMTkyYTQ5ZWIifQ%3D%3D',
          'chj_it_sso':'nZHd30AoQM0_ZWLMFEZfQgAAAAAACIABemhhbmd4dWUx',
          'scan_redirect_url':'http://finance-test.it.chehejia.com:18000/finance#/'
          }
response = requests.get(url = url_code,params=data,cookies=cookies,timeout=3)

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Method before class execution')
    @classmethod
    def tearDownClass(cls) -> None:
        print('Method after class execution')
    def setUp(self):
        print('-----setup---')
    def tearDown(self) :
        print('----teardown---')
    def test_01(self):
        print('第一条用例')
    def test_2(self):
        print('第二条用例')

if __name__ == "__main__":
    unittest.main()
