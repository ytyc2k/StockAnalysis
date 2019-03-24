import pandas as pd
from pandas.core.frame import DataFrame
import time

def convert_currency(value):
    if isinstance(value, str):
        value = float(value.replace('--', '0.00'))
    return value

# 沪深共89页
# for rYear in range(2018, 2019):  # 每次限两至三年
#     for i in range(1, 5):
#         tables = pd.read_html(
#             "http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/mainindex/index.phtml?s_i=&s_a=&s_c=&reportdate=" + str(
#                 rYear) + "&quarter=4&p=" + str(i))
#         for table in tables:
#             if i == 1:
#                 mainTable = DataFrame(table).ix[0:, 0:]
#             else:
#                 mainTable = pd.concat([mainTable, table.ix[0:, 0:]])
#
#
#     # pd.to_numeric(mainTable['净资产收益率(%)'], downcast='float', errors='ignore')
#     mainTable.to_excel('./download/html-新浪-沪深F10-业绩报表-' + str(rYear) + 'Q4.xlsx')
#
# print(mainTable['净资产收益率(%)'])

fn='./download/html-新浪-沪深F10-业绩报表-' + str(2018) + 'Q4.xlsx'
cvt={
                '净资产收益率(%)': convert_currency,
                '每股现金流量(元)': convert_currency,
             }
DataFrame = pd.read_excel(fn,converters=cvt)
# DataFrame['净资产收益率(%)'] = DataFrame['净资产收益率(%)'].apply(convert_currency)
# DataFrame['每股现金流量(元)'] = DataFrame['每股现金流量(元)'].apply(convert_currency)
# print(DataFrame[(DataFrame['每股收益(元)'] > 1.0) & (DataFrame['净资产收益率(%)'] > 20)  & (DataFrame['净利润同比(%)'] > 10) & (DataFrame['每股现金流量(元)'] > 0)][0:5])
DataFrame[(DataFrame['每股收益(元)'] > 1.0) & (DataFrame['净资产收益率(%)'] > 20)  & (DataFrame['净利润同比(%)'] > 10)].to_excel('./download/haha.xlsx')