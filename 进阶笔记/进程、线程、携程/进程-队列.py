from multiprocessing import Queue
from multiprocessing import Pool

'''
队列：
q = Queue(n)  创建队列，n为队列的最大长度
q.put(x,timeout=s)  往队列中添加元素，x为被添加的元素,s为添加元素操作的过期秒数
q.get(timeout=s)  从队列取出元素，s为取出元素操作的过期秒数
q.qsize()  当前队列已放入的元素数量
q.full()  返回当前队列是否已满
q.empty()  返回当前队列是否空的
q.put_nowait()  非阻塞式放入元素
q.get_nowait()  非阻塞式取出元素

'''


if __name__ == '__main__':
    pool = Pool(5)
    q = Queue(5)
    q.put('A')
    q.put('B')
    q.put('C')
    q.put('D')
    q.put('E')
    print(q.qsize())
    print(f'取出元素：{q.get()}')
    q.get_nowait()
    q.put_nowait(1)
    if q.full():
        print('队列已满')
    else:
        q.put('F', timeout=3)
        # q.put('G', timeout=3)
    print(q.qsize())
