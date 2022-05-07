import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''导入sklearn包的波士顿房产数据集，回归问题常用。'''
from sklearn.datasets import load_boston

'''导入线性回归模型：LinearRegression'''
from sklearn.linear_model import LinearRegression

boston_dataset = load_boston()

boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)

boston['MEDV'] = boston_dataset.target

'''
输出：Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT', 'MEDV'],
      dtype='object')
CRIM：城镇人均犯罪率                                    ------【城镇人均犯罪率】
ZN：占地面积超过25,000平方英尺的住宅用地比例。              ------【住宅用地所占比例】
INDUS：每个城镇非零售业务的比例。                         ------【城镇中非商业用地占比例】
CHAS：Charles River虚拟变量（如果是河道，则为1;否则为0     ------【查尔斯河虚拟变量，用于回归分析】
NOX：一氧化氮浓度（每千万份）                             ------【环保指标】
RM：每间住宅的平均房间数                                 ------【每栋住宅房间数】
AGE：1940年以前建造的自住单位比例                         ------【1940年以前建造的自住单位比例 】
DIS -波士顿的五个就业中心加权距离                         ------【与波士顿的五个就业中心加权距离】
RAD：径向高速公路的可达性指数                             ------【距离高速公路的便利指数】
TAX：每10,000美元的全额物业税率                          ------【每一万美元的不动产税率】
PTRATIO：城镇的学生与教师比例                            ------【城镇中教师学生比例】
B：1000（Bk：0.63）^ 2其中Bk是城镇黑人的比例              ------【城镇中黑人比例】
LSTAT：人口状况下降％                                   ------【房东属于低等收入阶层比例】
MEDV：自有住房的中位数报价, 单位1000美元                   ------【自住房屋房价中位数】
'''
print(boston['RM'].describe())

'''计算元素间的相关性，通过分析相关性，可找出哪些字段间的关联性最密切（最接近1为相关性最大），就把这2个字段作为'''
corr_matrix = boston.corr().round(2)
print(corr_matrix)

'''输出散点图'''
boston['MEDV'] = boston_dataset.target
boston.plot(kind='scatter',
            x='LSTAT',
            y='MEDV',
            figsize=(8, 6))
plt.savefig("plot1.png")

'''在 scikit-learn 中，模型需要一个二维特征矩阵（X、2darray 或 pandas DataFrame）和一个一维目标数组（Y）。 '''
'''使用RM数据生成DataFrame数组'''
X = boston[['RM']]
'''使用RM数据生成Serice数组'''
Y = boston['MEDV']

'''模型实例化'''
model = LinearRegression()

'''区分数据集，把70%数据作为训练集，30%数据作为测试集'''
'''在 scikit-learn 的 model_selection 模块中使用train_test_split 函数将数据分成两个随机子集。设置 random_state 以便结果可重现。'''
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
# print('Y_test:\n',Y_test)

'''拟合模型，拟合等于训练'''
model.fit(X_train, Y_train)

'''经过训练后，输出截距intercept和斜率slope'''
print(model.intercept_.round(2))
print(model.coef_.round(2))

'''预测测试数据，需把要预测的数据转化为一维数组（Series）'''
new_RM = np.array([6.5]).reshape(-1, 1)
'''.predict(arg)：预测数据，参数arg必须为一维数组（Series或2d array）'''
print(model.predict(new_RM))
'''.predict()等同于model.intercept_+model.coef_*x。x：须预测的数据，套用公司y=截距+斜率*x'''
print(model.intercept_ + model.coef_ * 6.5)

'''使用测试集验证预测的数据'''
y_test_predicted = model.predict(X_test)
'''绘制散点图与预测参数折线图的对比'''
plt.scatter(X_test, Y_test, label='testing data')
plt.plot(X_test, y_test_predicted, label='prediction', linewidth=3)
plt.xlabel('RM')
plt.xlim((4, 9))
plt.ylabel('MEDV')
plt.legend(loc='upper left')
plt.savefig("y_test_predicted.png")
plt.show()

'''计算残差（误差）：是目标的观察值与预测值之间的差异。绘制残差的分布'''
residuals = Y_test - y_test_predicted
plt.scatter(X_test, residuals)  # 绘制残差值折线图
plt.hlines(y=0, xmin=X_test.min(), xmax=X_test.max(), linestyle='--')  # 在y=0绘制参考线
plt.xlim((4, 9))  # 设置x轴数值范围
plt.xlabel('RM')
plt.ylabel('residuals')
plt.savefig("plot.png")
plt.show()

'''误差均值'''
print('误差均值residuals.mean():', residuals.mean())

'''均方误差mean squared error (MSE)'''
print('均方误差(residuals**2).mean():', (residuals ** 2).mean())
'''使用 scikit-learn 指标模块下的 mean_squared_error() 方法输出均方误差'''
from sklearn.metrics import mean_squared_error

print('均方误差mean_squared_error(Y_test, y_test_predicted):', mean_squared_error(Y_test, y_test_predicted))
'''一般来说，MSE越小越好，但没有绝对的好坏阈值。我们可以根据因变量来定义它，即测试集中的MEDV。Y_test 范围从 6.3 到 50，方差为 92.26。与总方差相比，36.52 的 MSE 还不错。'''

'''使用model.score()计算R平方（R-squared）。R平方：它是模型解释的总变异的比例。在这里，我们的模型解释了测试数据中大约 60% 的可变性。'''
print('R平方（R-squared）model.score(X_test, Y_test)：', model.score(X_test, Y_test))
'''R平方的另一种计算方法'''
print('R平方（R-squared）1-(residuals**2).sum()/((Y_test-Y_test.mean())**2).sum()：',
      1 - (residuals ** 2).sum() / ((Y_test - Y_test.mean()) ** 2).sum())
'''一个完美的模型解释了数据中的所有变化。注意 R 平方介于 0 和 100% 之间：0% 表示模型没有解释响应数据在其平均值附近的任何变异性，而 100% 表示模型解释了所有变异。'''

'''多元线性回归模型multivariate linear regression model。公式：y=b0+b1*x1+b2*x2'''
X2 = boston[['RM', 'LSTAT']]
Y = boston['MEDV']
X2_train, X2_test, Y_train, Y_test = train_test_split(X2, Y, test_size=0.3, random_state=1)
model2 = LinearRegression()
model2.fit(X2_train, Y_train)
y_test_predicted2 = model2.predict(X2_test)
print('多元线性回归模型的MSE：',mean_squared_error(Y_test, y_test_predicted2).round(2))