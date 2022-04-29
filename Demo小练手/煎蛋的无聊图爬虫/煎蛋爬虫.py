import re
import parsel
import check_filename
import download
import requests

url_l = [r'http://jandan.net/pic', ]
path=r'C:\Users\wacky\Desktop\煎蛋图片爬虫\煎蛋图片'
dic={}

#<a href="//tva1.sinaimg.cn/large/005OuxLily1gxwwb59o5ig30go09mheg.gif" target="_blank" class="view_img_link" referrerPolicy="no-referrer">[查看原图]</a>

while True:
    response = requests.get(url_l[-1], )
    html_data = response.text
    selector = parsel.Selector(html_data)
    ols = selector.xpath(r'//*[@id="comments"]/ol/li')
    for ol in ols:
        oo = ol.xpath(r'./div/div/div[3]/span[2]/span/text()').get()
        img = ol.xpath(r'./div/div/div[2]/p/a/@href').get()

        if type(oo) == type(' '):
            if int(oo) > 300:
                img_url = 'http:' + img
                file_name=re.search(r'.+/.*/(.*)',img)
                file_name=check_filename.check_filename(file_name.group(1))
                download.download(img_url,path,file_name)

    # imgs=re.findall(f'<a href="//(.*?)" target="_blank"',response.text,)
    # for img in imgs:
    #     img_url='http://'+img
    #     file_name=re.search(r'.+/.*/(.*)',img)
    #     file_name=check_filename.check_filename(file_name.group(1))
    #     download.download(img_url,path,file_name)
        # print(img)
    try:
        next_url = r'http://' + re.search(r'<a title="Older Comments" href="//(.*)" class="previous-comment-page">下一页</a>',response.text).group(1)
    except:
        break
    url_l.append(next_url)
    print(url_l[-1])
print('End',len(url_l))
