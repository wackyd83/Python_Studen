import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''在 sklearn.model_selection 中使用 train_test_split区分训练集和测试集'''
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')

'''.drop()：删除id字段。axis=1：按纵列进行操作。inplace=True：修改原变量的值'''
iris.drop('id', axis=1, inplace=True)

print('iris数据表的统计信息：\n', iris.describe())

'''需要判断数据集是平衡数据集还是不平衡数据集。当数据集不平衡时，将使用稍微不同的分析。因此，重要的是要了解数据是平衡的还是不平衡的。平衡：每种类型的数据数量相同。'''
print(iris.groupby('species').size())  # 显示每个分类的数量
print(iris['species'].value_counts())  # 显示每个分类的数量

'''这使我们对输入变量的分布有了更清晰的认识，表明萼片长度和萼片宽度都具有正态（高斯）分布。也就是说，分布具有漂亮的对称钟形。但是，花瓣的长度不正常。它的图显示了两种模式，一个峰值出现在 0 附近，另一个峰值出现在 5 附近。观察到花瓣宽度的模式较少。'''
iris.hist()
plt.show()

'''根据数据类型绘制散点图'''
inv_name_dict = {'iris-setosa': 0, 'iris-versicolor': 1, 'iris-virginica': 2}
'''根据种类获取颜色编码'''
colors = [inv_name_dict[item] for item in iris['species']]
'''根据数据集中每种类型的花瓣数据（sepal_len、sepal_wd）绘制散点图。使用 sepal_length 和 sepal_width特征，我们可以区分 iris-setosa 和其他；'''
scatter = plt.scatter(iris['sepal_len'], iris['sepal_wd'], c=colors)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.legend(handles=scatter.legend_elements()[0],
           labels=inv_name_dict.keys())
plt.savefig("plot_sepal.png")
plt.show()
'''根据数据集中每种类型的花瓣数据（petal_len、petal_wd）绘制散点图。将 iris-versicolor 从 iris-virginica 中分离出来更难，因为绿色和黄色数据点有重叠。 同样，花瓣长度和宽度之间：iris-versicolor 和 iris-virginica 之间的边界仍然有些模糊，这表明某些分类器存在困难。在训练时决定我们应该使用哪些功能是值得牢记的。'''
scatter = plt.scatter(iris['petal_len'], iris['petal_wd'], c=colors)
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.legend(handles=scatter.legend_elements()[0], labels=inv_name_dict.keys())
plt.savefig("plot_petal.png")
plt.show()

'''pd.plotting.scatter_matrix()：绘制各个字段组合的散点图，以便观察哪些字段组合可以明显地区分类型。'''
pd.plotting.scatter_matrix(iris, c=colors)
plt.savefig("plot_matrix.png")
plt.show()

'''K最近邻：待测试点的k参数范围内哪种类型最多，就把待测试点推断为该类型。例如：有两个类：蓝色方块和红色三角形。基于 3nn 算法，即当 k 为 3 时，我们应该为具有未知标签的绿点分配什么标签？在距离绿点（实线圆圈）最近的 3 个数据点中，两个是红色三角形，一个是蓝色正方形，因此绿色点被预测为红色三角形。如果 k 为 5（虚线圆圈），则将其分类为蓝色方块（3 个蓝色方块对 2 个红色三角形，蓝色方块占多数）。'''

'''早些时候我们发现花瓣的长度和宽度是区分物种的最有用的特征。然后我们定义特征和标签如下：'''
X = iris[['petal_len', 'petal_wd']]
y = iris['species']

'''我们使用 70-30 的拆分，即 70% 的数据用于训练，30% 用于测试。请注意，我们指定拆分按标签y分层。这样做是为了确保标签的分布在训练集和测试集中保持相似.'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1, stratify=y)

print(y_train.value_counts())
print(y_test.value_counts())

'''导入K最近邻（knn）模型'''
from sklearn.neighbors import KNeighborsClassifier

'''创建K最近邻（knn）模型实例，并设置超参数K=5。超参数：在机器学习的上下文中，超参数是在开始学习过程之前设置值的参数，而不是通过训练得到的参数数据。通常情况下，需要对超参数进行优化，给学习机选择一组最优超参数，以提高学习的性能和效果。'''
knn = KNeighborsClassifier(n_neighbors=5)
'''模型拟合（训练）'''
knn.fit(X_train, y_train)

'''.predict()：对分类进行预测'''
pred = knn.predict(X_test)
print('对测试集的预测：', pred[:5])

'''.predict_prob：以数组形式输出目标的概率'''
y_pred_prob = knn.predict_proba(X_test)
print('第 11 和第 12 朵花的预测概率：\n', y_pred_prob[10:12])
'''
输出： 
[[1.  0.  0. ]
 [0.  0.2 0.8]]
第 11 朵花被预测为 iris-setosa 的概率为 1，iris-versicolor 和 iris-virginica 均为 0。对于下一朵花，有 20% 的机会将其分类为 iris- versicolor，但 80% 的机会是 iris-virginica。它告诉我们的是，在测试集中第 12 朵花的五个最近邻居中，1 个是 iris-versicolor，其余 4 个是 iris-virginica。要查看相应的预测
'''

'''.score()：准确性，计算预测标签与观察标签完全匹配的数据点的比例。'''
y_pred = knn.predict(X_test)
print('(y_pred == y_test.values).sum()：', (y_pred == y_test.values).sum())
print('y_test.size：', y_test.size)

print('准确性y_pred == y_test.values).sum() / y_test.size：\n', (y_pred == y_test.values).sum() / y_test.size)
print('准确性knn.score(X_test, y_test)：\n', knn.score(X_test, y_test))

