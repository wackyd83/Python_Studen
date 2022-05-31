import numpy as np

'''神经网络是非常流行且功能强大的机器学习模型。神经网络通常可以很好地工作，而您无需使用领域知识来进行任何特征工程。'''

'''单个神经元Neuron计算公式：
y = f * (w1 * x1 + w2 * x2 + b)
w1 和 w2 称为权重，将 b 称为偏差。将这些值 (w1, w2, b) 称为参数。函数 f 是激活函数。常用的激活函数是sigmoid函数。激活函数将输入数据压缩到一个固定的范围内（通常在 0 到 1 之间）'''

'''常用激活函数：
sigmoid：将输入数据压缩到一个固定的范围内（通常在 0 到 1 之间）。
tanh：形式与 sigmoid 相似，但范围从 -1 到 1 而不是 0 到 1。
ReLU：代表 Rectified Linear Unit。它是正数的恒等函数并将负数发送到 0。
这些激活函数中的任何一个都可以正常工作。使用哪一个将取决于我们数据的具体情况。在实践中，我们通过比较不同神经网络的性能来确定使用哪一个。
'''

'''多层感知器：
多层感知器总是有一个输入层，每个输入都有一个神经元（或节点）。有两个输入，因此有两个输入节点。它将有一个输出层，每个输出都有一个节点。上面有单个输出值的 1 个输出节点。它可以有任意数量的隐藏层，每个隐藏层可以有任意数量的节点。
 输入层中的节点采用单个输入值并将其向前传递。隐藏层和输出层中的节点可以接受多个输入，但它们总是产生一个输出。有时节点需要将它们的输出传递给多个节点。
 单层感知器是一个没有任何隐藏层的神经网络。这些很少使用。大多数神经网络都是多层感知器，通常有一个或两个隐藏层。
'''

'''预测多个目标值：
如果我们试图预测图像是鸟、猫还是狗，我们将有三个输出节点。第一个（y1）测量图像是否为鸟，第二个（y2）测量图像是否为猫，第三个（y3）测量图像是否为狗。模型选择具有最高值的输出。神经网络输出 y1=0.3、y2=0.2 和 y3=0.5，然后模型将确定图像中有狗 (y3)。
'''

'''损失函数：
我们将使用交叉熵cross entropy作为我们的损失函数。当我们训练神经网络时，我们是在优化一个损失函数。交叉熵越大，模型越好。
交叉熵：
if y = 1:
    p
elif y = 0:
    1-p
y是预测结果，p是预测值
'''

'''反向传播：
神经网络从输出节点向后工作，迭代更新节点的系数。这种通过神经网络向后移动的过程称为反向传播或反向传播。
我们初始化所有系数值并迭代地更改值，以便在每次迭代中我们看到损失函数的改进。最终我们无法再改进损失函数，然后我们发现了我们的最优模型。
在我们创建神经网络之前，我们固定节点数和层数。然后我们使用反向传播迭代更新所有的系数值，直到我们收敛到一个最优的神经网络上。'''

'''使用make_classification()函数生成数据集用于实验
• n_samples: 数据中元素个数
• n_features: 特征的数量
• n_informative: 有用特征数量
• n_redundant: 冗余特征数量
• random_state: 随机状态（保持每次随机结果一致）
'''
'''使用更多的人工数据集，可以看看make_circles和make_moons。'''

from sklearn.datasets import make_classification  # 导入make_classification以便生成数据集

X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=3)  # 生成一个2个特征，0个冗余特征，2个有效特征，并且随机状态为3的数据集
print(X)
print(y)

'''绘制数据，以便直观观察'''
from matplotlib import pyplot as plt

plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], s=100, edgecolors='k')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], s=100, edgecolors='k', marker='^')
plt.show()

'''MLP分类器'''
from sklearn.model_selection import train_test_split  # 导入数据集随机拆分成训练集和测试集
from sklearn.neural_network import MLPClassifier  # 导入MLP分类器类

X, y = make_classification(n_features=2, n_redundant=0, n_informative=2, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)
mlp = MLPClassifier(max_iter=1000)  # max_iter=1000，表示迭代次数上限为1000
mlp.fit(X_train, y_train)
print("准确性accuracy:", mlp.score(X_test, y_test))

