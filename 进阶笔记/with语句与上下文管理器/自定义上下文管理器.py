# 上下文管理器：在类里面实现__enter__和__exit__方法，创建的对象就是上下文管理器


#  自定义的上下文管理器
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        #  上文方法，负责返回操作对象资源，比如：文件对象，数据库连接对象
        self.file=open(self.file_name,self.file_mode)
        return self.file

    #   当with语句执行完成后，自动执行__exit__方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        #  下文方法，负责释放对象资源，比如：关闭文件，关闭数据库连接对象
        print('over')
        self.file.close()



#   with语句结合上下文管理器对象使用
with File('logx.txt','a+') as f:
    file_data=f.read()
    print(file_data)
