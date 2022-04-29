import threading
import queue
import random
import time

def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put(f'生产者生产数据：{num}')
        print(f'生产者生产数据:{num}')
        time.sleep(0.5)
        i += 1
    q.put(None)
    q.task_done()


def consume(q):
    while True:
        item=q.get()
        if item is None:
            break
        print(f'消费者获得：{item}')
        time.sleep(1.1)
        q.task_done()

if __name__ == '__main__':
    q=queue.Queue(10)
    arr=[]

    tp=threading.Thread(target=produce,args=(q,))
    tp.start()

    tc=threading.Thread(target=consume,args=(q,))
    tc.start()

    tp.join()
    tc.join()
    print('END')