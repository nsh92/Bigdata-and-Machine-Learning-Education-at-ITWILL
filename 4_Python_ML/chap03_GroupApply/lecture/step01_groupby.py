# -*- coding: utf-8 -*-
"""
DataFrame 객체 대상 그룹화
- 형식 ) Df.groupby('집단변수').수학통계함수()
"""
import pandas as pd

tips = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\tips.csv")
tips.info()
tips.head()

# 팁 비율 : 파생변수
tips['tip_pct'] = tips['tip']/tips['total_bill'] 
tips.info()
tips.head()

# 변수 복제 # sex 칼럼 이름을 gender로 바꾸려고 함
tips['gender'] = tips['sex']

# 변수 제거
del tips['sex']
tips.head()

# 1. 집단변수 1개 -> 전체 컬럼 그룹화
gender_grp = tips.groupby('gender')
gender_grp # DataFrameGroupBy object

## 그룹객체.함수()
gender_grp.size()  # 빈도수 확인
# Female     87
# Male      157

## 그룹 통계량
gender_grp.sum()  # 숫자변수만 연산
'''
        total_bill     tip  size    tip_pct
gender                                     
Female     1570.95  246.51   214  14.484694
Male       3256.82  485.07   413  24.751136
'''
gender_grp.mean()

dir(gender_grp)  # gender_grp에 대하여 호출가능한 멤버들 목록 주루룩

## 그룹별 요약통계량
gender_grp.describe()  # 수치 제공
gender_grp.boxplot()   # 그래프 제공


# 2. 집단변수 1개(smoker) -> 특정 칼럼 그룹화(tip)
smoker_grp = tips['tip'].groupby(tips['smoker'])
smoker_grp.size()
## No     151
## Yes     93

smoker_grp.mean()
## No     2.991854
## Yes    3.008710


# 3. 집단변수 2개 -> 전체 컬럼 그룹화
# 형식) DF.groupby(['컬럼1', '컬럼2']) # 1차그루핑 : 컬럼1, 2차 : 컬럼2
gender_smoker_grp = tips.groupby([tips['gender'], tips['smoker']])
gender_smoker_grp.size()
'''
gender  smoker
Female  No        54
        Yes       33
Male    No        97
        Yes       60
'''

## 특정 변수 통계량
gender_smoker_grp.describe() # 뭐가 막 많음 : gsd 참고
gender_smoker_grp['tip'].describe() # 특정 변수를 정함
'''
               count      mean       std   min  25%   50%     75%   max
gender smoker                                                          
Female No       54.0  2.773519  1.128425  1.00  2.0  2.68  3.4375   5.2
       Yes      33.0  2.931515  1.219916  1.00  2.0  2.88  3.5000   6.5
Male   No       97.0  3.113402  1.489559  1.25  2.0  2.74  3.7100   9.0
       Yes      60.0  3.051167  1.500120  1.00  2.0  3.00  3.8200  10.0
[해설] 여성은 흡연자, 남성은 비흡연자가 팁 지불에 후하다
'''
gsd = gender_smoker_grp.describe()


# 4. 집단변수 2개 -> 특정 컬럼 그룹화
gender_smoker_tip_grp = tips['tip'].groupby([tips['gender'], tips['smoker']])

gender_smoker_tip_grp.size()
'''
Female  No        54
        Yes       33
Male    No        97
        Yes       60
'''
gender_smoker_tip_grp.size().shape # (4,) : 1차원

## 각 집단별 tip 합
gender_smoker_tip_grp.sum()
'''
Female  No        149.77
        Yes        96.74
Male    No        302.00
        Yes       183.07
'''
gender_smoker_tip_grp.sum().shape # (4,) : 1차원

## 저 1차원들을 2차원으로 보내고 싶다
gender_smoker_tip_grp.sum().unstack() 
'''
smoker      No     Yes
gender                
Female  149.77   96.74
Male    302.00  183.07
'''
gender_smoker_tip_grp.sum().unstack().shape # (2, 2) : 2차원

## unstack이 아닌, stack으로 쓰면 반대 개념으로 돌아감
grp_2d = gender_smoker_tip_grp.sum().unstack()
grp_1d = grp_2d.stack()
'''
Female  No        149.77
        Yes        96.74
Male    No        302.00
        Yes       183.07
'''

grp_2d ## 성별vs흡연유무 : 교차분할표(합계)인 셈

## 성별 흡연유무 - 교차분할표(빈도수)
grp_2d_size = gender_smoker_tip_grp.size().unstack()
'''
smoker  No  Yes
gender         
Female  54   33
Male    97   60
'''


# 연습문제 1번 ㄱ


# 아이리스로 복습
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")

iris_grp = iris.groupby('Species')
iris_grp_sum = iris_grp.sum()
print(iris_grp_sum)

iris_grp2 = iris['Sepal.Length'].groupby(iris['Species'])
iris_grp2.sum()




