'''训练集的分类数量不相同：如果每个类中的观察数量不相等，或者数据集中有两个以上的类，则单独的分类准确性可能会产生误导。计算混淆矩阵将更好地了解分类正确的内容以及错误的类型。'''
'''混淆矩阵：它是按每个类别细分的正确和错误预测计数的摘要。 在对虹膜进行分类时，我们可以使用模块sklearn.metrics下的confusion_matrix() ：'''
from sklearn.metrics import confusion_matrix  # 导入混沌矩阵

print('混沌矩阵confusion_matrix(y_test, y_pred)：\n', confusion_matrix(y_test, y_pred))

'''导入plot_confusion_matrix模块,把混沌矩阵可视化'''
from sklearn.metrics import plot_confusion_matrix

plot_confusion_matrix(knn, X_test, y_test, cmap=plt.cm.Blues);
plt.savefig("plot_confusion_matrix.png")
plt.show()
'''
输出：
[[15  0  0]
 [ 0 15  0]
 [ 0  1 14]]
第一行对应实际的鸢尾花；[15, 0, 0] 表示 iris-setosa 有 15 个被正确预测，没有一个被错误标记；而最后一行 [0, 1, 14] 表明在 15 个实际的 iris-virginica 中，0 个被预测为 iris-setosa，1 个被预测为 iris-versicolor，其余 14 个被正确识别为 iris-virginica。这与我们在探索性数据分析过程中的观察结果一致，即散点图上两个物种之间存在一些重叠，区分鸢尾花和鸢尾花比识别鸢尾花更难。
'''

'''交叉验证（K-fold Cross Validation）：以前我们在拟合模型之前进行了训练测试拆分，以便我们可以在测试数据上报告模型性能。这是一种简单的交叉验证技术，也称为保持法。但是，拆分是随机的，因此模型性能可能对数据的拆分方式很敏感。为了克服这个问题，我们引入了k 折交叉验证。 在 k 折交叉验证中，将数据分为k 个子集。然后将holdout方法重复k次，每次将k个子集中的一个作为测试集，将其他k-1个子集组合起来训练模型。然后在 k 次试验中对准确度进行平均，以提供模型的总体有效性。这样，所有的数据点都被使用了；并且有更多的指标，所以我们不依赖一个测试数据来进行模型性能评估。'''
from sklearn.model_selection import cross_val_score

knn_cv = KNeighborsClassifier(n_neighbors=3)  # 创建一个用于交叉验证的新模型knn_cv
cv_scores = cross_val_score(knn_cv, X, y, cv=10)  # 进行5次交叉验证：cv=5
print('5次交叉验证的结果：\n', cv_scores)
print('平均准确性：', cv_scores.mean())
'''作为一般规则，首选 5 倍或 10 倍交叉验证；但没有正式的规则。随着 k 变大，训练集和重采样子集之间的大小差异变小。随着这种差异的减小，该技术的偏差变得更小。'''

'''网络搜索Grid Search：用于调整优化K超参数。交叉验证和网格搜索调整参数的技术适用于分类和回归问题。'''
from sklearn.model_selection import GridSearchCV

# create new a knn model.创建一个新的knn模型knn2
knn2 = KNeighborsClassifier()
# create a dict of all values we want to test for n_neighbors.创建一个用于存放k超参数范围的字典param_grid
param_grid = {'n_neighbors': np.arange(2, 10)}
# use gridsearch to test all values for n_neighbors.使用gridsearch函数测试k超参数范围的准确性
knn_gscv = GridSearchCV(knn2, param_grid, cv=5)
# fit model to data.拟合模型
knn_gscv.fit(X, y)
print('最佳k超参数的值为：', knn_gscv.best_params_)
print('最佳k超参数的准确性为：', knn_gscv.best_score_)

'''测试得出k超参数的最佳数值后，构建最终的模型'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = pd.read_csv('iris.csv')

iris.drop('id', axis=1, inplace=True)

X = iris[['petal_len', 'petal_wd']]
y = iris['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1, stratify=y)

from sklearn.model_selection import GridSearchCV

# create new a knn model
knn2 = KNeighborsClassifier()
# create a dict of all values we want to test for n_neighbors
param_grid = {'n_neighbors': np.arange(2, 20)}
# use gridsearch to test all values for n_neighbors
knn_gscv = GridSearchCV(knn2, param_grid, cv=5)
# fit model to data
knn_gscv.fit(X, y)

knn_final = KNeighborsClassifier(n_neighbors=knn_gscv.best_params_['n_neighbors'])
knn_final.fit(X, y)

y_pred = knn_final.predict(X)
print(knn_final.score(X, y))

'''.predict(np.array())数据预测'''
new_data = np.array([3.76, 1.20])  # 把需要预测的一组数据转换为二维数组
new_data = new_data.reshape(1, -1)
print('预测结果为：', knn_final.predict(new_data))

'''同时预测多组数据，数据以一维数组返回'''
new_data = np.array([[3.76, 1.2], [5.25, 1.2], [1.58, 1.2]])
print('多组数据的预测结果为：', knn_final.predict(new_data))
print('多组数据的预测结果概率为：\n',knn_final.predict_proba(new_data))
'''
输出：
[[0.   1.   0.  ]
 [0.   0.25 0.75]
 [1.   0.   0.  ]]
每行总和为 1。以第二个虹膜为例，我们的模型预测虹膜为杂色的概率为 25%，维吉尼亚的概率为 75%。这与标签预测一致
'''

