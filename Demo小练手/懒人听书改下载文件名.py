import os, sys, base64, re



def rename(old_file_name):
    transtab = old_file_name.maketrans({'_':'+' , '-':'/' })
    new_name=old_file_name.translate(transtab)
    decodestr = base64.b64decode(new_name)
    new_file_name=decodestr.decode('utf-8', errors='ignore')+'.mp3'
    return new_file_name

root_path = 'E:\\tingshu\\.5aSn6YGT5pyd5aSp77yI5aSa5Lq657K-5ZOB77yJ'

path_list = os.listdir(root_path)
for i in path_list:
    Old_path=os.path.join(root_path,i)
    # print(Old_path)
    if os.path.isdir(Old_path):
        continue
    else:
        New_path=os.path.join(root_path,rename(i))
        os.rename(Old_path,New_path)
        print(i,'名称改为：',rename(i))



