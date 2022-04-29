import time
import threading

n = 0
l1 = threading.RLock()
l2 = threading.RLock()

def task1(x):
    global n
    t1 = 0
    run_time1 = 0
    print(f'开始执行task{x}')

    for i1 in range(100000000):
        l1.acquire()
        star1 = time.time()
        n += 1
        t1 += 1
        if i1 == 75124549:
            print(f'i1运行{75124549}次时，n值为:{n}')
        end1 = time.time()
        run_time1 += end1 - star1
        l1.release()

    print(f'-------------------》task{x}中你的值：{n}')
    print(f'-------------------》task{x}执行了{t1}次，耗时{run_time1}秒')


def task2(x):
    global n
    t2 = 0
    run_time2 = 0
    print(f'开始执行task{x}')

    for i2 in range(100000000):
        l2.acquire()
        star2 = time.time()
        n += 1
        t2 += 1
        if i2 == 75124549:
            print(f't2运行{75124549}次时，n值为:{n}')
        end2 = time.time()
        run_time2 += end2 - star2
        l2.release()

    print(f'-------------------》task2中你的值：{n}')
    print(f'-------------------》task2执行了{t2}次，耗时{run_time2}秒')


if __name__ == '__main__':
    tt1 = threading.Thread(target=task1, args=(1,))
    tt2 = threading.Thread(target=task2, args=(2,))

    tt1.start()
    tt2.start()

    tt1.join()
    tt2.join()

    print(f'最后打印n的值：{n}')
