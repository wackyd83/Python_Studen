from sklearn.linear_model import LogisticRegression
import pandas as pd

'''逻辑回归是一种在数学上找到最佳线的方法'''

'''可能性：是我们如何评分和比较最佳拟合线的可能选择。
可能性计算：如果预测与事实相符，得分为概率p。如果预测与实时相反，得分为1-概率p。'''

'''标准做法是将特征的2d数组称为X，将目标值的1d数组称为y。'''
df = pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values
print(X)
print(y)

'''构建特征矩阵和目标数组：X（作为 2d numpy 数组的特征）和 y（作为 1d numpy 数组的目标）'''
X1 = df[['Fare', 'Age']].values
y1 = df['Survived'].values

'''模型实例化'''
model1 = LogisticRegression()

'''拟合模型，并显示系数和截距'''
model1.fit(X1, y1)
print('model1系数：', model1.coef_)
print('model1截距：', model1.intercept_)

'''使用更多特征进行模型拟合'''
X2 = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y2 = y1
model2 = LogisticRegression()
model2.fit(X2, y2)
print('model2预测1~5条数据结果：', model2.predict(X[:5]))
print('数据记录中1~5条的结果：', y[:5])
print('model2系数：', model2.coef_)
print('model2截距：', model2.intercept_)

'''model.score()：模型准确度得分'''
y_pred = model2.predict(X)
print('预测准确的数量：', (y == y_pred).sum())
print('样本总数：', y.shape[0])
print((y == y_pred).sum() / y.shape[0])  # 输出0.8049605411499436，说明该模型的准确度为80%
print('model.score()计算模型准确度得分：', model2.score(X, y))  # 使用model.score()直接得出模型准确度得分

'''导入乳腺癌数据集'''
from sklearn.datasets import load_breast_cancer

cancer_data=load_breast_cancer()
print('数据集规模：\n',cancer_data['data'].shape)  #查看数据集的描述
print('字段名：\n',cancer_data['feature_names'])  #列名单独存放在feature_names字段

'''使用数据集和字段名创建dataFrame对象，df对象包含30个字段的特征矩阵和1个字段的目标数组'''
df=pd.DataFrame(cancer_data['data'],columns=cancer_data['feature_names'])
df['target']=cancer_data['target']

X=df[cancer_data.feature_names].values
y=df['target'].values

model3=LogisticRegression(solver='liblinear')  #模型耗时太久，收到收敛警告，需要切换不同的求解器'liblinear'
model3.fit(X,y)

print("预测数据集第一行的结果：", model3.predict([X[0]]))
print('模型的准确性得分为:',model3.score(X,y))  #输出：0.9595782073813708，模型的准确性得分为96%

