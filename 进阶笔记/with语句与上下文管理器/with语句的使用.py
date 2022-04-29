try:
    file=open('logx.txt','w')
    result=file.read()
    print(result)

except Exception as e:
    print(e)

finally:
    file.close()

with open('logx.txt','a+') as f:
    result = f.read()
    print(result)
    print('with结束')

