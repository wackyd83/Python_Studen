'''一个好的分割特征:
进行数据分割后，分割两测的预测目标分类数量差异非常明显（呈现多倍关系）。'''

'''基尼杂质：
基尼杂质是衡量一组纯度的指标。它将是一个介于 0 和 0.5 之间的值，其中 0.5 是完全不纯的（50% 幸存，50% 未幸存），0 是完全纯的（100% 在同一类中）。 
计算公式：基尼杂质gini=2 * p * (1-p)
p 是幸存乘客的百分比。因此 (1-p) 是没有幸存的乘客的百分比。
'''

'''熵:
熵是纯度的另一种度量。它将是一个介于 0 和 1 之间的值，其中 1 完全不纯（50% 幸存，50% 未幸存），0 完全纯（100% 相同类别）。 
计算公式：熵entropy=- [p * log2p + (1-p) * log2(1-p)
p 是幸存乘客的百分比。因此 (1-p) 是没有幸存的乘客的百分比。
'''

'''使用基尼杂质或者熵计算节点分割得分时，可以交叉校验，以确保所使用的分割节点更好'''

'''信息增益：

计算公式：Information Gain=H(S)-|A|/|S|*H(A)-|B|/|S|*H(B)
H 是我们的杂质度量（基尼杂质或熵）
S 是原始数据集
A 和 B 是我们将数据集 S 分成的两组。'''

import pandas as pd
from sklearn.model_selection import train_test_split  # 导入数据集自动划分训练集和测试集模块
from sklearn.tree import DecisionTreeClassifier  # 导入sklearn决策树模块

df = pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=22)  # 使用train_test_split函数把数据集拆分为训练集和测试集，随机种子为22

model = DecisionTreeClassifier()  # 模型实例化

model.fit(X_train, y_train)  # 使用训练集对模型进行拟合

print(model.predict([[3, True, 22, 1, 0, 7.25]]))  # 使用模型进行预测

'''对于同一个数据集，分别使用逻辑回归和决策树模型进行K折交叉验证，对比2个模型的准确度、精确度和召回率得分平均值。'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.metrics import precision_score, recall_score, accuracy_score
import numpy as np

df = pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

kf = KFold(n_splits=5, shuffle=True, random_state=10)
dt_accuracy_scores = []
dt_precision_scores = []
dt_recall_scores = []
lr_accuracy_scores = []
lr_precision_scores = []
lr_recall_scores = []
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    dt_accuracy_scores.append(dt.score(X_test, y_test))
    dt_y_pred = dt.predict(X_test)
    dt_precision_scores.append(precision_score(y_test, dt_y_pred))
    dt_recall_scores.append(recall_score(y_test, dt_y_pred))
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    lr_accuracy_scores.append(lr.score(X_test, y_test))
    lr_y_pred = lr.predict(X_test)
    lr_precision_scores.append(precision_score(y_test, lr_y_pred))
    lr_recall_scores.append(recall_score(y_test, lr_y_pred))
print("决策树Decision Tree")
print("  准确度accuracy:", np.mean(dt_accuracy_scores))
print("  精确度precision:", np.mean(dt_precision_scores))
print("  召回率recall:", np.mean(dt_recall_scores))
print("逻辑回归Logistic Regression")
print("  准确度accuracy:", np.mean(lr_accuracy_scores))
print("  精确度precision:", np.mean(lr_precision_scores))
print("  召回率recall:", np.mean(lr_recall_scores))
'''输出：
决策树Decision Tree
  准确度accuracy: 0.7756173427283691
  精确度precision: 0.7048701882912409
  召回率recall: 0.7204562594268478
逻辑回归Logistic Regression
  准确度accuracy: 0.7970354853043865
  精确度precision: 0.7618898922983288
  召回率recall: 0.6900529617441382
