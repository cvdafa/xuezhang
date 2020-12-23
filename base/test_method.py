import unittest
import json
import HtmlTestRunner
import mock
from base.base_request import RunMain

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('---类执行之前的方法')

    @classmethod
    def tearDownClass(cls) -> None:
        print('----类执行之后的方法')


    def setUp(self) -> None:
        self.run = RunMain() #进行实例化
        print('---setup---')

    def tearDown(self) -> None:
        print("---tearDown")

    def test_01(self):
        url = 'http://finance-test.it.chehejia.com:18000/finance/budget/submit/department'
        data = {'budget_type': '费用预算',
               'is_submit': 0,
               'search': {}
                }
        cookies = {'cna':'xTTFF+mRJzQCActdfWb+7zxE',
          'xlly_s':'1',
          'laravel_session':'eyJpdiI6IjBHWlZHU0hhQ1pGU25SZWhTb0xZSnc9PSIsInZhbHVlIjoienBpb0lqMmZpM2J3VVkyZVRGRmp6K3J6anBteDdhaTMyTUJpZlkrbEQwK0FYbmxKVWVLV3doektzSGRuMnJkRSIsIm1hYyI6IjU5MjczMGM5ZWQxZTZhM2M2ZGM1ODlhOGVjNjlmMjNhNDBjMTFiNTIyZTQyMmUyMzUyMzlmYzFhMTkyYTQ5ZWIifQ%3D%3D',
          'chj_it_sso':'nZHd30AoQM0_ZWLMFEZfQgAAAAAACIABemhhbmd4dWUx',
          'scan_redirect_url':'http://finance-test.it.chehejia.com:18000/finance#/'
          }
        mock_data = mock.Mock(return_value=data)
        print(mock_data)
        res1 = self.run.run_main(url=url,method='GET',data=data,cookies=cookies)

        self.assertEqual(res1['code'],0,msg='出错了')
        print(res1)
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(TestMethod)
    unittest.TextTestRunner.run(suite)






