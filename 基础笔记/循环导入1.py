from 循环导入2 import  func1


def task1():
    print('----------task1------------')


def task2():
    print('------------task2-------------')
    func1()

if __name__=='__main__':
    task2()