'''
문1) score_iq.csv 데이터셋을 이용하여 단순선형회귀모델을 생성하시오.
   <조건1> y변수 : score, x변수 : academy      
   <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
   <조건3> 회귀선 적용 시각화 
   
문2) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
   <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정
   iris = pd.read_csv('../data/iris.csv')
   iris.columns = iris.columns.str.replace('.', '_')
   <조건2> y변수 : 1번째 칼럼, x변수 : 2~4번째 칼럼    
   <조건3> 회귀계수 확인 
   <조건4> 회귀모델 세부 결과 확인  : summary()함수 이용 
'''

from scipy import stats
import pandas as pd
import statsmodels.formula.api as sm
from pylab import plot, legend, show
score_iq = pd.read_csv("C:/ITWILL/4_Python-II/data/score_iq.csv")
iris = pd.read_csv("C:/ITWILL/4_Python-II/data/iris.csv")

# 문1
model = stats.linregress(score_iq['academy'], score_iq['score'])
model
'''
LinregressResult(
slope=4.847829398324446, intercept=68.23926884996192, rvalue=0.8962646792534938, 
pvalue=4.036716755167992e-54, stderr=0.1971936807753301)
'''
y_pred = score_iq['academy']*model.slope + model.intercept
plot(score_iq['academy'], score_iq['score'], 'b.') # 산점도
plot(score_iq['academy'], y_pred, 'r.-')      # 회귀선
legend(['x, y scatter', 'regress model line'])
show()

# 문2
iris.columns = iris.columns.str.replace('.', '_')
iris.info()
cor = iris.corr()
cor['Sepal_Length']
formula = "Sepal_Length ~ Sepal_Width + Petal_Length + Petal_Width"
model1 = ols(formula, data = iris).fit()
model1.summary()
'''
Intercept        1.8560
Sepal_Width      0.6508
Petal_Length     0.7091 
Petal_Width     -0.5565
세 변수 다 유의함, Adj. R-squared: 0.856 강한 설명력
'''
y_pred1 = model1.fittedvalues
y_true = iris['Sepal_Length']

import matplotlib.pyplot as plt
model1.params

plt.plot(y_true, 'b-', label='real values')
plt.plot(y_pred1, 'r-', label='y prediction')
plt.yticks(range(3, 10))
plt.legend(loc = 'best')
plt.show()





