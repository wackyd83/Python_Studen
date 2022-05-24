import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y=df['Survived'].values
model=LogisticRegression()
model.fit(X,y)
y_pred=model.predict(X)

'''导入计算准确度（Accuracy）、精确度（Precision）、召回率（灵敏度）（Recall ）和 F1 分数（F1 Score）的函数'''
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

print('准确度（Accuracy）：',accuracy_score(y,y_pred),model.score(X,y))  #accuracy_score(y,y_pred)与model.score(X,y)等值
print('精确度（Precision）：',precision_score(y,y_pred))
print('召回率（Recall ）：',recall_score(y,y_pred))
print('F1 分数（F1 Score）：',f1_score(y,y_pred))

'''精度(precision)是衡量模型对其积极预测的精确程度的衡量标准。
A true positive (TP) ：预测阳性，实际也是阳性，预测正确.
A true negative (TN) ：预测阴性，实际也是阴性，预测正确.
A false positive (FP)：预测阳性，实际是阴性，预测错误.
A false negative (FN)：预测阴性，实际是阳性，预测错误.
精度(precision)计算公式：TP / (TP + FP)'''

'''召回率（Recall）：召回率是模型正确预测的正例百分比。是衡量模型可以召回多少积极案例的指标。
精度(precision)计算公式：TP / (TP + FN)'''
'''敏感性（sensitivity）是召回的另一个术语，即真实阳性率。'''

'''一句话总结：提高精度：有杀错冇放过；提高召回率：水至清则无鱼。'''

'''F1分数（F1 Score）：是准确率和召回率值的调和平均值。
F1分数公式：2 * precision * Recall / （precision + Recall）'''

'''sklearn自带的混沌矩阵函数,Scikit-learn 反转混淆矩阵以首先显示负数'''
from sklearn.metrics import confusion_matrix
print('混沌函数输出的4个象限分别为：\n',confusion_matrix(y,y_pred))

'''特异性（specificity ）是真正的负率。
计算公式如下：TN / (TN + FP)'''

'''sklearn没有专门的敏感性和特异性函数，使用时需自定义。'''
'''precision_recall_fscore_support：第二个数组是召回，所以我们可以忽略其他三个数组。有两个值。第一个是负类的召回，第二个是正类的召回。第二个值是标准召回率或灵敏度值，您可以看到该值与我们上面得到的匹配。第一个值是特异性。'''
from sklearn.metrics import precision_recall_fscore_support
'''敏感性与召回率相同，因此可以直接使用召回率函数recall_score()'''
from sklearn.metrics import recall_score
sensitivity_score = recall_score  #敏感性与召回率相同，因此可以直接使用召回率函数recall_score()

'''自定义函数specificity_score()：接收precision_recall_fscore_support返回的特异性结果'''
def specificity_score(y_true, y_pred):
    p, r, f, s = precision_recall_fscore_support(y_true, y_pred)
    return r[0]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("敏感性sensitivity:", sensitivity_score(y_test, y_pred))
print("特异性specificity:", specificity_score(y_test, y_pred))

y_pred75 = model.predict_proba(X_test)[:, 1] > 0.75
print("精度precision 75:", precision_score(y_test, y_pred75))
print("召回率recall 75:", recall_score(y_test, y_pred75))
