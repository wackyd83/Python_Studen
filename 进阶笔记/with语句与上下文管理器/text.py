from my_open import *

with my_open('logx.txt','r') as f:
    file=f.read()
    print(file)

