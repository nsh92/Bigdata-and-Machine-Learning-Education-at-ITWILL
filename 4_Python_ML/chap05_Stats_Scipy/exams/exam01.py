# -*- coding: utf-8 -*-
"""
문01) 이항검정 : 토요일(Sat)에 오는 여자 손님 중 비흡연자가 흡연자 보다 많다고 할 수 있는가?

 # 귀무가설 : 비흡연자와 흡연자의 비율은 차이가 없다.(P=0.5)
"""

import pandas as pd

tips = pd.read_csv('C:/ITWILL/4_Python-II/data/tips.csv')
print(tips.info())
print(tips.head())

day = tips['day']
print(day.value_counts())
'''
Sat     87  -> 토요일 빈도수 
Sun     76
Thur    62
Fri     19
'''

gender = tips['sex']
print(gender.value_counts())
'''
Male      157
Female     87 -> 여자 빈도수
'''
tips_day = tips[tips['day'] == 'Sat']
tips_day.shape # (87, 7)

tips_day_gender = tips_day[tips_day['sex'] == 'Female']
tips_day_gender.shape # (28, 7)

tips_day_gender['smoker'].value_counts()
'''
Yes    15
No     13
'''

smk_sat = stats.binom_test(x=13, n=28, p=0.5, alternative='two-sided')
smk_sat # 0.8505540192127226
# 차이가 없다고 볼 수 있다.