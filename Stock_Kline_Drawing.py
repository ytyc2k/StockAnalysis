import tushare as ts
import matplotlib.pyplot as pt
code='600230'
d=ts.get_k_data(code,ktype='D')
print(len(d))
pt.title(code)
pt.plot(d['high'],c='g')
pt.plot(d['low'],c='g')
pt.savefig('b.png')
pt.show()
print(d)