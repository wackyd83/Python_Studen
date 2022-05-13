import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_wine

'''聚类是一种无监督学习，它允许我们找到相似对象的组，这些对象彼此之间的相关性比与其他组中的对象更相关。业务用例的示例包括根据内容对文档、音乐和电影进行分组，或者根据购买行为查找客户群，作为推荐引擎的基础。'''

'''最流行的聚类算法之一是k-means。假设有 n 个数据点，算法工作如下： 步骤 1：初始化- 选择 k 个随机点作为聚类中心，称为质心步骤 2：聚类分配- 根据与每个质心的距离将每个数据点分配到其最近的质心, 并形成 k 个集群 第 3 步：质心更新- 对于每个新集群，通过取分配给集群的所有点的平均值来计算其质心 第 4 步：重复第2 步和第 3 步，直到没有任何集群分配发生变化，或者达到最大迭代次数'''

'''使用numpy计算2点间的距离'''
x1 = np.array([0, 1])
x2 = np.array([2, 0])
print(np.sqrt(((x1-x2)**2).sum()))
# 2.23606797749979
print(np.sqrt(5))
# 2.23606797749979

'''计算葡萄酒分类：每种葡萄酒有 13 个特征，如果我们可以将所有的葡萄酒分成 3 组，那么它将 13 维空间缩减为 3 维空间。'''
data = load_wine()
wine = pd.DataFrame(data.data, columns=data.feature_names)
print(wine.shape)
print(wine.columns)
print(wine.iloc[:,:3].describe())  #统计前3个字段的数据描述

'''pd.plotting.scatter_matrix()：显示沿对角线的直方图和对角线外每对属性的散点图'''
from pandas.plotting import scatter_matrix
scatter_matrix(wine.iloc[:,:])
plt.savefig("plot_win_scatter_matrix.png")
plt.show()
'''k的数量（子组）需要通过观察散点图进行主观判断（瞎猜）'''

'''对数据进行标准化处理： z = (x - mean) / std 其中 x 是原始数据，mean 和 std 是 x 的平均值和标准差，z 是缩放后的 x，使得它以 0 为中心并且具有单位标准差。使用 sklearn.preprocessing 的StandardScaler'''
from sklearn.preprocessing import StandardScaler  #对数据进行标准化的库
X = wine[['alcohol', 'total_phenols']]
scale = StandardScaler()  #实例化缩放器
scale.fit(X)  #计算平均值和标准差，稍后用于缩放
print(scale.mean_)  #输出：[13.00061798  2.29511236]
print(scale.scale_)  #输出：[0.80954291 0.62409056]


'''健全性检查，看看每个特征是否以 0 为中心并且标准为 1'''
X_scaled = scale.transform(X)
print(X_scaled.mean(axis=0))
print(X_scaled.std(axis=0))

'''为了进行建模，我们遵循实例化/拟合/预测工作流程。'''
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)  #实例化模型,n_clusters=n,n为分类的数量
kmeans.fit(X_scaled)  #拟合模型
y_pred = kmeans.predict(X_scaled)  #作出预测
print('分类明细：\n',y_pred)  #预测每个元素的分类
print('质心坐标：\n',kmeans.cluster_centers_)  #标示质心坐标

'''可视化散点图及质心坐标位置'''
import matplotlib.pyplot as plt
'''绘制缩放数据'''
plt.scatter(X_scaled[:,0],X_scaled[:,1],c= y_pred)
'''设置质心位置及显示样式'''
plt.scatter(kmeans.cluster_centers_[:, 0],kmeans.cluster_centers_[:, 1],marker="*",s = 250,c = [0,1,2],edgecolors='k')  #c需根据n_clusters=n的n值设置
'''设置散点图的xy轴名称、标题等可视化图表信息'''
plt.xlabel('alcohol'); plt.ylabel('total phenols')
plt.title('k-means (k=3)')
plt.savefig("plot_kmeans.cluster_centers_.png")
plt.show()

'''往模型中放入一组测试数据，测试这组数据的分类'''
X_new = np.array([[13, 2.5]])
X_new_scaled = scale.transform(X_new)
print(kmeans.predict(X_new_scaled))  #打印这组测试数据的分类

'''
由于集群的顺序可能会发生变化，因此每次运行代码时都会得到略微不同的结果。k-means 的一个主要缺点是质心的随机初始猜测可能导致不良聚类，k-means++ 算法通过在继续使用标准 k-means 算法之前指定初始化质心的过程来解决这个障碍。
'''
'''紧密度可以测量为从数据点到其最近质心的距离或惯性的平方和。'''

'''聚类后的失真'''
kmeans = KMeans(n_clusters=2)
kmeans.fit(X_scaled)
print('n_clusters=2的失真：',kmeans.inertia_)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_scaled)
print('n_clusters=3的失真：',kmeans.inertia_)
kmeans = KMeans(n_clusters=4)
kmeans.fit(X_scaled)
print('n_clusters=4的失真：',kmeans.inertia_)

'''绘制聚类数量不同的失真折线图，计算分类数量范围的失真。失真随着聚类数量的增加而减少。最佳 k 应该是失真不再快速减小的地方。'''
inertia = []
for i in np.arange(1, 11):
    km = KMeans(
        n_clusters=i
    )
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.plot(np.arange(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.savefig("plot_Inertia.png")
plt.show()

'''使用更多字段来进行分类，并绘制失真数值折线图，以便找到最优k值'''
X = wine  #使用所有字段参与聚类
scale = StandardScaler()  #模型实例化
scale.fit(X)  #模型拟合
X_scaled = scale.transform(X)  #预测
'''通过失真折线图寻找最优k值'''
inertia = []
for i in np.arange(1, 11):
    km = KMeans(
        n_clusters=i
        )
    km.fit(X_scaled)
    inertia.append(km.inertia_)
plt.plot(np.arange(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title("all features")
plt.savefig("plot_all_Inertia.png")
plt.show()

'''对比后可观察到k=3时，失真不再迅速减少，因此k取值为3'''
k_opt = 3
kmeans = KMeans(k_opt)
kmeans.fit(X_scaled)
y_pred = kmeans.predict(X_scaled)
print(y_pred)

'''很难确定具有 2 个特征的模型在对葡萄酒进行分组时比具有所有 13 个特征的模型更准确。应该选择哪种模型（），通常由外部信息决定。例如，营销部门想知道是否需要针对特定大陆的策略来销售这些葡萄酒。我们现在可以访问消费者的人口统计信息，从模型 A 中确定的三个集群分别比模型 B 更好地对应于欧洲、亚洲和北美的客户；那么模型 A 是赢家。'''