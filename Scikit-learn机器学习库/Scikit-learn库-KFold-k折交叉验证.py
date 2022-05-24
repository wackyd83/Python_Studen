''' 创建多个训练和测试集的过程称为k折交叉验证。'''

'''对于小型数据集，为了衡量模型的指标值，将进行多次模型数据集划分评估，然后取平均值。跟住评估指标的平均值后，再使用所有数据进行模型构建。'''

from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

scores = []  #用以存放5次测试分数的空列表
kf = KFold(n_splits=5, shuffle=True)
for train_index, test_index in kf.split(X):  #train_index用以存储训练集的索引，test_index用以存储测试集的索引
    X_train, X_test = X[train_index], X[test_index]  #通过索引值把数据集X划分成训练集和测试集
    y_train, y_test = y[train_index], y[test_index]  #通过索引值把数据集y划分成训练集和测试集
    model = LogisticRegression()  #模型实例化
    model.fit(X_train, y_train)  #使用X_train,y_train训练集对模型进行拟合
    scores.append(model.score(X_test, y_test))
print(scores)  #分别把模型的准确度得分添加进列表scores
print(np.mean(scores))
final_model = LogisticRegression()  #模型实例化
final_model.fit(X, y)  #使用全体数据对模型进行拟合
