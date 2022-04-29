import time

import gevent
from greenlet import greenlet
from gevent import monkey

'''  #不用第三方库，而是采用yield方式实现协程
def task1():
    for i in range(5):
        print('A'+str(i))
        yield
        time.sleep(0.2)

def task2():
    for i in range(5):
        print('B'+str(i))
        yield
        time.sleep(0.2)

if __name__ == '__main__':
    g1=task1()
    g2=task2()

    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
'''


'''  #使用greenlet库实现人工切换协程
def a():
    for i in range(5):
        print('A'+str(i))
        gb.switch()
        time.sleep(0.2)

def b():
    for i in range(2):
        print('B'+str(i))
        gc.switch()
        time.sleep(0.2)

def c():
    for i in range(3):
        print('C'+str(i))
        ga.switch()
        time.sleep(0.2)

if __name__ == '__main__':
    ga=greenlet(a)
    gb=greenlet(b)
    gc=greenlet(c)

    ga.switch()
'''

# '''  #使用gevent实现自动切换协程
monkey.patch_all()

def a():
    for i in range(5):
        print('A'+str(i))
        time.sleep(0.2)

def b():
    for i in range(2):
        print('B'+str(i))
        time.sleep(0.2)

def c():
    for i in range(3):
        print('C'+str(i))
        time.sleep(0.2)

if __name__ == '__main__':
    g1=gevent.spawn(a)
    g2=gevent.spawn(b)
    g3=gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()

    print('END')
# '''