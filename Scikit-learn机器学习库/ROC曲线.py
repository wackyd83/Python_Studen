

'''ROC曲线是特异性和敏感性的关系图。roc_curve 函数：该函数从我们的模型中获取真实的目标值和预测概率'''
from matplotlib import pyplot as plt

'''
从 ROC 曲线中选取模型:
如果我们处于这样一种情况，即我们所有的正面预测都是正确的，而不是我们抓住所有的正面案例（这意味着我们正确地预测了大多数负面案例） ，我们应该选择特异性更高的模型（模型A）。 如果我们处于一种重要的情况下，我们必须尽可能多地捕获正例，我们应该选择具有更高灵敏度的模型（模型 C）。 如果我们想要在敏感性和特异性之间取得平衡，我们应该选择模型 B。'''

'''
曲线下面积:
 为了对此进行经验测量，我们计算曲线下面积，也称为 AUC。这是 ROC 曲线下的面积。它是一个介于 0 和 1 之间的值，越高越好。 由于 ROC 是具有不同阈值的所有不同逻辑回归模型的图，因此 AUC 不能衡量单个模型的性能。它可以大致了解 Logistic 回归模型的执行情况。要获得单个模型，您仍然需要找到问题的最佳阈值。
这个指标告诉我们逻辑回归模型在我们的数据上的总体表现如何。由于 ROC 曲线显示了多个模型的性能，AUC 并不是衡量单个模型的性能。
'''
'''比较Titanic数据集中，使用所有字段计算的模型和只使用2个字段的模型进行AUC分数比较。这个指标告诉我们逻辑回归模型在我们的数据上的总体表现如何。由于 ROC 曲线显示了多个模型的性能，AUC 并不是衡量单个模型的性能。'''
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve

df = pd.read_csv('titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y)

model1 = LogisticRegression()
model1.fit(X_train, y_train)
y_pred_proba1 = model1.predict_proba(X_test)
print("model1 AUC score:", roc_auc_score(y_test, y_pred_proba1[:, 1]))
fpr1, tpr1, thresholds1 = roc_curve(y_test, y_pred_proba1[:,1])

model2 = LogisticRegression()
model2.fit(X_train[:, 0:2], y_train)
y_pred_proba2 = model2.predict_proba(X_test[:, 0:2])
print("model2 AUC score:", roc_auc_score(y_test, y_pred_proba2[:, 1]))
fpr2, tpr2, thresholds2 = roc_curve(y_test, y_pred_proba2[:,1])

plt.plot(fpr1, tpr1,label = "model1")
plt.plot(fpr2, tpr2,label = "model2")
plt.plot([0, 1], [0, 1], linestyle='--',label = "std_line")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('1 - specificity')
plt.ylabel('sensitivity')
plt.legend()
plt.savefig('ROC_Curve.png')
plt.show()