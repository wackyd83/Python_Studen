import requests

url = 'http://webapi.cninfo.com.cn/#/marketDataDate'

headers = {
    "Cookie": "routeId=.uc1; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1657784504;",
    "Referer": "http://webapi.cninfo.com.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
}



data='tdate=2022-07-13&market=SZE'

response=requests.post(url,data=data,headers=headers)
print(response.text)
