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
from sklearn.model_selection import train_test_split  #导入数据集自动划分训练集和测试集模块
from sklearn.tree import DecisionTreeClassifier  #导入sklearn决策树模块

df=pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=22)  #使用train_test_split函数把数据集拆分为训练集和测试集，随机种子为22

model=DecisionTreeClassifier()  #模型实例化

model.fit(X_train,y_train)  #使用训练集对模型进行拟合

print(model.predict([[3, True, 22, 1, 0, 7.25]]))  #使用模型进行预测

'''对于同一个数据集，分别使用逻辑回归和决策树模型进行K折交叉验证，对比2个模型的准确度、精确度和召回率得分平均值。'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.metrics import precision_score, recall_score,accuracy_score
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
    begin=time.time()
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
    print('耗时：',time.time()-begin)
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
使用sklearn的export_graphviz函数'''