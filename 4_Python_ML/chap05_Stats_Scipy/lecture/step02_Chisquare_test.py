# -*- coding: utf-8 -*-
"""
카이제곱검정(chisquare test)
- 일원 카이제곱, 이원 카이제곱
"""
from scipy import stats
import numpy as np

# 1. 일원 카이제곱 검정
# 귀무가설 : 관측치와 기대치는 차이가 없다.(게임에 적합하다.)
# 대립가설 : 관측치와 기대치는 차이가 있다.(게임에 적합하지 않다.)
real_data = [4, 6, 17, 16, 8, 9] # 관측치
exp_data = [10,10,10,10,10,10] # 기대치
chis = stats.chisquare(real_data, exp_data)
print('statistic = %.3f, pvalue = %.3f'%(chis))
# statistic = 14.200 = k^2 : 카이제곱값, pvalue = 0.014
# statistic = Σ(관측값 - 기댓값)2 / 기댓값 = 기대비율

# 리스트 -> 넘파이
real_arr = np.array(real_data)
exp_arr = np.array(exp_data)

chis2 = sum((real_arr - exp_arr)**2 / exp_arr)
chis2 # 14.200000000000001 카이스퀘어 검정통계량


# 2. 이원 카이제곱 검정
import pandas as pd
smoke = pd.read_csv('C:/ITWILL/4_Python-II/data/smoke.csv')
smoke.info()
'''
교육수준과 흡연유무 간의 독립성 검정
귀무가설 : 교육수준과 흡연유무 간의 관련성이 없다
'''
# DF -> vector
education = smoke.education
smoking = smoke.smoking

chis = stats.chisquare(education, smoking)
# statistic=347.66666666666663, pvalue=0.5848667941187113
# pvalue >= 0.05 이므로 귀무가설 채택


# 교차분할표 : 보통 카이제곱 하기 전에 먼저 확인함
tab = pd.crosstab(education, smoking)
tab
'''
smoking     1   2   3
education            
1          51  92  68
2          22  21   9
3          43  28  21
이것만 봐도 딱히 별 상관성이 없어 보임
'''

'''
성별 vs 흡연 유무 독립성 검정
'''
tips = pd.read_csv('C:/ITWILL/4_Python-II/data/tips.csv')
tips.info()

gender = tips.sex
smoker = tips.smoker
tab1 = pd.crosstab(gender, smoker)

chis1 = stats.chisquare(gender, smoker) # 문자타입이라 안됨

# 더미변수 생성 0/1 -> 1/2 (여기선 0을 인식못함)
gender_dummy = [1 if g == 'male' else 2 for g in gender]
smoker_dummy = [1 if s == 'No' else 2 for s in smoker]

chis1 = stats.chisquare(gender_dummy, smoker_dummy)
# statistic=151.0, pvalue=0.9999993110794366











