'''同一份数据集的情况下，评估使用哪些字段的模型表现最好'''


'''在 scikit-learn 中构建这两个模型。然后我们将使用 k 折交叉验证来计算两个模型的准确率、精度、召回率和 F1 分数'''

from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'

kf = KFold(n_splits=5, shuffle=True)  # 实例化KFold模型
X1 = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values  #使用所有字段构建特征数据集
X2 = df[['Pclass', 'male', 'Age']].values  #只使用'Pclass', 'male', 'Age'3个字段构建特征数据集
X3 = df[['Fare', 'Age']].values  #只使用'Fare', 'Age'构建特征数据集
y = df['Survived'].values  #构建标签数据集


def score_model(X, y, kf):  #自定义一个函数，用以放入特征集和标签集
    accuracy_scores = []
    precision_scores = []
    recall_scores = []
    f1_scores = []  #定义4个空列表，用以存储4个结果分数
    for train_index, test_index in kf.split(X):  #使用kf.split函数，对放入的数据集进行k折交叉验证
        X_train, X_test = X[train_index], X[test_index]  #通过索引值把数据集X划分成训练集和测试集
        y_train, y_test = y[train_index], y[test_index]  #通过索引值把数据集y划分成训练集和测试集
        model = LogisticRegression()  #模型实例化
        model.fit(X_train, y_train)  #使用X_train,y_train训练集对模型进行拟合
        y_pred = model.predict(X_test)  #测试集的预测结果列表
        accuracy_scores.append(accuracy_score(y_test, y_pred))  #对预测结果进行准确度accuracy评分
        precision_scores.append(precision_score(y_test, y_pred))  #对预测结果进行精确度precision评分
        recall_scores.append(recall_score(y_test, y_pred))  #对预测结果进行召回率recall评分
        f1_scores.append(f1_score(y_test, y_pred))  #对预测结果进行f1分数f1 score评分
    print('准确度accuracy:', np.mean(accuracy_scores))
    print("精确度precision:", np.mean(precision_scores))
    print("召回率recall:", np.mean(recall_scores))
    print("f1分数f1 score:", np.mean(f1_scores))


print("Logistic Regression with all features")
score_model(X1, y, kf)
print()
print("Logistic Regression with Pclass, Sex & Age features")
score_model(X2, y, kf)
print()
print("Logistic Regression with Fare & Age features")
score_model(X3, y, kf)

'''对比3个模型：
模型一与模型一得分基本相同，符合预期。模型三得分较低，因此选择特征较少但得分较高的模型二，以便获得更好的性能与得分平衡。'''

final_model = LogisticRegression()
final_model.fit(X1, y)

print(final_model.predict([[3, False, 25, 0, 1, 2]]))
