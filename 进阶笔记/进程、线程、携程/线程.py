'''
线程：
t = threading.Thread(target=download, name='d_l', args=(random.random()*2,))
t.start()

线程共享全局变量

GIL  全局解析器锁

线程状态：
1.新建
2.就绪
3.运行
4.阻塞  阻塞结束后回到就绪状态，等待分配计算资源
5.结束

'''
import random
import threading
from time import sleep

img = ['girl.jpg', 'boy.jpg', 'man.jpg']


def download(n):
    for i in img:
        print((f'正在下载：{i}'))
        sleep(n)
        print(f'下载{i}成功')

def listen_music(n):
    musics=['大碗宽面','土耳其冰激凌','沙漠骆驼','十年']
    for music in musics:
        print(f'正在听:{music}')
        sleep(n)

if __name__ == '__main__':

    t_d = threading.Thread(target=download, name='d_l', args=(random.random()*2,))
    t_l=threading.Thread(target=listen_music,args=(random.random()*2,))

    t_d.start()
    t_l.start()


    n=1
    # while True:
    #     print(n)
    #     n+=1
    #     sleep(1)