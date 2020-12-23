import requests
class RunMain():
    def send_get(self,url,data,cookies):
        res = requests.get(url=url,data=data,cookies=cookies).json()
        return res

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()

    def run_main(self,url,method,data=None,cookies=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data,cookies)
        else:
            res = self.send_post(url,data,cookies)
        return res









