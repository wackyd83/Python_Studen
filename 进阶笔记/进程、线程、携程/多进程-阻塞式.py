import os
import time
from multiprocessing import Process
from multiprocessing import Pool
from random import random
from time import sleep

'''
进程池：
pool=Pool(n)  创建进程池，n为最大进程数量
pool.apply()  阻塞式添加任务，任务只能逐个执行完后才执行下一个，与进程池内空进程数量无关
pool.apply_async()  非阻塞式添加任务，任务逐个添加，直到进程池内空进程都被占满，待任意进程任务完成后再添加后续任务
pool.close()  关闭进程池，关闭后不能再往进程池添加任务
pool.join()  主进程等待进程池内所有进程任务都完结后才关闭
'''

def job(job_name):
    print(f'开始做{job_name}任务')
    start = time.time()
    sleep(random() * 2)
    end = time.time()
    print(f'完成任务:{job_name}  用时：{end - start}  任务ID:{os.getpid()}')
    # return (f'完成任务:{job_name}  用时：{end - start}  任务ID:{os.getpid()}')


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['发呆', '吃饭', '听歌', '打机', '洗衫', '看电影', '看书', '听故仔', '睇新闻']
    nums = [1, 2, 3, 4, 5, 6, 7]
    for i in nums:
        pool.apply_async(job, args=(i,))
    for i in tasks:
        pool.apply(job, args=(i,))

    pool.close()

    pool.join()
    print('OVER!!!!!!!!!!!!!!!!!!!!!!!!!!')
