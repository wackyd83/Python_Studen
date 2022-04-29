# logging日志：用来记录程序运行时的日志信息

import logging

# 设置logging日志的配置信息
# level设置输出级别
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s',
                    filename='logx.txt',
                    filemode='w')
logging.FileHandler(encoding='utf-8',filename='logx.txt')


logging.debug('我就是一个bug1111111111')
logging.info('我就是一个info')
logging.warning('我就是一个warning111111111')
logging.error('我就是一个error')
logging.critical('我就是一个critical')

# 默认是warning级别，只有大于等于warning级别的日志才会输出显示
