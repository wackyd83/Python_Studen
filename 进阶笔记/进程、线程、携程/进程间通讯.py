from multiprocessing import Process
from multiprocessing import Queue
from time import sleep

img = ['girl.jpg', 'boy.jpg', 'man.jpg']


def download(q):
    for i in img:
        print((f'正在下载：{i}'))
        sleep(1)
        q.put(i)


def getfile(q):
    while not q.empty():
        file = q.get()
        print(f'{file}保存成功')
    print('全部保存完毕')


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print('OVER!!!!!!!!!!!!!!!!!!!!!!!!!!')
