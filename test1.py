#import tushare as ts
# HisPrice=tushare.get_hist_data('000001')
# print(HisPrice)
# HisPrice.to_csv('price.csv')

# pro = ts.pro_api()
# ts.set_token('2ea046a36dbb32e269770c7cb28bd826164adb2588936cefc04dc3e3')
# df = pro.top_list(trade_date='20190315')
# print(df)

# pro = ts.pro_api()
# ts.set_token('2ea046a36dbb32e269770c7cb28bd826164adb2588936cefc04dc3e3')
# df = pro.daily(ts_code='600115.SH')
# # print(df)
# from datetime import datetime,timedelta
# v_yestoday=(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
# df=ts.get_hist_data('000686',v_yestoday)
# print(df)

import tushare as ts
import numpy as np
df = ts.get_money_supply_bal()[::-1]
print(df.head())
df['m2']=df['m2'].astype(float)
df['rate'] = df['m2'].apply(np.log).diff().apply(lambda x: format(x, '+.2%'))
print(df[['year','m2','rate']])

# destTable = srcTable.loc[srcTable.tid == 1, ['ts1', 'ts2']].sort_values(by='ts1')
# destTable.columns = ['deltaTs1', 'deltaTs2']
# destTable = destTable.diff()
# destTable = destTable.fillna(0)
# destTable['delay'] = destTable['deltaTs2'] - destTable['deltaTs1']
# print(destTable)
