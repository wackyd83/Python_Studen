'''通过打JS断点，查看JS代码对请求头的验证内容，然后把需要验证的内容添加到代码的请求头中'''
import requests

url = 'http://www.whggzy.com/front/search/category'
headers = {
    'Accept': "*/*",
    'Content-Type': "application/json",
    'X-Requested-With': "XMLHttpRequest",
    'Referer': 'http://www.whggzy.com/ZcyAnnouncement1/ZcyAnnouncement11/index.html?utm=sites_group_front.5b1ba037.0.0.f0588390f78011ecbcc91b4cb991dc28',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
}

data = "{\"utm\":\"sites_group_front.5b1ba037.0.0.f0588390f78011ecbcc91b4cb991dc28\",\"categoryCode\":\"ZcyAnnouncement11\",\"pageSize\":15,\"pageNo\":1}"

response = requests.post(url=url, headers=headers, data=data).text
print(response)
