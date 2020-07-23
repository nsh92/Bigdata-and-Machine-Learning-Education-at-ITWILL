# -*- coding: utf-8 -*-
"""
집단 간 평균차이 검정
1. 한 집단 평균차이 검정
2. 두 집단 평균차이 검정
3. 대응 두 집단 평균 차이 검정
"""
from scipy import stats  # t검정
import numpy as np       # 숫자 연산
import pandas as pd      # file read

# 1. 한 집단 평균차이 검정
# 대한민국 남자 평균 키(모평균) : 175.5cm
# 표본 추출 30명
sample_data = np.random.uniform(172, 180, size = 300)
sample_data

## 기술통계
sample_data.mean() # 175.95279415001085
one_group_test = stats.ttest_1samp(sample_data, 175.5)
one_group_test
print('statistic = %.5f, pvalue = %.5f'%(one_group_test))
# statistic = 3.62034, pvalue = 0.00035
# 여기서 샘플링한 애들은 모평균과 차이가 있다고 볼 수 있다 [pvalue < 0.05]


# 2. 두 집단 평균 차이 검정
female_score = np.random.uniform(50, 100, size = 30)
male_score = np.random.uniform(45, 95, size = 30)
two_sample = stats.ttest_ind(female_score, male_score)
two_sample
print('statistic = %.5f, pvalue = %.5f'%(two_sample))
# 평균에 차이가 없다고 볼 수 있다

## 기술통계
female_score.mean()
male_score.mean()

## csv 업로드
two_sample = pd.read_csv('C:/ITWILL/4_Python-II/data/two_sample.csv')
two_sample.info()
sample_data = two_sample[['method', 'score']]
sample_data.head() # method는 집단변수
sample_data['method'].value_counts()
# 2    120
# 1    120
# 두 method에 따라 score에 차이가 있는가
# 서브셋으로 교육방법에 따라 나눔
method1 = sample_data[sample_data['method']==1]
method2 = sample_data[sample_data['method']==2]
score1 = method1.score
score2 = method2.score

# NA제거 : 평균으로 대체
score1 = score1.fillna(score1.mean())
score2 = score2.fillna(score2.mean())

two_sample = stats.ttest_ind(score1, score2)
two_sample
print('statistic = %.5f, pvalue = %.5f'%(two_sample))
# statistic = -0.94686, pvalue = 0.34467
# 교육 방법에 따른 별 차이가 없다
score1.mean() # 5.496590909090908
score2.mean() # 5.591304347826086


# 3. 대응 두 집단 평균차이 검정 : 복용전 65 -> 복용후 60
before = np.random.randint(65, size = 30) * 0.5 # 0.5는 실수로 만들기 위함이지 별 의미 없음
after = np.random.randint(60, size = 30) * 0.5

pired_test = stats.ttest_rel(before, after)
print('statistic = %.5f, pvalue = %.5f'%(pired_test))
# statistic = 2.47212, pvalue = 0.01954
before.mean()
after.mean()




























