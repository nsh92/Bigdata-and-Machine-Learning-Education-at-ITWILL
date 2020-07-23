'''   
문5) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd

iris = pd.read_csv('C:/ITWILL/4_Python-II/data/iris.csv')
print(iris.info())
col1 = iris['Sepal.Length']
col2 = iris['Sepal.Width']
col3 = iris['Petal.Length']
col4 = iris['Petal.Width']

print('합계=', col1.sum())
print('평균=', col1.mean())
print('표준편차=', col1.std())
print('합계=', col4.sum())
print('평균=', col4.mean())
print('표준편차=', col4.std())

df1 = pd.concat([col1, col2], axis = 1)
df2 = pd.concat([col3, col4], axis = 1)

iris_df = pd.concat([df1, df2], axis = 1)
iris_df.info()
