import glob, os
import pandas as pd
pd.set_option('expand_frame_repr', False)
os.chdir("C:\\Users\\T180P\\Desktop\\Tong\\StockAnalysis")
i = 1
fs=glob.glob("*_ts.csv")[::-1]
df1 = pd.read_csv(fs[0],index_col='name',encoding='gbk')
df2 = pd.read_csv(fs[1],index_col='name',encoding='gbk')
df = pd.merge(left=df1, right=df2[['volume']], on='name', how='outer')
df = df[['code','trade','changepercent','volume_x','volume_y','pe','esp','profit','npr','holders']]
flter=((df['changepercent'] > 2.00) & (df['volume_x']/df['volume_y'] > 3.00) & (df['pe']<15) & (df['profit']>10))
df = df[flter]
print(df)

# df[['name','trade_x','trade_y']].dropna(axis=0,how='all').to_csv('aaa.csv')
# print(df.info())
# for file in fs:
#     if i == 1:
#         df1 = pd.read_csv(file,encoding='gbk')
#     else:
#         df2 = pd.read_csv(file,encoding='gbk')
#         df = pd.merge(left=df1, right=df2['trade'], on='code', how='outer')
#     i+=1
