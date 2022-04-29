import threading

n=0

def task(x):
    global n
    for i in range(100000000):

        n+=1

    print(f'-------------------》task{x}中你的值：{n}')

if __name__ == '__main__':
    t1=threading.Thread(target=task,args=(1,))
    t2=threading.Thread(target=task,args=(2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f'最后打印n的值：{n}')

