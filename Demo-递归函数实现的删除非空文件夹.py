import os

del_path = r'E:\test_dir\test_dir'
what_del_files = []
what_del_dirs = []


def func(path):
    for i in os.listdir(path):
        full_path = os.path.abspath(os.path.join(path, i))

        if os.path.isdir(full_path):
            # print('{}这是一个文件夹'.format(i))
            if os.listdir(full_path) == []:
                # print('{}是个空文件夹'.format(i))
                global what_del_dirs
                what_del_dirs.append(full_path)
                os.rmdir(full_path)
            else:
                func(full_path)
                what_del_dirs.append(full_path)
                os.rmdir(full_path)

        #
        #
        elif os.path.isfile(full_path):
            # print('{}这是一个文件'.format(i))
            global what_del_files
            what_del_files.append(full_path)
            os.remove(full_path)


func(del_path)

print('删除成功！！')

print('\n已删除以下文件夹：')
for i in what_del_dirs:
    print(i)

print('''
***********************************************************************************
已删除以下文件：''')
for i in what_del_files:
    print(i)
