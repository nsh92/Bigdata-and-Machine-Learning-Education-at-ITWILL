'''
문2) dataset.csv 파일을 이용하여 교차테이블과 누적막대차트를 그리시오.
  <조건1> 성별(gender)과 만족도(survey) 칼럼으로 교차테이블  작성 
  <조건2> 교차테이블 결과를 대상으로 만족도 1,3,5만 선택하여 데이터프레임 생성   
  <조건3> 생성된 데이터프레임 대상 칼럼명 수정 : ['seoul','incheon','busan']
  <조건4> 생성된 데이터프레임 대상  index 수정 : ['male', 'female']     
  <조건5> 생성된 데이터프레임 대상 누적가로막대차트 그리기
'''

import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('C:/ITWILL/4_Python-II/data/dataset.csv')
dataset.info()

dataset['gender'].unique()
dataset['survey'].unique()
tab = pd.crosstab(dataset['gender'], dataset['survey'])
print(tab)

tab_result = tab.loc[:,[1, 3, 5]]

tab_result.columns = ['seoul','incheon','busan']
tab_result.index = ['male', 'female']

tab_result.plot(kind='barh', title='bar plot', stacked=True)


