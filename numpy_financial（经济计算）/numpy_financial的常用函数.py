import numpy_financial as npf

'''fv：计算预估投资价值'''
rate = 0.035
nper = 20
pmt = -2000
pv = -1000000
fv = npf.fv(rate=rate / 12, nper=nper * 12, pmt=pmt, pv=pv)
#  rate：年化投资回报率
#  nper：投资年数
#  pmt：每月投入资金（负值）
#  pv：期初值（负值）
print(f'期初资产￥{abs(pv)}元，每月再投入￥{abs(float(pmt)):.2f}元，年均收益率{rate * 100:.2f}%，{nper}年后期末价值为：￥{abs(fv):.2f}元。')

'''pv：计算未来金额在现在的价值'''
rate = 0.035
nper = 20
pmt = -2000
fv = 5000000
pv = npf.pv(rate=rate / 12, nper=nper * 12, pmt=pmt, fv=fv)
#  rate：年化投资回报率
#  nper：投资年数
#  pmt：每月投入资金（负值）
#  fv：预期达到的资产总值(正值）
print(
    f'年均收益率{rate * 100:.2f}%，每月投入￥{abs(float(pmt)):.2f}元，投资{nper}年后，期末资产￥{abs(float(fv)):.2f}元，需要投入本金：￥{abs(pv):.2f}元。')

'''pmt：计算每期支付金额'''
rate = 0.075
nper = 20
pv = 1000000
fv = 0
per = 240
pmt = npf.pmt(rate=rate / 12, nper=nper * 12, pv=pv, fv=fv)
#  rate：年化投资回报率
#  nper：投资年数
#  pv：现值（正值）
#  fv：预期达到的资产总值(正值）
#  per：还款的第几期
'''ppmt：每期支付金额之本金'''
ppmt = npf.ppmt(rate=rate / 12, per=per, nper=nper * 12, pv=pv, fv=fv)
'''ipmt：每期支付金额之利息'''
ipmt = npf.ipmt(rate=rate / 12, per=per, nper=nper * 12, pv=pv, fv=fv)
print(
    f'年利率{rate * 100}%，贷款总额￥{abs(pv)}元，{nper}年还清，每月还款￥{abs(pmt):.2f}元，第{per}期本金：￥{abs(ppmt):.2f}元，第{per}期利息：￥{abs(ipmt):.2f}元。'
)

'''nper：分期数'''
rate = 0.075
pmt = -8055.93
pv = 1000000
fv = 0
#  rate：年利率
#  pmt：每期还款金额（负值）
#  pv：贷款总额（正值）
#  fv：期末剩余贷款金额(正值）
nper = npf.nper(rate=rate / 12, pmt=pmt, pv=pv, fv=fv)
print(
    f'年利率{rate * 100}%，贷款总额￥{abs(pv)}元，每月还款￥{abs(pmt)}，需要还款{nper / 12:.2f}年，共{nper:.2f}期。还款总金额:￥{-pmt * nper:.2f}元。'
)

'''rate：计算利率'''
nper = 240
pmt = -8055.93
pv = 1000000
fv = 0
#  nper：还款期数
#  pmt：每期还款金额（负值）
#  pv：贷款总额（正值）
#  fv：期末剩余贷款金额(正值）
rate = npf.rate(nper=nper, pmt=pmt, pv=pv, fv=fv, when='end', guess=0.1, tol=1e-06, maxiter=100)
print(
    f'贷款总额￥{abs(pv)}元，每月还款￥{abs(pmt)}元，分{nper}期还清，期末贷款本金剩余￥{fv}元，贷款利率为：{rate * 12 * 100:.2f}%。'
)

'''npv：净现值
净现值是指投资方案所产生的【现金净流量】（流入-流出）以资金成本为贴现率折现之后与原始投资额现值的差额
经济意义:
NPV>0表示项目实施后，除保证可实现预定的收益率外，尚可获得更高的收益。
NPV<0表示项目实施后，未能达到预定的收益率水平，而不能确定项目已亏损。
NPV=0表示项目实施后的投资收益率正好达到预期，而不是投资项目盈亏平衡。
'''
rate = 0.281
values = [-100, 39, 59, 55, 20]
#  rate：scalar数值，折现率。
#  values：现金流。正数代表‘收入’或‘取款’，负数代表‘投资’或‘存款’。第一个值必须是初始的投资，也就是必须是负数。
#  公式：NPV=Σ（CI-CO）（1+i）^(-t)
npv = npf.npv(rate=rate, values=values)
print(f'净现值为：{npv:.5}')

'''irr：内部收益率
一个人投资100，然后按照固定的时间间隔进行取款，[39,59,55,20]。
假设最终值是0，那么他投资的100，最终产出是173。
因为阶段性取款，收益率不是简单的做平均。而是用以下公式计算：
-100 + 39/(1+r) + 59/(1+r)^2 + 55/(1+r)^3 + 20/(1+r)^4 = 0
'''
values = [-100, 39, 59, 55, 20]
#  values：array形式，每一期的现金流。正数代表‘收入’或‘取款’，负数代表‘投资’或‘存款’。第一个值必须是初始的投资，也就是必须是负数。
irr = npf.irr(values=values)
print(f'投资金额为：￥{-values[0]}元，产出总金额为：￥{sum(values[1:])}元，内部收益率为：{irr:.5f}')

'''mirr：修正内部收益率
指在一定贴现率的条件下，将投资项目的未来现金流入量按照一定的贴现率（再投资率）计算至最后一年的终值，
再将该投资项目的现金流入量的终值折算为现值，并使现金流入量的现值与投资项目的现金流出量达到价值平衡的贴现率。
这种方法同时考虑了不同的投资成本（Finance Rate）和现金再投资收益率（Reinvestment Rate）。
'''
values = [-100, 110, -110, 120]
finance_rate = 0.065
reinvest_rate = 0.075
#  values：现金流（必须有一个正值和一个负值），第一个值可以看做是沉没成本。
#  finance_rate：现金流中使用的资金支付的利率
#  reinvest_rate：将现金流再投资的收益率
mirr = npf.mirr(values=values, finance_rate=finance_rate, reinvest_rate=reinvest_rate)
print(f'投资金额为：￥{-values[0]}元，产出总金额为：￥{sum(values[1:])}元，修正内部收益率：{mirr:.5f}')
