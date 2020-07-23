# -*- coding: utf-8 -*-
"""
scipy 패키지의 확률분포 검정
1. 정규분포 검정
   - 연속변수 확률분포 : 정규분포, 균등분포, 카이제곱, T/Z/F분포
2. 이항분포 검정(2가지 변수의 확률분포)
   - 이산확률분포 : 베르누이분포, 이항분포, 포아송분포
"""
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# 1. 정규분포 검정
# 평균 중심 좌우 대칭성 검정

## 1) 정규분포 객체 생성
mu = 0; std = 1 # 표준정규분포
std_norm = stats.norm(mu, std) # 정규분포 객체 생성
std_norm # <scipy.stats._distn_infrastructure.rv_frozen at 0x142602c5908> : 객체 정보만 조회됨

## 2) 정규분포 확률 변수
N = 1000 # 시행횟수
norm_data = std_norm.rvs(N) # 시뮬레이션(.rvs) : 1000 난수 생성
len(norm_data) # 1000

## 3) 히스토그램 : 좌우대칭성 확인
plt.hist(norm_data)
plt.show()

## 4) 정규성 검정
## 귀무가설 : 정규분포와 차이가 없다
stats1, pvalue = stats.shapiro(norm_data)
                # (0.9972438216209412, 0.08546201139688492)
                #     검정통계량           p-value
print('검정통계량 : %.5f'%(stats1))  # -1.96 ~ +1.96 : 채택역
print('pvalue : %.5f'%(pvalue))    # >=0.05(알파값) : 채택역


# 2. 이항분포 검정 : 2가지 범주의 확률분포 + 가설검정
'''
- 베르누이 분포 : 이항변수(성공 or 실패)에서 성공(1)이 나올 확률분포(모수 : 성공확률), 성공확률을 미리 알고 있어야함
- 이항분포 : 베르누이 기반 + 시행횟수(n) 적용한 확률분포(모수 : P, N)

ex) P = 게임에 이길 확률(40%), N = 시행횟수(100번) -> 성공횟수는 얼마나 될까
'''
N = 100 # 시행횟수
P = 0.4 # 성공확률(모수)

## 1) 베르누이 분포 -> 이항분포 확률 변수
x = stats.bernoulli(P).rvs(N)  # 변수명과 모듈명이 겹치지 않도록 조심하자
x # 0실패, 1성공

## 2) 성공횟수
x_succ = np.count_nonzero(x) # 0이 아닌 걸 센다
print('성공횟수 =', x_succ) # 성공횟수 = 실행할 때마다 달라짐

## 3) 이항분포 검정 : 이항분포에 대한 가설검정
## 귀무가설 : 게임에 이길 확률은 40%와 다르지 않다.
'''
stats.binom_test(x, n, p=0.5, alternative='two-sided') 기본 파라미터 및 기본값들
x : 성공횟수
n : 시행횟수
p : 성공확률
alternative='two-sided' : 양측검정 여부
'''
pvalue = stats.binom_test(x=x_succ, n=N, p=P, alternative='two-sided')
# 0.2614269815307507 : p-value

if pvalue >= 0.05:
    print('게임에 이길 확률은 40%와 다르지 않다')
else:
    print('게임에 이길 확률은 40%와 다르다고 볼 수 있다')

'''
사례 : 100명의 합격자 중에서 남자 합격자는 45일 때, 
남녀 합격률의 차이가 있다고 볼 수 있는가?
'''
# 귀무가설 : 남녀 합격률의 차이가 없다 : p=50:50
nam = stats.bernoulli(0.5).rvs(100)
nam
nam_succ = np.count_nonzero(nam)

pv = stats.binom_test(x=45, n=100, p=0.5, alternative='two-sided')
# 0.36820161732669654

if pv >= 0.05:
    print('남녀 합격률에 유의한 차이가 없다')
else:
    print('남녀 합격률에 유의한 차이가 있다')




