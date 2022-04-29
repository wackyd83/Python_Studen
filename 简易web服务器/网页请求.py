import parsel
import requests

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

def download_media(url,media_name):
    response = requests.get(url, headers=headers)

    with open(f'{media_name}.mp3','wb') as f:
        f.write(response.content)


url = 'https://audiopay.cos.tx.xmcdn.com/download/1.0.0/group1/M08/95/28/wKgJN1vCozbAq1MkAEZwqkFarV4327.m4a?sign=e81e50f3db8f22fc19041596baba1aee&buy_key=FM&timestamp=1636124365947000&token=7236&duration=570'

download_media(url,'bb')