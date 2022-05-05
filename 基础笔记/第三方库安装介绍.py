#pillow  图片处理的第三方库
#import pillow
import requests #网络请求库


response=requests.get('https://www.12306.cn/index/')

print(response.text)