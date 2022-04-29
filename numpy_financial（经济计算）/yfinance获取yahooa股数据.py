import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd

# '''定义data导入比亚迪深圳A股的股票信息'''
# # data=yf.Ticker('002594.sz')
# '''定义data导入美股特斯拉的股票信息'''
# data = yf.Ticker('TLSA')
#
# '''获取股票信息'''
# print(data.info)
# '''获取股票RoE信息，RoE：净资产收益率'''
# print('股票的净资产收益率为：', data.info['returnOnEquity'])
#
# '''获取历史交易信息'''
# hist = data.history(period='1y')
# print(hist.head(5))
# '''获取每个元素间的变化比例'''
# x = hist['Close'].pct_change()
# print(x)
# '''获取股票收益'''
# returns = (x + 1).cumprod()
# print(returns)
# '''生成股票收益折线图，并保存到plot.png文件'''
# returns.plot()
# plt.savefig('plot.png')
#
# '''获取分红（dividends）和拆分（splits)'''
# print(data.actions)
# '''获取分红（dividends）'''
# print(data.dividends)
# '''获取拆分（splits）'''
# print(data.splits)
#
# '''获取年度财务信息'''
# print(data.financials)
# '''获取季度财务信息'''
# print(data.quarterly_financials)
#
# '''获取主要持有人'''
# print(data.major_holders)
# '''获取机构持有人'''
# print(data.institutional_holders)
#
# '''获取年度资产负债表'''
# print(data.balance_sheet)
# '''获取季度资产负债表'''
# print(data.quarterly_balance_sheet)
#
# '''获取年度现金流量表'''
# print(data.cashflow)
# '''获取月度现金流量表'''
# print(data.quarterly_cashflow)
#
# '''获取年度收益'''
# print(data.earnings)
# '''获取季度收益'''
# print(data.quarterly_earnings)
#
# '''获取可持续性'''
# print(data.sustainability)
#
# '''获取分析师建议'''
# print(data.recommendations)
#
# '''获取下一事件（收益等）'''
# print(data.calendar)
#
# '''获取ISIN代码（ISIN：国际证券识别码）'''
# print(data.isin)
#
# '''获取期权到期日期列表'''
# print(data.options)
# '''定义特定到期的期权链，填入期权到期日列表中的日期'''
# opt = data.option_chain('2022-06-17')
# '''获取期权call列表，call：看涨期权'''
# print(opt.calls)
# '''获取期权put列表，put：看跌期权'''
# print(opt.puts)
#
# '''使用代理服务器'''
# hist = data.history(period='max', proxy={"https": "https://47.74.226.8:5001"})
# print(hist.head(5))
#
# '''获取多个股票数据'''
# data = yf.download('twtr AAPL TLSA msft 002594.sz', start='2019-01-01', end='2022-04-30')
# print('多个股票收市价：', data['Close'])
#
# '''获取每个股票的每个元素间的变化比例'''
# x = data['Close'].pct_change()
# print('股票每日收市价变化比例：', x)
#
# '''获取每个元素间变化的统计信息，包括平均值、标准偏差、最小值、最大值、25%、50%、75%的数值'''
# print('变化比例统计信息：', x.describe())
#
# '''获取股票之间的相关性'''
# corr = x.corr()
# print('股票之间的相关性：', corr)
# '''生成股票之间的相关性图表'''
# sm.graphics.plot_corr(corr, xnames=list(x.columns))
# plt.savefig('plot_corr.png')
#
# '''获取投资组合收益'''
# stocks = ['AAPL', 'AMZN', 'MSFT', 'TLSA']
# weights = [0.1, 0.1, 0.1, 0.7]
# data = yf.download(stocks, start='2020-01-01')
# x = data['Close'].pct_change()  # 每日回报
# ret = (x * weights).sum(axis=1)  # 投资组合回报
# cumulative = (ret + 1).cumprod()
# print('投资组合收益：', cumulative)
# '''生成投资组合收益图表'''
# cumulative.plot()
# plt.savefig('plot_cumulative.png')
# '''生成投资组合每日波动率'''
# print('投资组合每日波动率：', np.std(ret))
# '''生成投资组合年度波动率'''
# annual_std = np.std(ret) * np.sqrt(252)
# print('投资组合年度波动率：', annual_std)
# '''生成夏普比率'''
# sharpe = (np.mean(ret) / np.std(ret)) * np.sqrt(252)
# print('投资组合的夏普比率是：', sharpe)

'''投资组合比例猜测，蒙特卡罗模拟'''
stocks = ['AAPL', 'AMZN', 'MSFT', 'TSLA']
data = yf.download(stocks, start='2018-01-01')
#  获取每日股票价格数据
data = data['Close']
x = data.pct_change()
print(x)

p_weights = []
p_returns = []
p_risk = []
p_sharpe = []

'''随机一组随机比例'''
wts = np.random.uniform(size=4)
wts = wts / np.sum(wts)
print(wts)

'''运行一个for循环，生成随机权重并计算投资组合的收益、波动率和夏普比率。'''
count = 500
for k in range(0, count):
    wts = np.random.uniform(size=len(x.columns))
    wts = wts / np.sum(wts)
    p_weights.append(wts)

    mean_ret = (x.mean() * wts).sum() * 252
    p_returns.append(mean_ret)

    ret = (x * wts).sum(axis=1)
    annual_std = np.std(ret) * np.sqrt(252)
    p_risk.append(annual_std)

    sharpe = (np.mean(ret) / np.std(ret)) * np.sqrt(252)
    p_sharpe.append(sharpe)
    # print(p_sharpe)

max_ind = np.argmax(p_sharpe)

print(f'投资组合最大夏普比率：{p_sharpe[max_ind]}')

print(f'投资组合最大回报的分配比例：'
      + f'\n{stocks[0]}:{p_weights[max_ind][0]}'
      + f'\n{stocks[1]}:{p_weights[max_ind][1]}'
      + f'\n{stocks[2]}:{p_weights[max_ind][2]}'
      + f'\n{stocks[3]}:{p_weights[max_ind][3]}')

s = pd.Series(p_weights[max_ind], index=x.columns)
s.plot(kind='bar')
plt.savefig('最佳投资组合的比例.png')

'''生成有效边界图表'''
plt.scatter(p_risk, p_returns, c=p_sharpe, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')

plt.scatter(p_risk[max_ind], p_returns[max_ind], color='r', marker='*', s=500)
plt.show()

plt.savefig('Efficient_Frontier.png')
