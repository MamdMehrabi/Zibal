from requests import get, post
from json import loads

class main:

    def __init__(self):
        pass

    def request(self):
        json = {
    "merchant": "zibal",
    "amount": 160000,
    "callbackUrl": "http://onlymamad.com/callback.php",
    "description": "Hello World!",
    "orderId": "ZBL-7799",
    "mobile": "09123456789"
    }
        url = "https://gateway.zibal.ir/v1/request"
        req = post(url=url, json=json).json()
        self.message = req["message"]
        self.result = req["result"]
        #print(req)
        if self.result == 100:
            self.trackID = req["trackId"]
            print(self.trackID)
        elif self.result == [102, 103, 104, 105, 106, 113]:
            raise Exception(self.message)
    def start(self):
        url = f"https://gateway.zibal.ir/start/{self.trackID}"
        callback = post(url=url)
        print(callback)



a = main()
a.request()
a.start()
