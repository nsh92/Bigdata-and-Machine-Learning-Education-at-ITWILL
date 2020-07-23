# -*- coding: utf-8 -*-
"""
피벗테이블(pivot table)
- 사용자가 행, 열 그리고 교차셀에 변수를 지정하여 테이블 생성
"""
import pandas as pd
pivot_data = pd.read_csv('C:/ITWILL/4_Python-II/data/pivot_data.csv')
pivot_data.info()
'''
교차셀 : 매출액(price)         : 숫자변수이어야 함
행 : 연도(year), 분기(quarter) : 집단변수이어야 함
열 : 매출규모(size)            : 집단변수이어야 함
셀에 적용할 통계 : sum
'''
ptable = pd.pivot_table(pivot_data, values = 'price',
               index = ['year', 'quarter'],
               columns = 'size',
               aggfunc = 'sum')
ptable
'''
size          LARGE  SMALL
year quarter              
2016 1Q        2000   1000
     2Q        2500   1200
2017 3Q        2200   1300
     4Q        2800   2300
'''

ptable.shape  # (4, 2) : 2차원
ptable.plot(kind='barh')
ptable.plot(kind='barh', stacked=True)


movie = pd.read_csv('C:/ITWILL/4_Python-II/data/movie_rating.csv')
# 행 : 평가자
# 열 : 영화 제목
# 셀 : 평점
# 함수 : sum
# 피벗테이블 만들기
movie.info()

pi_mov = pd.pivot_table(movie, values='rating',
                        index='critic',
                        columns='title',
                        aggfunc='sum')
pi_mov

# 축 평균
pi_mov.mean(axis = 1) # 행단위
pi_mov.mean(axis = 0) # 열단위

































