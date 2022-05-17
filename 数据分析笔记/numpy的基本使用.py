import numpy as np
import pandas as pd

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180,
           168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185,
           191]
''''np.array()函数：把列表转换成numpy对象'''
heights_arr = np.array(heights)

'''numpy对象.size：统计numpy对象元素个数'''
print(f'heights_arr.size:{heights_arr.size}')

'''numpy对象.shape：统计numpy对象的形状（纬度）'''
print(f'heights_arr.shape数组的形状（纬度）:{heights_arr.shape}')

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56,
        55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
heights_and_ages_arr = np.array(heights_and_ages)
print(f'heights_and_ages_arr.shape:{heights_and_ages_arr.shape}')

'''numpy对象.reshape(n，m)：重塑numpy一维数组为n纬数组，每个数组m个元素。n,m使用-1代表自动计算数量。'''
print(f'heights_and_ages_arr.reshape((2,-1)):\n{heights_and_ages_arr.reshape((2, -1))}')

'''numpy对象.dtype:显示所有元素的数据类型'''
print(f'heights_and_ages_arr.dtype:{heights_and_ages_arr.dtype}')

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183,
                 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185,
                 188, 188, 182, 185, 191]
heights_float_arr = np.array(heights_float)

'''numpy对象自动统一元素类型'''
print(heights_float_arr)

'''numpy对象支持以下类型：int、float、bool,数据类型后面的数字表示该数据类型的位长度'''
print(f'heights_float_arr.dtype:{heights_float_arr.dtype}')

'''打印heights_arr第5个元素的值'''
print(f'heights_arr[4]:{heights_arr[4]}')

'''numpy数组重新赋值'''
heights_and_ages_arr = heights_and_ages_arr.reshape((2, 45))

'''打印heights_and_ages_arr第2个数组第3个元素'''
print(f'heights_and_ages_arr[1,2]:{heights_and_ages_arr[1, 2]}')

'''打印heights_and_ages_arr第一个数组1~3号元素,结果会以列表类型返回'''
print(f'heights_and_ages_arr[0,0:3]:{heights_and_ages_arr[0, 0:3]}')

'''打印heights_and_ages_arr整个第1列'''
print(f'heights_and_ages_arr[:, 0]:{heights_and_ages_arr[:, 0]}')

'''修改heights_arr的第5个元素'''
heights_arr[4] = 165

'''修改heights_and_ages_arr第1个数组，第5个元素'''
heights_and_ages_arr[0, 4] = 165

'''修改heights_and_ages_arr第1个数组所有元素'''
heights_and_ages_arr[0, :] = 180

'''修改heights_and_ages_arr第1、2个数组，每个数组的第1、2个元素'''
heights_and_ages_arr[:2, :2] = 1688

'''用列表给numpy数值赋值'''
heights_and_ages_arr[:, 0] = [190, 58]

'''用新的numpy数组给numpy数组赋值，2个numpy数组必须形状（纬度）一致'''
new_record = np.array([[180, 183, 190], [54, 50, 69]])
heights_and_ages_arr[:, 0:3] = new_record

'''np.vstack():把2个相同形状的numpy array数组按行（列不变）堆叠成1个新数组'''
heights_arr = np.array(heights)
ages_arr = np.array(ages)
heights_arr = heights_arr.reshape((1, 45))
ages_arr = ages_arr.reshape((1, 45))
height_age_arr = np.vstack((heights_arr, ages_arr))
'''np.concatenate((arr1,arr2),axis=0):把2个相同形状的numpy array数组按列（行不变）堆叠成1个新数组。等同于np.vstack()'''
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=0)

'''np.hstack():把2个相同形状的numpy array数组按列（行不变）堆叠成1个新数组。np.concatenate((arr1,arr2),axis=1)可实现相同效果'''
heights_arr = heights_arr.reshape((45, 1))
ages_arr = ages_arr.reshape((45, 1))
height_age_arr = np.hstack((heights_arr, ages_arr))

'''numpy数组的乘法'''
print(f'height_age_arr[:, 0] * 0.0328084:{height_age_arr[:, 0] * 0.0328084}')

'''numpy数组.sum(axis=0):numpy数组的和。axis=0：每个数组分别求和'''
print(f'height_age_arr.sum():{height_age_arr.sum()}')
print(f'height_age_arr.sum(axis=0):{height_age_arr.sum(axis=0)}')
print(f'height_age_arr.sum(axis=1):{height_age_arr.sum(axis=1)}')


''' .min(), .max(), .mean()：与.sum()相同的用法分别求最小值、最大值、均值'''
print(f'height_age_arr.min(axis=0):{height_age_arr.min(axis=0)}')
print(f'height_age_arr.max(axis=0):{height_age_arr.max(axis=0)}')
print(f'height_age_arr.mean(axis=0):{height_age_arr.mean(axis=0)}')

'''比较小于50的元素，返回比较结果的bool值列表,比较方式遵循python的语法'''
print(f'height_age_arr[:, 1] < 50:\n{height_age_arr[:, 1] < 50}')

'''numpy对象(条件).sum()：统计numpy对象数组内数组元素符合条件的个数'''
print(f'(height_age_arr[:, 1] < 50).sum():{(height_age_arr[:, 1] < 50).sum()}')

'''height_age_arr第1个数组大于等于182的元素建立一维数组mask（蒙版）'''
mask = height_age_arr[:, 0] >= 182
print(f' height_age_arr[:, 0] >= 182:{mask}')

'''mask.sum()：统计符合条件的元素数量'''
print('统计符合条件的元素数量mask.sum()：',mask.sum())

'''以mask（蒙版）过滤height_age_arr'''
tall_presidents = height_age_arr[mask, ]
print(f'tall_presidents.shape:{tall_presidents.shape}')

'''height_age_arr第1个数组大于等于182,并且第2个数组小于或等于50的元素建立一维数组mask（蒙版）'''
mask = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)
print(height_age_arr[mask,])

'''df.values()函数：pandas对象转换成numpy对象'''
df = pd.read_csv('../Scikit-learn机器学习库/titanic.csv')
print('data.Series转换成numpy对象:\n',df['Fare'].values[0:10])
print('data.dataFrame转换成numpy对象:\n',df[['Pclass','Fare','Age']].values[0:10])

'''df.dataFrame的形状（纬度）'''
print('df.dataFrame的形状（纬度）:',df.shape)
