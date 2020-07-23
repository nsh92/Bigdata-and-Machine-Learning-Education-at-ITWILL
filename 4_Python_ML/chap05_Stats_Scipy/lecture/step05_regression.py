# -*- coding: utf-8 -*-
"""
scipy 패키지의 state 모듈의 함수
 - 통계적 방식의 회귀분석
 1. 단순선형회귀모델
 2. 다중선형회귀모델
"""
from scipy import stats
import pandas as pd

# 1. 단순선형회귀모델
'''
x -> y
'''
score_iq = pd.read_csv("C:/ITWILL/4_Python-II/data/score_iq.csv")
score_iq.info()

## 변수 선택
x = score_iq.iq
y = score_iq['score']

## 회귀모델 생성
model = stats.linregress(x,y)
model
'''
LinregressResult(
slope=0.6514309527270075,         기울기 
intercept=-2.8564471221974657,    절편
rvalue=0.8822203446134699,        설명력(Rsquared)
pvalue=2.8476895206683644e-50,    pvalue : x의 유의성 검정
stderr=0.028577934409305443)      표본오차
'''

print('기울기라능', model.slope)  # 이렇게 회귀객체의 멤버변수로 산출값을 데려올 수 있음
print('절편이라능', model.intercept)

score_iq.head(1)
'''
     sid  score(y) iq(x)  academy  game  tv
0  10001     90     140     2     1   0
'''
# 예측력을 검사해보자 y = X*a + b
X = 140
y_pred = X*model.slope + model.intercept
y_pred # 88.34388625958358

Y = 90
err = Y - y_pred
err # 1.6561137404164157

## 프로덕트 csv 이용
product = pd.read_csv("C:/ITWILL/4_Python-II/data/product.csv")
product.info()
product.corr() # b-c가 가장 높은 상관관계
## x : 제품적절성, y : 제품만족도
model2 = stats.linregress(product['b'], product['c'])
model2
'''
LinregressResult(
slope=0.7392761785971821, 
intercept=0.7788583344701907, 
rvalue=0.766852699640837, 
pvalue=2.235344857549548e-52, 
stderr=0.03822605528717565)
'''
product.head(1)
'''
   a  b  c
0  3  4  3
'''
X = 4
y_pred = X*model2.slope + model2.intercept
y_pred
Y = 3
err = Y - y_pred
err # -0.7359630488589191 # 음수가나올수있으니
err = (Y - y_pred)**2     # 제곱을 취함
err # 0.5416416092857157

X = product['b']
y_pred = X*model2.slope + model2.intercept 
Y = product['c']

len(y_pred) # 264
y_pred[:10]
Y[:10]


# 2. 회귀모델 시각화
from pylab import plot, legend, show

plot(product['b'], product['c'], 'b.') # 산점도
plot(product['b'], y_pred, 'r.-')      # 회귀선
legend(['x, y scatter', 'regress model line'])
show()


# 3. 다중선형회귀모델 : y ~ x1 + x2 ...
from statsmodels.formula.api import ols
wine = pd.read_csv('C:/ITWILL/4_Python-II/data/winequality-both.csv')
wine.info()

wine.columns = wine.columns.str.replace(' ', '_')
wine.info()

# quality vs other
cor = wine.corr()
cor['quality'] # 영향력이 높은 3개 뽑음
formula = "quality ~ alcohol + chlorides + volatile_acidity"
model = ols(formula, data = wine).fit()
model # 모델 객체가 생성되었다는 표시
model.summary()  # R의 summary(모델)
# Adj. R-squared: 0.259                          # 설명력이 높진않내
# F-statistic: 758.6, Prob (F-statistic): 0.00   # 통계적으로는 유의하다 (유의성검정 F통계)
# 그 아래칸은 각 x에 대한 설명
# P>|t| 0.05보다 작은값이면 유의한 변수다라는 거 : chlorides는 유의하지 않다
# coef : 기울기
# Durbin-Watson: 1.645 잔차검정

# 회귀객체에 대한 멤버들 이용
# 기울기, 절편 호출
model.params
'''
Intercept           2.909941
alcohol             0.319578
chlorides           0.159258
volatile_acidity   -1.334944
'''

# y예측치 호출
y_pred = model.fittedvalues  # 예측치
y_true = wine.quality        # 관측치
err = (y_true - y_pred)**2
y_true[:10]
y_pred[:10]

# 대표값 비교를 통해서도 추측 가능
y_true.mean()
y_pred.mean()

# 차트 확인
import matplotlib.pyplot as plt
plt.plot(y_true, 'b.', label='real values')
plt.plot(y_pred, 'r.', label='y prediction')
plt.yticks(range(0, 10))
plt.legend(loc = 'best')
plt.show()


























