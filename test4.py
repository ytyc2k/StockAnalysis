# -*- coding: utf-8 -*-
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option('expand_frame_repr', False)
date_now = '20190320'
print(str(date_now))

# 读取TDX的每日股票数据
df = pd.read_csv('{}_ts.csv'.format(str(date_now)), encoding='gbk')
df.fillna(0, inplace=True)
df.replace('nan ', 0, inplace=True)
df[['changepercent', 'pe', 'mktcap', 'nmc']] = df[['changepercent', 'pe', 'mktcap', 'nmc']].astype(float)
df['timeToMarket'] = pd.to_datetime(df['timeToMarket'])
df['code'] = df['code'].astype(str)  # 转化成str后，NAN也变成nan str格式

print(df.iloc[1])

# 找出上涨的股票
df_up = df[df['changepercent'] > 0.00]
# 走平股数
df_even = df[df['changepercent'] == 0.00]
# 找出下跌的股票
df_down = df[df['changepercent'] < 0.00]

# 找出涨停的股票
limit_up = df[df['changepercent'] >= 9.70]
limit_down = df[df['changepercent'] <= -9.70]

# 涨停股数中的未封板股，上市日期小于15天
limit_up_new = limit_up[pd.to_datetime(date_now) - limit_up['timeToMarket'] <= pd.Timedelta(15)]
# 涨停股数中次新股，上市日期小于1年
limit_up_fresh = limit_up[pd.to_datetime(date_now) - limit_up['timeToMarket'] <= pd.Timedelta(365)]

# 涨停股数中的未封板股，上市日期小于15天
limit_down_new = limit_down[pd.to_datetime(date_now) - limit_down['timeToMarket'] <= pd.Timedelta(15)]
# 涨停股数中次新股，上市日期小于1年
limit_down_fresh = limit_down[pd.to_datetime(date_now) - limit_down['timeToMarket'] <= pd.Timedelta(365)]

print('A股上涨个数： %d, A股下跌个数： %d, A股走平个数: %d' % (df_up.shape[0], df_down.shape[0], df_even.shape[0]))
print('A股总成交额：%d, 总成交量：%d' % (df['amount'].sum(), df['volume'].sum()))
print('A股平均市盈率：%.2f， 平均流通市值 %.2f 亿, 平均总市值 %.2f 亿' % (df['pe'].mean(), df['nmc'].mean(), df['mktcap'].mean()))
print('涨停数量：%d 个, 涨停中上市日期小于15天的：%d, 涨停中上市日期小于1年的：%d' % (limit_up.shape[0], limit_up_new.shape[0], limit_up_fresh.shape[0]))
print('跌停数量：%d 个, 涨停中上市日期小于15天的：%d, 涨停中上市日期小于1年的：%d' % (limit_down.shape[0], limit_down_new.shape[0], limit_down_fresh.shape[0]))