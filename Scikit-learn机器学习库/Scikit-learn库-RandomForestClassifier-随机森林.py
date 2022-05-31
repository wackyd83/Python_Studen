'''随机森林是集成的一个示例，因为它使用多个机器学习模型来创建单个模型。'''

'''自举：
是数据点的随机样本，我们从原始数据集中随机选择替换数据点以创建相同大小的数据集。随机选择替换意味着我们可以多次选择相同的数据点。这意味着在自举样本中，原始数据集中的一些数据点会出现多次，而有些则根本不会出现。
'''

'''自助聚集Bootstrap Aggregation（或Bagging）：
是一种通过从基于自举样本构建的多个模型创建集合来减少单个模型中的方差的技术。为了进行预测，我们对10棵决策树中的每棵进行预测，然后每棵决策树都进行投票。得票最多的预测为最终预测。'''

'''去相关树：
将在构建每个决策树时对模型添加一些限制，以便树有更多的变化。我们称之为去相关树。'''

'''随机森林：
如果我们有 9 个特征，我们将在每个节点上考虑其中的 3 个（随机选择）。 如果我们打包这些决策树，我们会得到一个随机森林。'''

import pandas as pd
from sklearn.datasets import load_breast_cancer  # 导入数据源
from sklearn.ensemble import RandomForestClassifier  # 导入随机森林模型
from sklearn.model_selection import train_test_split  # 导入数据集随机划分训练集和测试集库

cancer_data = load_breast_cancer()
df = pd.DataFrame(cancer_data['data'], columns=cancer_data['feature_names'])
df['target'] = cancer_data['target']

X = df[cancer_data.feature_names].values
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=101)  # 设置随机种子，方便调试

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

first_row = X_test[0]
print("预测测试集首行数据prediction:", rf.predict([first_row]))
print("测试集中首行的标签true value:", y_test[0])
print("随机森林的准确性random forest accuracy:", rf.score(X_test, y_test))

'''与决策树进行比对'''
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
print("决策树的准确性decision tree accuracy:", dt.score(X_test, y_test))

'''随机森林由决策树组成，因此也具有决策树的预剪枝参数：max_depth、min_samples_leaf和max_leaf_nodes。对于随机森林，调整这些通常并不重要，因为过度拟合通常不是问题。 '''

'''
n_estimators：树的数量。
max_features：每次拆分时要考虑的特征数量。
'''

rf = RandomForestClassifier(max_features=5)  # max_features通常使用默认值，通常不需要更改，但可以设置为固定数字

rf = RandomForestClassifier(n_estimators=15)  # n_estimators默认值为10。

'''随机森林的一大优势便是它们很少需要进行太多调整。默认值对大多数数据集都适用。'''

'''网络搜索：使用网络搜索比较随机森林不同参数的性能。'''
from sklearn.model_selection import GridSearchCV  # 加载网络搜索模块，与决策树的网络搜索使用相同模块

param_grid = {
    'n_estimators': [10, 25, 50, 75, 100],
    'max_features': [1, 2, 3, 4, 5]
}  # 定义需要进行交叉验证的参数列表

rf = RandomForestClassifier(random_state=123)  # 定义随机种子，以便调试
gs = GridSearchCV(rf, param_grid, scoring='f1', cv=5)  # 网络搜索类实例化，scoring参数定义网络搜索结果的对比标准，cv定义交叉验证次数
gs.fit(X, y)
print("最佳参数best params:", gs.best_params_)  # 最佳参数存放在gs.best_params_
print("最好参数组合的得分best score:", gs.best_score_)

'''增加树的数量将提高性能。树越多，算法就越复杂。更复杂的算法使用起来更耗费资源。'''

'''使用肘图Elbow Graph找到最佳参数'''
n_estimators = list(range(1, 101))  # 使用网络搜索，尝试n_estimators 从 1 到 100 的所有值
param_grid = {
    'n_estimators': n_estimators,
}
rf = RandomForestClassifier()
gs = GridSearchCV(rf, param_grid, cv=5)
gs.fit(X, y)

scores=gs.cv_results_['mean_test_score']

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']  #显示中文标签
plt.plot(n_estimators, scores)
plt.xlabel("树的数量n_estimators")
plt.ylabel("准确性accuracy")
plt.xlim(0, 100)
plt.ylim(0.9, 1)
plt.savefig('随机森林肘图.png')
plt.show()

'''特征选择：
对于一棵树，可以计算出每个特征在树中减少了多少杂质。然后对于森林，可以平均每个特征的杂质减少。将此度量视为每个特征的重要性度量，然后我们可以根据特征重要性对特征进行排名和选择。
'''
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, random_state=101)
rf = RandomForestClassifier(n_estimators=10, random_state=111)
rf.fit(X_train, y_train)

ft_imp = pd.Series(rf.feature_importances_, index=cancer_data.feature_names).sort_values(ascending=False)
print(ft_imp.head(10))
'''输出：
worst radius            0.309701
mean concave points     0.183126
worst concave points    0.115641
mean perimeter          0.064119
mean radius             0.058742
worst concavity         0.050951
radius error            0.049103
mean texture            0.017197
worst area              0.016512
mean concavity          0.014696
dtype: float64
由上往下，数值越大的特征字段起到的作用越重要
'''

'''对比全特征字段与选定特征字段建模的得分'''
X = df[cancer_data.feature_names].values
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=101)

rf = RandomForestClassifier(n_estimators=10, random_state=111)
rf.fit(X_train, y_train)
print('全特征字段score:',rf.score(X_test, y_test))

worst_cols = [col for col in df.columns if 'worst' in col]
X_worst = df[worst_cols]
X_train, X_test, y_train, y_test = train_test_split(X_worst, y, random_state=101)
rf.fit(X_train, y_train)
print('worst特征score：',rf.score(X_test, y_test))

mean_cols = [col for col in df.columns if 'mean' in col]
X_mean = df[mean_cols]
X_train, X_test, y_train, y_test = train_test_split(X_mean, y, random_state=101)
rf.fit(X_train, y_train)
print('mean特征score：',rf.score(X_test, y_test))

'''随机森林优缺点：
表现：
优点：
最大优势在于它们通常无需任何调整即可正常运行。
还将在几乎每个数据集上表现得很好。

可解析性：
缺点：
随机森林尽管由决策树组成，但并不容易解释。

计算：
缺点：
构建随机森林可能会有点慢，尤其是当随机森林中有很多树时。
'''

from sklearn.datasets import make_circles  #使用make_circles函数生成数据集
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.model_selection import KFold

X, y = make_circles(noise=0.2, factor=0.5, random_state=1)

kf = KFold(n_splits=5, shuffle=True, random_state=1)
lr_scores = []
rf_scores = []
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    lr = LogisticRegression(solver='lbfgs')
    lr.fit(X_train, y_train)
    lr_scores.append(lr.score(X_test, y_test))
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(X_train, y_train)
    rf_scores.append(rf.score(X_test, y_test))
print("逻辑回归accuracy:", np.mean(lr_scores))
print("随机森林accuracy:", np.mean(rf_scores))
'''输出：
逻辑回归accuracy: 0.36
随机森林accuracy: 0.8400000000000001
可看到随机森林比较适合这个数据集
'''
'''在寻找新分类问题的基准时，通常的做法是从构建逻辑回归模型和随机森林模型开始，因为这两个模型都有可能在没有任何调整的情况下表现良好。这将为您提供要尝试击败的指标的值。通常几乎不可能比这些基准做得更好。'''
