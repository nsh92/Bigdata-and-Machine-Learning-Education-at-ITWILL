'''
문02) winequality-both.csv 데이터셋을 이용하여 다음과 같이 처리하시오.
   <조건1> quality, type 칼럼으로 교차분할표 작성 
   <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬       
   <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
           -> 각 집단 평균 통계량 출력
   <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
'''

import pandas as pd
from scipy import stats
wine = pd.read_csv('C:/ITWILL/4_Python-II/data/winequality-both.csv')
wine.info()

quality = wine.quality
type1 = wine.type
tab = pd.crosstab(quality, type1)
type(tab)
tab1 = tab.sort_values(by='white', ascending=False)

data = wine[['quality', 'type']]
red = data[data['type']=='red']
white = data[data['type']=='white']
stats.ttest_ind(red['quality'], white['quality'])
# statistic=-9.685649554187696, pvalue=4.888069044201508e-22 : 귀무가설 기각

# 대립가설 채택 -> 단측검정 : red < white
red['quality'].mean()    # 5.6360225140712945
white['quality'].mean()  # 5.87790935075541

cor = wine.corr()
cor['alcohol']
'''
fixed acidity          -0.095452
volatile acidity       -0.037640
citric acid            -0.010493
residual sugar         -0.359415
chlorides              -0.256916
free sulfur dioxide    -0.179838
total sulfur dioxide   -0.265740
density                -0.686745
pH                      0.121248
sulphates              -0.003029
alcohol                 1.000000
quality                 0.444319
'''