'''

'''scikit-learn 的决策树算法中的默认杂质标准是基尼杂质。但是，它们也实现了熵，您可以在创建DecisionTreeClassifier 对象时选择要使用的熵(criterion='entropy')。'''
dt = DecisionTreeClassifier(criterion='entropy')

'''对比使用基尼杂质和熵性能差异的决策树模型'''
import time

kf = KFold(n_splits=5, shuffle=True)
for criterion in ['gini', 'entropy']:
    begin = time.time()
    print("Decision Tree - {}".format(criterion))
    accuracy = []
    precision = []
    recall = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        dt = DecisionTreeClassifier(criterion=criterion)
        dt.fit(X_train, y_train)
        y_pred = dt.predict(X_test)
        accuracy.append(accuracy_score(y_test, y_pred))
        precision.append(precision_score(y_test, y_pred))
        recall.append(recall_score(y_test, y_pred))
    print("accuracy:", np.mean(accuracy))
    print("precision:", np.mean(precision))
    print("recall:", np.mean(recall))
    print('耗时：', time.time() - begin)
    print()
'''输出：
Decision Tree - gini
accuracy: 0.7642798197168793
precision: 0.698584293513459
recall: 0.6844102983501879
0.011999368667602539

Decision Tree - entropy
accuracy: 0.7835840792230051
precision: 0.7208576875919676
recall: 0.7185279635586921
0.012991189956665039
结论是基尼杂质比熵的计算速度基本相同。'''

'''决策树可视化：
使用sklearn的export_graphviz函数，并且需要安装graphviz模块。以下为根据'Pclass', 'male'生成的决策树图'''
from sklearn.tree import export_graphviz
import graphviz

feature_names = ['Pclass', 'male']
X = df[feature_names].values
y = df['Survived'].values

dt = DecisionTreeClassifier()
dt.fit(X, y)

dot_file = export_graphviz(dt, feature_names=feature_names)
graph = graphviz.Source(dot_file)
graph.render(filename='生成的决策树模型树', format='png', cleanup=True)

'''决策树非常容易过度拟合。因此需要剪枝。剪枝有2种方法：
预剪枝：有关于何时停止建造树的规则，所以我们在树太大之前停止建造。
后剪枝：构建整棵树，然后我们检查树，并决定删除哪片叶子，使树更小。'''

'''预剪枝：
最大深度：仅将树长到一定深度或树的高度。如果最大深度为 3，则每个数据点最多有 3 个拆分。
叶大小：如果该节点的样本数低于阈值，则不要拆分该节点。
叶节点数：限制树中允许的叶节点总数。
'''

'''欠拟合：
如果您将最大深度设置得太小，您将没有太多的树，也没有任何预测能力。同样，如果叶子大小太大，或者叶子节点的数量太小，你就会得到一个欠拟合模型。
'''

'''预剪枝参数：
max_depth：限制深度，限制树在根节点和叶节点之间可以具有的步数。
min_samples_leaf：避免具有少量数据点的叶节点，告诉模型如果叶节点中的数据点数量低于阈值，则提前停止构建树。
max_leaf_nodes：限制叶节点的数量，设置树中叶节点的数量上限。
'''
dt = DecisionTreeClassifier(max_depth=3, min_samples_leaf=2, max_leaf_nodes=10)

'''使用交叉验证决定预剪枝的参数。
GridSearchCV 有四个我们将使用的参数：
1. 模型（在本例中为 DecisionTreeClassifier）
2. 参数网格：参数名称和所有可能值的字典
3. 使用什么度量（默认为准确度）
4. k-fold 交叉验证 的折叠数让我们创建参数网格变量。我们将列出我们想要尝试的每个参数的所有可能值。
'''
from sklearn.model_selection import GridSearchCV  # 导入sklearn内置的网络搜索类

X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

param_grid = {
    'max_depth': [5, 15, 25],
    'min_samples_leaf': [1, 3],
    'max_leaf_nodes': [10, 20, 35, 50]}  # 定义需要进行交叉验证的各项备选参数

dt = DecisionTreeClassifier()
gs = GridSearchCV(dt, param_grid, scoring='f1', cv=5)

gs.fit(X, y)
print("最好的参数是best params:", gs.best_params_)
print("最好参数组合的得分best score:", gs.best_score_)
'''多次执行网络搜索时，可能会出现不同结果，这是因为有几个性能相近的模型。我们选择更简单的模型即可。'''

'''决策树的优缺点：
计算：
缺点：
构建决策树的计算成本非常高。
优点：
使用决策树进行预测的计算成本非常低。
PS. 我们更关心预测的计算时间而不是训练。预测通常需要在用户等待结果时实时发生。

表现：
缺点：
容易过度拟合。
优点：
根据数据表现得很好。
PS. 决策树通常需要与其他模型在没有调整的情况下执行相同的工作。

可解析性：
优点：
很容易对预测进行解释。
PS. 可解释性是决策树的最大优势。
'''