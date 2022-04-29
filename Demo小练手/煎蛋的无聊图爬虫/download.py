import os

import requests


def download(url,path,file_name):
    '''传入音频实际地址，保存的文件名下载对应音频到工作目录'''
    if os.path.isfile(f'{path}\{file_name}'):
        print((f'{path}\{file_name}..................................文件已存在，不重新下载'))
        return False
    else:
        response = requests.get(url)
        # print(response.text)
        with open(f'{path}\{file_name}', 'wb') as f:
            f.write(response.content)
        return print(f'{file_name}....................下载完成')