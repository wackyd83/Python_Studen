import pandas as pd
from sklearn.linear_model import LogisticRegression

'''过度拟合：过度拟合是指我们在模型已经看到的数据上表现良好，但在新数据上表现不佳。我们数据集中的特征越多，我们就越容易过度拟合。'''

df=pd.read_csv('titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y=df['Survived'].values

'''导入sklearn的train_test_split函数，以便自动随机划分训练集和测试集'''
from sklearn.model_selection import train_test_split
'''一个标准的细分是将我们的数据的 70-80% 放在训练集中，将 20-30% 放在测试集中。'''
X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.9)  #设置训练集的比例为90%。train_size默认值为0.75。
model=LogisticRegression()
model.fit(X,y)

'''导入分数评估函数accuracy_score, precision_score, recall_score, f1_score'''
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
y_pred = model.predict(X_test)  #使用测试集评估测试模型分数
print("准确性accuracy:", accuracy_score(y_test, y_pred))
print("精确度precision:", precision_score(y_test, y_pred))
print("召回率recall:", recall_score(y_test, y_pred))
print("f1分数f1 score:", f1_score(y_test, y_pred))  #使用测试集评估测试模型分数
'''使用train_test_split进行数据集随机分配，将导致每次生成测试集和训练集不同导致最后得分不同'''
X = [[1, 1], [2, 2], [3, 3], [4, 4]]
y = [0, 0, 1, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y)
print('X_train', X_train)
print('X_test', X_test)
'''使用random_state=1参数可以使每次运行train_test_split语句得出的训练集和测试集一致'''
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=1)  #随机状态也称为种子
print('X_train', X_train)
print('X_test', X_test)