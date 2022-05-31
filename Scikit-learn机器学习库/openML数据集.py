import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml  # fetch_openml:从open ML数据库下载数据集
from sklearn.neural_network import MLPClassifier

X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
X0 = X[y == '0']
y0 = y[y == '0']
print('X.shape:', X0.shape)
print('y.shape:', y0.shape)
print('min(X):', np.min(X0), '\nmax(X):', np.max(X0))
print('y[0:5]:', y0[0:5])

mlp_openML = MLPClassifier(
    hidden_layer_sizes=(6,),
    max_iter=200,
    alpha=1e-4,
    solver='sgd',
    random_state=2
)
mlp_openML.fit(X0, y0)

print('the end')

'''可视化隐藏层'''
fig, axes = plt.subplots(2, 3, figsize=(5, 4))
for i, ax in enumerate(axes.ravel()):
    coef = mlp_openML.coefs_[0][:, i]
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray)
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(i + 1)
plt.savefig('可视化隐藏层.png')
plt.show()
