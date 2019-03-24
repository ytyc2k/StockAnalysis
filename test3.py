# import tushare as ts
from datetime import datetime,timedelta
# dt=(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
# dt=(datetime.now()).strftime('%Y-%m-%d')
# df=ts.get_today_all()
# df.to_csv('DailyStockPrice'+dt+'.csv')
# df=ts.get_stock_basics()
# df.to_csv('StockBasicInfo.csv')

#
# import pandas as pd
# df = pd.read_csv('DailyStockPrice_'+v_yes)
# fil=((df['pb']>15) & (df['code']>601600))
# print(df.head(3))
# print(df.ix[fil])
# df.ix[fil].to_csv('Result')

import tushare as ts
import pandas as pd
from datetime import datetime,timedelta

def get_today_all_ts(date):
    date_now = date
    df_close, df_basics = pd.DataFrame(),pd.DataFrame()
    while df_close.empty:
        try:
            df_close = ts.get_today_all()
            print('Done1')
        except:
            print('Error1')
            df_close = pd.DataFrame()
    while df_basics.empty:
        try:
            df_basics = ts.get_stock_basics()
            print('Done2')
        except:
            print('Error2')
            df_basics = pd.DataFrame()
    df_all = pd.merge(left=df_close, right=df_basics, on='name', how='outer')
    print('Done3')
    df_all['code'] = df_all['code'].astype(str) + ' '
    df_all.to_csv(str(date_now) + '_ts.csv', index=False, encoding='gbk')
    return df_all
def read_from_file_ts():
    df1 = pd.read_csv('DailyStockPrice2019-03-18.csv')
    # df2 = pd.read_csv('StockBasicInfo.csv')
    df2 = ts.get_stock_basics()
    df_all = pd.merge(left=df1, right=df2, on='name', how='outer')
    df_all['code'] = df_all['code'].astype(str) + ' '
    df_all.to_csv(str(dt) + '_ts.csv', index=False, encoding='gbk')
if __name__ == '__main__':
    dt=(datetime.now()- timedelta(0)).strftime('%Y%m%d') # China Stock Market close date
    get_today_all_ts(date=dt)
