# -*- coding: utf-8 -*-
"""
matplotlib API 사용 차트 그리기
 형식) plt.plot(data) ; plt.show()

 1. 기본 차트 그리기 : plt.plot()
 2. 산점도 그리기    : plt.scatter()  # 막대는 bar, 파이는 pie
 3. subplot 이용 차트 그리기
"""
import matplotlib.pyplot as plt  # plt별칭
# 차트에서 한글 지원 # data폴더의 한글차트.txt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd  # 파일을 읽기 위함

import numpy as np   # 숫자 데이터 생성


# 1. 기본차트 그리기
help(plt.plot)
'''
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # ditto, but with red plusses
'''

## 기본
data = np.arange(10)  # 0~9 생성
plt.plot(data, 'r+') # 저 마킹 지정이 없으면 걍 라인 차트임
plt.show()

## 표준정규분포
data2 = np.random.randn(10)  # 저 갯수만큼 표준정규분포를 따르는 난수 생성
plt.plot(data, data2)
plt.show()

## 산점도
plt.plot(data, data2, 'ro')  # (마킹)점 와꾸 선택
plt.show()

## 그니까 라인 그리는 것이 기본설정이고 저렇게 bo니 r+니 하면 산점도가 되는 거임


# 2. 산점도 그리는 별도의 함수
## 단색
plt.scatter(data, data2, c='r', marker='o')
# r과 o는 약속된 기호고 자세한 내용은 help를 참고
plt.show()

## 각각 혹은 군집에 따른 채색을 다르게 하고 싶다
cdata = np.random.randint(1,4,10)  # 1~3 난수 정수 생성
cdata # 색깔 지정을 위한 숫자를 생성함
plt.scatter(data, data2, c=cdata, marker='o')
plt.show()


# 3. 격자 형식 차트 : subplot
## 칸을 나누고 각 칸에 다른 차트를 그리고자 한다
## 객체 생성
fig = plt.figure(figsize = (5, 3))  # 차트 크기 4칸 밭전 모양
x1 = fig.add_subplot(2,2,1)
x2 = fig.add_subplot(2,2,2)
x3 = fig.add_subplot(2,2,3)
x4 = fig.add_subplot(2,2,4)
## x1에 차트를 그려넣으면 저 칸에 들어간다

## 데이터 생성
data3 = np.random.randint(1,100, 100)
data4 = np.random.randint(10,110, 100)
cdata = np.random.randint(1,4,100)

## 첫번째 격자 : 히스토그램
x1.hist(data3)

## 두번째 격자 : 산점도
x2.scatter(data3, data4, c=cdata)

## 세번째 격자 : 선 그래프
x3.plot(data3)

## 네번째 격자
x4.plot(data4, 'g--') # 초록색, 점선 표시
plt.show()


# 4. 차트 크기 지정, 두 개 이상 차트 그리기
fig = plt.figure(figsize=(12,5))
chart = fig.add_subplot()  # (1,1,1)이 기본값

## 계단형 차트
chart.plot(data, color='r', label='step', drawstyle='steps-post')

## 선 스타일 차트
chart.plot(data2, color='b', label='line')

## 차트 제목
plt.title('계단형  vs  선 스타일')
plt.xlabel('데이터')
plt.ylabel('난수 정수')
plt.legend(loc='best') # 범례추가, 알아서 적당한 곳에 배치하라
plt.show()

#### 연습문제 1번 ####

dir(chart)  # chart의 멤버들
'''
'bar'
'barh'
'boxplot'
'hist'
'pie'
'scatter'
'''

# 5. 막대차트
fig2 = plt.figure()

chart2 = fig2.add_subplot()

data = [127, 90, 202, 150, 250]
idx = range(len(data))  # 0 ~ 4
chart2.bar(idx, data, color='darkblue')

## 막대차트 레이블 추가
x_label = ['서울', '대전', '부산', '광주', '인천']
plt.xticks(idx, x_label)

plt.xlabel('판매 지역')
plt.ylabel('지역별 매출현황')
plt.title('2020년 1분기 지역별 판매현황')
plt.show()




