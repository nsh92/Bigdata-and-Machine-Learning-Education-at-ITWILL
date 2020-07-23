# -*- coding: utf-8 -*-
"""
Numpy 패키지 특징
 - 선형대수(벡터, 행렬) 연산 관련 함수 제공
 - list보다 이점 : N차원 배열 생성, 선형대수 연산, 고속 처리
 - Series와 공통점 
   -> 수학/통계 함수 지원
       ex) obj.수학통계()
   -> 범위수정, 블록연산, 
   -> 인덱싱/슬라이싱
 - 주요 모듈과 함수
   1. random : 난수 생성
   2. array 함수 : N차원 배열 생성(array([list])) :[]의 수가 차원의 수
   3. 샘플링 함수
   4. arrange : range()와 유사
 - 참고 사이트 : http://www.scipy.org
"""
import numpy as np

# 리스트 자료 구조
lst = [1,2,3]
lst # [1, 2, 3]
lst**2 # 불가능 : 리스트는 선형대수가 불가능하다
# 굳이 되게 하려면
for i in lst:
    print(i**2)

# 저런 리스트를 넘파이로 가져와보자
arr = np.array(lst)
arr # array([1, 2, 3]) : lst와 모양은 비슷하나 연산에서 달라진다
arr ** 2 # array([1, 4, 9], dtype=int32)

# 동일 type
arr = np.array([1,'two',3])
arr # array(['1', 'two', '3'], dtype='<U11')
# type을 일관되게 가져간다

arr = np.array([[1,'two',3]])
arr # array([['1', 'two', '3']], dtype='<U11')
arr.shape # (1, 3) : 2차원


# 1. random : 난수 생성 함수
np.random.randn() # 모듈.모듈.정규분포난수함수()
data = np.random.randn(3, 4) # 3행 4열 2차원 및 12개 난수 만들자
'''
array([[ 2.90121287, -0.29300334,  2.12537649,  0.81951342],
       [ 0.61230505,  1.08946795,  0.12844334, -0.16814253],
       [ 0.39419075,  0.57567543,  2.04627998,  0.7528884 ]])
대가로 중첩 : 2차원, 줄 : 행, 칸 : 열
'''

for row in data:
    print('행 단위 합계 :', row.sum())
    print('행 단위 평균 :', row.mean())

## 1) 수학 / 통계 함수 지원
type(data)  # numpy.ndarray : 넘파이 객체다 : 수학이나 통계함수를 붙일 수 있다
print('전체 합 :', data.sum())
print('전체 평균 :', data.mean())
print('전체 분산 :', data.var())
print('전체 표준편차 :', data.std())

dir(data)
data.shape # (3, 4)
data.size  # 12

## 2) 범위 수정, 블록 연산
data + data
data - data

## 3) 인덱싱 : R과 유사 : 판다스에 비해 쉬움
data[0,0] # 2.9012128683156555 1행1열
data[0,:] # 1행 전체
data[:,1] # 2열 전체


# 2. array 함수
## 1) 단일 리스트
lst1 = [3, 5.6, 4, 7, 8]
lst1 # 원소 5개의 단일 리스트
## 리스트를 넘파이로
arr1 = np.array(lst1)
arr1 # array([3. , 5.6, 4. , 7. , 8. ])
arr1.var()
arr1.std()
## 어레이로 만들면 수치 연산 멤버를 부름으로써 쉽게 계산할 수 있다

## 2) 중첩 리스트
lst2 = [[1,2,3,4,5], [2,3,4,5,6]]
lst2
lst2[0][2] # 첫 리스트(1~5)의 3을 조회함

arr2 = np.array(lst2)
arr2
#array([[1, 2, 3, 4, 5],
#       [2, 3, 4, 5, 6]]) 행렬구조로 출력 : 중첩이다 : 2차원으로 인식
arr2.shape # (2, 5)
arr2[0,2] # = lst2[0][2] : 3

## 2차원index : obj[행번호, 열번호]
arr2[1,:] # 2행 다
arr2[:,1] # 2열 다
arr2[:,2:4] # 박스형 선택 (콜론 뒷번호는 0부터 시작하지 않나봄)

## broadcast 연산
## - 작은 차원이 큰 차원으로 늘어난 후 연산을 수행
## 1) 스칼라 vs 벡터
0.5 * arr1  # array([1.5, 2.8, 2. , 3.5, 4. ])
# 스칼라가 각 원소에 대하여 곱해졌음
# = 스칼라가 arr1만큼 차원이 늘려졌음

## 2) 스칼라 vs 매트릭스
0.5 * arr2
# 위와 같은 논리

## 3) 벡터 vs 매트릭스
print(arr1.shape, arr2.shape) # (5,) (2, 5)
arr3 = arr1 + arr2
print(arr3)
#[[ 4.   7.6  7.  11.  13. ]
# [ 5.   8.6  8.  12.  14. ]]
# 벡터가 한 줄 늘려져서 각 위치에 연산됨
arr4 = arr1 * arr2


# 3. sampling 함수
num = list(range(1,11))
help(np.random.choice)
'''
choice(a, size=None, replace=True, p=None)
a : 관측치 길이
size : 임의 추출 길이
replace : 복원(T) 비복원(F) 여부
p : 꺼내질 확률
'''
idx = np.random.choice(a=len(num), size=5, replace=False) # 모듈.모듈.함수()
idx # array([7, 9, 5, 8, 2]) 5개를 랜덤하게 추출

import pandas as pd
score = pd.read_csv('C:/ITWILL/4_Python-II/data/score_iq.csv')
score.info()
len(score)
idx = np.random.choice(a=len(score), size=int(len(score)*0.3), replace=False)
len(idx)

# 판다스 DF 인덱스
score_train = score.iloc[idx,:]
score_train.shape # (45, 6)

# pandas(DF) -> numpy(array)
score_arr = np.array(score)
score_arr.shape # (150, 6)
score_train2 = score_arr[idx,:]
score_train2.shape # (45, 6)


# 4. arange 함수
zero_arr = np.zeros((3,5)) # 제로행렬 : 원소들이 다 0
'''
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
'''
cnt = 1
for i in range(3):      # 행 인덱스
    for j in range(5):  # 열 인덱스
       zero_arr[i, j] = cnt
       cnt += 1

zero_arr
'''
array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.]])
'''
# 근대 저 range() 대신에 arange()를
cnt = 1
for i in np.arange(3):      # 행 인덱스
    for j in np.arange(5):  # 열 인덱스
       zero_arr[i, j] = cnt
       cnt += 1
zero_arr
'''
array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.]])
같은 결과
근대 range()의 경우 음수 삽입 불가능해서 arange를 씀
'''
range(-1.0, 2, 0.1)      # 안됨
np.arange(-1.0, 2, 0.1)  # 됨
























