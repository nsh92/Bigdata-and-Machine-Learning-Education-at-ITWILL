# -*- coding: utf-8 -*-
"""
시계열 분석(time series analysis)
1. 시계열 자료 생성
2. 날짜형식 수정(다국어)
3. 시계열 시각화
4. 이동평균 기능 : 5일, 10일, 20일 평균 -> 추세선 평활(smoothing)
"""
from datetime import datetime # 날짜형식 수정 모듈
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. 시계열 자료 생성
time_data = pd.date_range("2017-03-01", "2020-03-30")
time_data # length=1126, freq='D' : 1126개, 하루 단위
## 하루 단위말고 월 단위
time_data2 = pd.date_range("2017-03-01", "2020-03-30", freq='M')
time_data2      # freq='M'
len(time_data2) # 36

# 월 단위 매출 현황
x = pd.Series(np.random.uniform(10, 100, size = 36))
# 날짜 벡터와 그에 대응하는 숫자 벡터가 생김
df = pd.DataFrame({'data' : time_data2, 'price' : x})
df # 전형적인 시계열 데이터 x축 : 시간, y축 : 값

plt.plot(df['data'], df['price'], 'r.-') # df를 넣으면 앞에오는 게 x, 뒤에 오는 게 y
plt.show()


# 2. 날짜형식 수정 (다국어)
kospi = pd.read_csv("C:/ITWILL/4_Python-II/data/cospi.csv")
kospi.info()
kospi.head() # 다국어 형식의 날짜
date = kospi['Date']
len(date) # 247

# 리스트내포 : 26-Feb-16 --> 2016-02-16
kdate = [datetime.strptime(d,'%d-%b-%y') for d in date]
         # 들어오는 날짜를 지정한 포멧대로
kospi['Date'] = kdate
kospi.head()

# 3. 시계열 시각화
kospi.index # RangeIndex(start=0, stop=247, step=1)

# 컬럼 -> 인덱스로
new_kospi = kospi.set_index('Date')
new_kospi.index
new_kospi.info()

new_kospi['2016']
len(new_kospi['2015'])
new_kospi['2015']
new_kospi['2015-05':'2015-03']

# 서브셋
new_kospi_HL = new_kospi[['High', 'Low']]
new_kospi_HL.index
new_kospi_HL['2015'].plot(title = '2015 year : High vs Low')
plt.show()

new_kospi_HL['2016'].plot(title = '2016 year : High vs Low')
plt.show()

new_kospi_HL['2016-02'].plot(title = '2016 year : High vs Low')
plt.show()


# 4. 이동평균 기능 : 5일, 10일, 20일 평균 -> 추세선 평활(smoothing)
## 1) 5일 단위 이동평균 : 5일 단위 평균 -> 마지막 5일째 이동
roll_mean5 = pd.Series.rolling(new_kospi_HL, window=5, center=False).mean()
roll_mean10 = pd.Series.rolling(new_kospi_HL, window=10, center=False).mean()
roll_mean20 = pd.Series.rolling(new_kospi_HL, window=20, center=False).mean()

## 시각화
roll_mean5 = pd.Series.rolling(new_kospi_HL.High, window=5, center=False).mean()
roll_mean10 = pd.Series.rolling(new_kospi_HL.High, window=10, center=False).mean()
roll_mean20 = pd.Series.rolling(new_kospi_HL.High, window=20, center=False).mean()
new_kospi_HL.High.plot(color='b', label='High column')
roll_mean5.plot(color='r', label='5day')
roll_mean10.plot(color='g', label='10day')
roll_mean20.plot(color='orange', label='20day')
plt.legend(loc='best')
plt.show()
























