# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:46:09 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_finance as mpf
import datetime
from matplotlib.pylab import date2num
import talib
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
df = pd.read_csv("F:/数据分析/MT4/XAUUSDdl.csv",engine='python',sep=",")
df = df[["时间","开盘价","收盘价","最高价","最低价"]]
df.reset_index(drop=True, inplace=True)
print(df)
closedata=df["收盘价"]
datadate=df["时间"]
df["时间"] = pd.to_datetime(df["时间"])
df.set_index("时间", inplace=True)
print(df)
fig=plt.subplots(figsize=(12,8))
plt.plot(df["收盘价"])
plt.show()

max_draw_down = 0
temp_max_value = 0
for i in range(1, len(df["收盘价"])):
    temp_max_value = max(temp_max_value, df["收盘价"][i-1])
    max_draw_down = min(max_draw_down, df["收盘价"][i]/temp_max_value-1)
print(str(max_draw_down))


data_list=[]
for dates,row in df.iterrows():
    t = date2num(dates)
    open,high,low,close = row[0:4]
    datas = (t,open,high,low,close)
    data_list.append(datas)

fig, ax = plt.subplots(figsize=(16,8))
fig.subplots_adjust(bottom=0.3)
mpf.candlestick_ochl(ax, data_list, width=0.4, colorup="red", colordown="green", alpha=1.0)
ax.xaxis_date()
# 设置日期刻度旋转的角度 
plt.xticks(rotation=45)
plt.title("价差走势K线图")
plt.xlabel("date")
plt.ylabel("price")
avg_5 = talib.EMA(df["收盘价"], timeperiod=5)
plt.plot(avg_5,color="r")
# x轴的刻度为日期
ax.xaxis_date ()
upperband, middleband, lowerband = talib.BBANDS(df["收盘价"], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
plt.plot(upperband)
plt.plot(middleband)
plt.plot(lowerband)
plt.grid()
plt.show()
print(avg_5)





