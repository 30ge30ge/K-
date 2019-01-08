# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:26:41 2018

@author: Administrator
"""

import tushare as ts
import pandas as pd 
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib.pylab import date2num
import datetime
import talib
ts=ts.get_hist_data("002941",start="2018-08-27",end="2019-01-07")
ts=ts[["open","close","high","low","volume"]]
ts.sort_values(by="date",inplace=True)
print(ts)

data_list = []
for dates,row in ts.iterrows():
    # 将时间转换为数字
    date_time = datetime.datetime.strptime(dates,"%Y-%m-%d")
    t = date2num(date_time)
    open,high,low,close = row[0:4]
    datas = (t,open,high,low,close)
    data_list.append(datas)
fig, ax = plt.subplots(figsize=(8,4))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick_ochl(ax, data_list, width=0.4, colorup="red", colordown="green", alpha=1.0)
ax.xaxis_date()

# 设置日期刻度旋转的角度 
plt.xticks(rotation=45)
plt.title("002941")
plt.xlabel("date")
plt.ylabel("price")
# x轴的刻度为日期
ax.xaxis_date ()
plt.grid()

avg_5 = talib.MA(ts["close"], timeperiod=5)
print(avg_5)
fig=plt.subplots(figsize=(8,4))
plt.plot(avg_5,color="g")
plt.xticks(rotation=75)
plt.show()
macd, macdsignal, macdhist = talib.MACD(ts["close"], fastperiod=12, slowperiod=26, signalperiod=9)
fig=plt.subplots(figsize=(8,4))
plt.plot(macd)
plt.xticks(rotation=75)
plt.show()
upperband, middleband, lowerband = talib.BBANDS(ts["close"], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
fig=plt.subplots(figsize=(8,4))
plt.plot(upperband)
plt.plot(middleband)
plt.plot(lowerband)
plt.xticks(rotation=75)
plt.show()