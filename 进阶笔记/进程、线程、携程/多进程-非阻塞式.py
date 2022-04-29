import os
import time
from multiprocessing import Process
from multiprocessing import Pool
from random import random
from time import sleep


def job(job_name):
    print(f'开始做{job_name}任务')
    start = time.time()
    sleep(random() * 2)
    end = time.time()
    print(f'完成任务:{job_name}  用时：{end - start}  任务ID:{os.getpid()}')
    return (f'完成任务:{job_name}  用时：{end - start}  任务ID:{os.getpid()}')

def call_back_func(n):
    print(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks=['发呆','吃饭','听歌','打机','洗衫','看电影','看书','听故仔','睇新闻']
    for i in tasks:
        pool.apply_async(job,args=(i,),callback=call_back_func)
    pool.close()
    pool.join()
    print('OVER!!!!!!!!!!!!!!!!!!!!!!!!!!')
