import pandas as pd
import numpy as np

'''转换成pd.Series对象的3种方式，这3种方法都已指定索引（index）'''
print(pd.Series([1, 2, 3], index=['a', 'b', 'c']))  # with index
print(pd.Series(np.array([1, 2, 3]), index=['a', 'b', 'c']))  # from a 1darray
print(pd.Series({'a': 1, 'b': 2, 'c': 3}))  # from a dict

'''通过索引查找pd.Series对象中的数据'''
series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(series['a'])

'''pd.Series：是pandsa的其中一种数据结构，可以看作是带有索引名或行名的numpy 一维数组'''

'''创建pd.DataFramme数据，pd.DataFramme可以视为pd.Series的集合，是pandas的另一种数据结构，是一个二维数组'''
wine_dict = {
    'red_wine': [3, 6, 5],
    'white_wine': [5, 0, 10]
}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
print(sales)

'''通过字段名查找pd.DataFrame对象中的数据'''
print(sales['white_wine'])

'''读取CSV文件作为pd.DataFrame的数据源'''
presidents_df = pd.read_csv('president_heights_party.csv', index_col='name')
print(presidents_df)

'''获取数据表的行数。.shrpe[0]与len(df)效果相同'''
print(f'数据表的行数：{presidents_df.shape[0]}')
print(f'数据表的行数：{len(presidents_df)}')
'''获取数据表的列数'''
print(f'数据表的列数：{presidents_df.shape[1]}')

'''获取数据表的元素个数'''
print(f'数据表的元素总个数：{presidents_df.size}')

'''.head()：获取数据表前n行数据，n不填写默认为5行'''
n = 3
print(f'数据表前{n}行数据：\n{presidents_df.head(n)}')

'''.tail()：获取数据表后n行数据，n不填写默认为5行'''
n = 3
print(f'数据表后{n}行数据：\n{presidents_df.tail(n)}')

'''.info()：获取数据表的概述信息，自带输出（print），不需要print'''
print(f'数据表的概述信息：')
presidents_df.info()

'''.loc['index']：通过索引查找数据，index为索引名'''
print(f'residents_df.loc["Abraham Lincoln"]：\n{presidents_df.loc["Abraham Lincoln"]}')
'''.loc['index']返回的结果为<class 'pandas.core.series.Series'>数据类型，是一维数组'''
print("数组的数据类型为：", type(presidents_df.loc['Abraham Lincoln']))
print("presidents_df.loc['Abraham Lincoln'].shape：", presidents_df.loc['Abraham Lincoln'].shape)

'''.loc['index1':'index2']：进行索引范围查询，返回的数据是pd.DataFrame数据表类型'''
print("presidents_df.loc['Abraham Lincoln':'Ulysses S. Grant']：\n",
      presidents_df.loc['Abraham Lincoln':'Ulysses S. Grant'])

'''.iloc[n]：进行行数索引，从0开始，返回的结果与.loc一致'''
print(presidents_df.iloc[0])
print(presidents_df.iloc[0:3])
print(presidents_df.iloc[-1:])

'''.columns：查询数据表的所有字段名称，返回的是一个对象'''
print('所有字段名称：', presidents_df.columns)

'''pd.DataFrame['字段名']：查询数据表该字段的所有数据'''
print("height的所有数据：", presidents_df['height'])
'''pd.DataFrame['字段名'][n:m]：m=0时查询数据表该字段第n行数据，[n:m]表示查询第n行~第m行的数据'''
print(presidents_df['height'][3])
print(presidents_df['height'][0:2])
'''pd.DataFram.字段名：查询数据表该字段的所有数据'''
print(presidents_df.height)
print(presidents_df.height[0:3])

'''pd.DataFrame[['字段名1','字段名2']].head(n)：查询字段名1和字段名2前n行的数据'''
n = 5
print(f"height和age前{n}行的数据：\n", presidents_df[['height', 'age']].head(n))

