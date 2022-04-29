import re
import pprint as pprint
import parsel
import requests

url_l = [r'http://jandan.net/pic', ]
dic={}

response = requests.get(url_l[-1], )

html_data = response.text
print(html_data)
selector = parsel.Selector(html_data)
ols = selector.xpath(r'//*[@id="comments"]/ol/li')
for ol in ols:
    oo = ol.xpath(r'./div/div/div[3]/span[2]/span/text()').get()
    img=ol.xpath(r'./div/div/div[2]/p/a/@href').get()
    print(oo)
    print(img)



#     for img in imgs:
#         print(img)
#     try:
#         next_url = r'http://' + re.search(r'<a title="Older Comments" href="//(.*)" class="previous-comment-page">下一页</a>',response.text).group(1)
#     except:
#         break
#     url_l.append(next_url)
#     print(url_l[-1])
# print('End',len(url_l))
