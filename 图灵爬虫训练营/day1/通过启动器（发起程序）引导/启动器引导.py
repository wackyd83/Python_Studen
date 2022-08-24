import requests
from urllib import parse
import time
import re
import execjs

# 读取js文件
with open('1688.com.js', 'r', encoding='utf-8') as f:
    # Python去执行对应的js代码
    ctx = execjs.compile(f.read())  # 执行读取的js代码

# 请求参数里面的值 -> c.data
# data = {"cid":"FactoryRankServiceWidget:FactoryRankServiceWidget","methodName":"execute","params":"{\"extParam\":\"{\\\"methodName\\\":\\\"readRelatedRankEntries\\\",\\\"cateId\\\":7,\\\"size\\\":15}\"}"}
# 请求头 1. 代理浏览器的类型  2. 需要cookie里面的某一个值
headers = {
    'cookie': 'ali_apache_id=11.186.201.43.1646366047523.228734.8; cookie2=17d67a6487896cb33eef71795b20a2e0; t=41aa384c45d9a993b63b1b1848abd080; _tb_token_=eee8eef7bd111; __cn_logon__=false; cna=qj3/F5q1wVkCAXFEigi/E+9h; ali_ab=124.16.5.169.1656923925204.2; xlly_s=1; _m_h5_tk=1f80742d2a525faea282cc05017759ad_1657788572727; _m_h5_tk_enc=27b955c6983838d1ae92e211fee7357b; alicnweb=touch_tb_at%3D1657779773898; isg=BGlpQO4WL1eBgBMN9mzZZgyveBXDNl1owHXvXAtfzNCP0orkUoa4OIyDlHZkkvWg; tfstk=cUDlB7Gj3bPSqFnZYYwWpgTC-dTOZtBUSvkj337KQ2WmcWkVij1V_IWBmzY6z61..; l=eBP7NBu7LEbcLq6KBO5adurza77TNIOf1SFzaNbMiInca6TV1eZGXNCHtP9kRdtjgt5vqeKz701fodnwJ2aLRFkDBeYIujcjfev6Re1..',
    'referer': 'https://sale.1688.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
}
# 时间戳 -> i值  py的第三方库
time1 = int(time.time() * 1000)
# c.data
data = {"cid": "TpFacRecommendService:TpFacRecommendService", "methodName": "execute",
        "params": "{\"query\":\"mainCate=67&leafCate=\",\"sort\":\"mix\",\"pageNo\":\"1\",\"pageSize\":\"20\",\"from\":\"PC\",\"trafficSource\":\"pc_index_recommend\",\"url\":\"https://sale.1688.com/factory/category.html?spm=a260k.22464671.home2019category.15.123d7a6ef2lHNU&mainId=67\"}"}

# token 生成
# d.token -> 在请求头cookie里面的
token = '1f80742d2a525faea282cc05017759ad'
# g => appkey
appKey = "12574478"
# print(data)
# d.token + "&" + i + "&" + g + "&" + c.data
p = (token + '&' + str(time1) + '&' + appKey + '&' + str(data))

# 执行js代码里面的h函数  p作为参数传递
sign = ctx.call('h', p)

url = f'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/?jsv=2.4.11&appKey=12574478&t={time1}&sign={sign}&api=mtop.taobao.widgetService.getJsonComponent&v=1.0&type=jsonp&isSec=0&timeout=20000&dataType=jsonp&callback=mtopjsonp3&'

# # 需要转码  因为网页的 urldata是 转码后的
urls = url + '&' + 'data=' + parse.quote(str(data))
print(urls)
# # print(sign)
response = requests.get(urls, headers=headers).text
print(response)