'''配置隐藏层和每层节点数：默认的 MLPClassifier 将具有 100 个节点的单个隐藏层。'''
mlp = MLPClassifier(max_iter=1000, hidden_layer_sizes=(100, 50))  # 创建2个隐藏层，分别为100个节点和50个节点的MLP分类器

'''
max_iter：这是迭代次数。一般来说，你拥有的数据越多，你需要收敛的迭代就越少。如果该值太大，运行代码将花费太长时间。如果该值太小，神​​经网络将不会收敛到最优解。
alpha：即步长。默认值为 0.0001。这是神经网络在每次迭代中改变系数的程度。如果该值太小，您可能永远不会收敛到最优解。如果该值太大，您可能会错过最佳解决方案。
solver：求解器。'lbfgs', 'sgd' and 'adam'。对于你的数据集，不同的求解器会更快地找到最优解。
'''

from sklearn.datasets import load_digits  # 加载数据集,该数据集为8*8像素的手写数字图像每个像素的灰阶值

X, y = load_digits(n_class=2, return_X_y=True)
print(X.shape, y.shape)
print(X[0])
print(X[0].reshape(8, 8))
print(y[0])

import matplotlib.pyplot as plt

plt.matshow(X[0].reshape(8, 8), cmap=plt.cm.gray)  # 使用matshow()函数绘制图形
plt.xticks(())  # 隐藏X轴标记
plt.yticks(())  # 隐藏y轴标记
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)
mlp_2 = MLPClassifier()
mlp_2.fit(X_train, y_train)

x = X_test[0]
plt.matshow(x.reshape(8, 8), cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())  # 隐藏y轴标记
plt.show()
print('预测x_test的结果为：', mlp_2.predict(X_test))
print('mlp（n_class=2）模型的得分为：', mlp_2.score(X_test, y_test))

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
mlp_all = MLPClassifier(random_state=2)
mlp_all.fit(X_train, y_train)
print('mlp（n_class=all）模型的得分为：', mlp_all.score(X_test, y_test))

y_pred = mlp_all.predict(X_test)  # 根据测试集获取模型对测试集的预测结果
incorrect = X_test[y_pred != y_test]  # 获取测试集X_test中，不符合真实结果的数据集
incorrect_true = y_test[y_pred != y_test]  # 获取测试集y_test中，不符合真实结果的数据集
incorrect_pred = y_pred[y_pred != y_test]  # 获取预测结果中与真实不符合的数据集

for j in range(len(incorrect)):  # 逐个查看预测错误的图像、实际值、预测值
    plt.matshow(incorrect[j].reshape(8, 8))
    cmap = plt.cm.gray
    plt.xticks(())
    plt.yticks(())
    print('true value：', incorrect_true[j])
    print('predicted value：', incorrect_pred[j])
    plt.show()

'''MLP分类器系数：列表中的两个元素对应两个层：隐藏层和输出层。对于这些层中的每一层，我们都有一个系数数组。我们看到我们有一个大小为 784 x 6 的二维数组。有 6 个节点和 784 个输入值馈入每个节点，并且我们对每个连接都有一个权重。'''
print('MLP分类器系数:\n', mlp_all.coefs_)
print('mlp.coefs_[0].shape：', mlp_all.coefs_[0].shape)

'''可视化隐藏层'''
fig, axes = plt.subplots(2, 3, figsize=(5, 4))
for i, ax in enumerate(axes.ravel()):
    coef = mlp_all.coefs_[0][:, i]
    ax.matshow(coef.reshape(8, 8), cmap=plt.cm.gray)
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(i + 1)
plt.show()

'''神经网络的优缺点：
可解释性：
无法简单解释神经网络在做什么。

计算：
神经网络需要相当长的时间来训练。一旦建立起来，神经网络做出预测的速度并不慢，但是，它们并不像其他一些模型那么快。

表现：
神经网络的主要吸引力在于它们的性能。在许多问题上，它们的表现根本无法被其他模型击败。神经网络对于非结构化数据集优于其他模型。
'''

