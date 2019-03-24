import tushare as ts
df=ts.get_hist_data('600115')

# print(df.head(4))
# print(df[['open','close']][:2])#选取两列的前两行
# print(df.iloc[[1,3],[0,2]])#选取1、3两行的0、2列
# print(df.ix[[1,3],['open','close']])#选取1、3两行的0、2列
# print(df.ix[:'2019-03-13',['open','close']])
# print(df.ix[:3,['open','close']])
# print(df.ix[:3,[0,2]])
# print(df.loc['2019-03-15':'2019-03-13',['close','open']]) #选取1、2两行的2、4列
# print(df.iloc[[1,3],[0,2]])#选取1、3两行的0、2列
# print(df.loc['2019-03-15':'2019-03-13'])
# print(df.loc[['2019-03-15','2019-03-13']])
# print(df.iloc[1:3])

df['haha']=0.0
df.loc[(df['open']==6.18),'haha']=120.00
df.ix[(df['open']>=6.18),[-1]]=120.00
df.ix[(df['close']==6.07),'haha']=120.00
df.haha=df.haha.map({120: 100, 0: 5.5})
df.haha = df.haha.apply(lambda x: 55.0 if x==100.0 else 77.0)
# df['total'] = df[['open','close']].apply(lambda x : x.sum(),axis=1)
df['total'] = df[['open', 'close']].apply(sum, axis=1)
fil=((df['total']>10) & (df['haha']>10))
print(df.ix[fil,1:2])
# print(df.head(10))
# # select * from df where 'close'==5.85
# # print(df['close'])
# print(df.info())
