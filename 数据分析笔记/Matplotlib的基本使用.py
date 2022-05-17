import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''用来正常显示中文标签'''
plt.rcParams['font.sans-serif']=['SimHei']

'''用来正常显示负号 有中文出现的情况，需要u"内容"'''
plt.rcParams['axes.unicode_minus']=False

'''使用ggplot UI风格生成图表'''
plt.style.use('ggplot')

'''np.linspace(arg1,arg2,arg3)：生成arg1~arg2之间等间隔的arg3个数值'''
x = np.linspace(0, 10, 1000)

'''np.sin(x)：根据x值生成sin(x)的值'''
y = np.sin(x)

'''plt.figure：创建自定义图像,figure即一个弹窗'''
fig = plt.figure(figsize=(8, 8))

'''plt.axes()：调用axes对象（坐标轴对象）去完成绘图任务，即在figure上生成1个坐标轴'''
ax=plt.axes()

'''ax.plot(x,y)：以x为x轴，y为y轴生成图表。color：设置线条颜色。linestyle：设置线条样式。label：设置图例中线条名称'''
ax.plot(x,y,color='k',label='sin(x)')
ax.plot(x,np.cos(x),color='b',linestyle ='--',label='cos(x)')
ax.plot(x,-np.cos(x),color='r',linestyle='-.',label='-cos(x)')
ax.plot(x,-y,color='g',linestyle=':',label='-sin(x)')

'''plt.legend()：显示图例'''
plt.legend()

'''设置x轴的轴标签'''
plt.xlabel('x轴')

'''设置y轴的轴标签'''
plt.ylabel('y轴')

'''设置图表的标题'''
plt.title('正弦曲线图')

'''设置x轴的限制,即设置x轴的最大值，设置后曲线图表按比例缩放'''
plt.xlim([-2,12])

'''设置y轴的限制即设置y轴的最大值，设置后曲线图表按比例缩放'''
plt.ylim([-1.5,1.5])

'''把生成的图表保存到本地'''
plt.savefig('plot.png')

'''弹出提示框显示刚生成的图表'''
plt.show()

'''画一条穿过(10,0)和(100,3)2个点的线'''
plt.plot([10,100],[0,3])
plt.savefig('一条穿过(0,80)和(80,5)2个点的线.png')
plt.show()

'''读取pd.DataFrame对象并根据height、age字段生成点状分布图（散点图）'''
presidents_df = pd.read_csv('president_heights_party.csv', index_col='name')
'''plt.scatter：生成点状分布图（散点图）。默认为圆点。marker：配置散点的形状。color：配置散点的颜色'''
plt.scatter(presidents_df['height'], presidents_df['age'],marker='>',color='r')
plt.xlabel('身高')
plt.ylabel('年龄')
plt.title('U.S. presidents')
plt.savefig("presidents_df_scatter_1.png")
plt.show()

'''pd.DataFrame对象可直接生成plot图表'''
presidents_df.plot(
    kind='scatter',
    y='height',
    x='age',
    title='U.S. presidents'
)
plt.savefig("presidents_df_scatter_2.png")
plt.show()

'''kind='hist'：生成直方图。bins：设置柱状图的柱子粗细，数值越大柱子越细'''
presidents_df['height'].plot(
    kind='hist',
    title='height',
    bins=20
)
plt.savefig("presidents_df_hist_1.png")
plt.show()

'''plt.hist(df[字段名],bins=5)：同样可生成柱状图'''
plt.hist(presidents_df['height'],bins=5)
plt.savefig("presidents_df_hist_2.png")
plt.show()

'''生成箱形图'''
plt.style.use('classic')  #  classic
presidents_df.boxplot(column='height')
plt.savefig("boxplot_1.png")
plt.show()

'''生成条状图，柱状图。条形图通常与直方图混淆。直方图和柱状图的区别是：1、代表的意义不同，直方图所代表的是数据的具体分布，而柱状图所代表的则是数据的大小。2、X轴的意思不同，在直方图中X轴所代表的是定量数据，柱状图里面的X轴所代表的则是分类数据。所以直方图里面的柱子是不能随意移动的，而且X轴上的区间需要连续，但是柱状图上的柱子却能够随意的排序移动。3、柱子的形态不同，直方图上的柱子其宽度是可以不一样的，也就是有宽的，有窄的，但是柱状图上面的柱子宽度是需要一致的。因为柱状图上的宽度并没有数值的含义，但是直方图上面的柱子是代表了区间的长度，所以宽度是根据区间来调整的。'''
party_cnt = presidents_df['party'].value_counts()
plt.style.use('ggplot')
party_cnt.plot(kind ='bar')
plt.savefig("plot.png")
plt.show()