'''使用.loc[:,'字段名1':'字段名2'].head(n)：查询从字段1~字段2的前3条数据'''
n = 3
print("presidents_df.loc[:, 'order':'height'].head(n)：\n", presidents_df.loc[:, 'order':'height'].head(n))

'''pd.DataFrame.min()：获取数据表每个字段的最小值'''
print('presidents_df.min()：\n', presidents_df.min())

'''pd.DataFrame.max()：获取数据表每个字段的最大值'''
print('presidents_df.max()：\n', presidents_df.max())

'''pd.DataFrame.mean()：获取数据表每个字段的平均值。平均值会自动缩减成只显示数值类型字段的平均值'''
print('presidents_df.mean()：\n', presidents_df.mean())

'''pd.DataFrame.median()：获取数据表每个字段的中位数。中位数会自动缩减成只显示数值类型字段的中位数'''
print('presidents_df.median()：\n', presidents_df.median())

'''pd.DataFrame.quantile([0.25,0.5,0.75,1])：获取数据表25%,50%,75%,100%的分位数。分位数会自动缩减成只显示数值类型字段的分位数。 .quantile(0.5) 和 .median()效果相同。 '''
print('presidents_df.quantile([0.25, 0.5, 0.75, 1])：\n', presidents_df.quantile([0.25, 0.5, 0.75, 1]))

'''.var()：获取数据表每个字段的方差。方差是每个数据点相对于整个数据集均值的平均平方偏差'''
print('presidents_df.var()：\n', presidents_df.var())

'''.std()：获取数据表每个字段的标准差。标准差是离均差平方的算术平均数（即：方差）的算术平方根'''
print('presidents_df.std()：\n', presidents_df.std())

'''.describe()：获取数据表每个字段的元素个数、平均值、标准差、最小值、25%分位数，50%分位数，75%分位数，最大值等数据。'''
print('presidents_df.describe()：\n', presidents_df.describe())

'''.value_counts()：获取分类变量各个变量的非空数据数量。分类变量是从一组有限的类别中取单一值的变量。'''
print("presidents_df['party'].value_counts()：\n", presidents_df['party'].value_counts())

'''使用.describe()获取分类变量的摘要统计'''
print("presidents_df['party'].describe()：\n", presidents_df['party'].describe())

'''df['字段名'].nunique()：统计分类变量有多少种不同的值'''
print("presidents_df['party'].nunique()：",presidents_df['party'].nunique())

'''.groupby('字段名')：根据字段名对数据表进行的数据进行分组，然后可以根据分组进行计算（如.describe(),.min(),.max(),.mean()等等。返回的是DataFrameGroupBy对象'''
print("presidents_df.groupby('party').describe()：\n", presidents_df.groupby('party').describe())

'''DataFrame.groupby('字段名1')['字段名2'].median()：以字段名1作为分类，分别统计字段2的中位数'''
print("presidents_df.groupby('party')['height'].median()：\n", presidents_df.groupby('party')['height'].median())

'''groupby对象.agg([汇聚方法名1,汇聚方法名2,汇聚方法名3,...])：同时获取多条汇聚计算结果，如最小值、中位数、最大值等。汇聚方法名可以使用字符串、np.方法名、方法名等三种方式表示'''
print("presidents_df.groupby('party')['height'].agg(['min', min, np.min, 'median', max])：\n",
      presidents_df.groupby('party')['height'].agg(['min', min, np.min, 'median', max]))

'''groupby对象.agg({'字段名1':[汇聚方法名1,汇聚方法名2],'字段名2':[汇聚方法名1,汇聚方法名2]})：可对groupby对象不同字段使用不同的汇聚方法'''
print("presidents_df.groupby('party').agg({'height': [np.median, np.mean], 'age': [min, max]})：\n",
      presidents_df.groupby('party').agg({'height': [np.median, np.mean], 'age': [min, max]}))

def double(x):
    return x*2
'''.agg([方法名])：对数据表的每个数据进行批量运算'''
print(presidents_df.agg([double,]))

'''.agg([方法名])：对数据表的指定字段的每个数据进行批量运算'''
print(presidents_df['order'].agg([double]))
