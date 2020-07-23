# -*- coding: utf-8 -*-
"""
회귀방정식에서 기울기와 절편 식
 기울기 = Cov(x,y) / Sxx(x의 편차 제곱의 평균)
 절편 = y_mu - (기울기 * x_mu)
"""
from scipy import stats # 회귀모델
import pandas as pd

galton = pd.read_csv('C:/ITWILL/4_Python-II/data/galton.csv')
galton.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 928 entries, 0 to 927
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   child   928 non-null    float64
 1   parent  928 non-null    float64
 '''
# 부모의 키X가 자녀의 키Y에 미치는 영향
x = galton['parent']
y = galton['child']
model = stats.linregress(x, y)
# slope=0.6462905819936423, intercept=23.941530180412748, 
# rvalue=0.4587623682928238, pvalue=1.7325092920142867e-49, stderr=0.04113588223793335
# rvalue : 부모의 키가 모든 것을 결정하지 않는구나

# Y = x*a + b
y_pred = x*model.slope + model.intercept
y_pred
y_true = y

# 예측치 vs 관측치(정답)
y_pred.mean()
y_true.mean() # 먼저 평균 비교 : 매우 유사

# 기울기 계산식
xu = x.mean()
yu = y.mean()
Cov_xy = sum((x-xu) * (y-yu)) / len(x)
Sxx = np.mean((x-xu)**2)
slope = Cov_xy / Sxx # 0.6462905819936413

# 절편 계산식
incept = yu - (slope * xu) # 23.94153018041171

# 설명력 rvalue
galton.corr() # 0.458762 : 이게 걍 rvalue구만
y_pred = x * slope + incept
y_pred.mean() # 68.08846982758423





























