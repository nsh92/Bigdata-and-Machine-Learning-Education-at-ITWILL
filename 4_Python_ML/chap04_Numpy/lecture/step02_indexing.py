# -*- coding: utf-8 -*-
"""
indexing / slicing
 - 1차원 인덱싱 : list와 동일
 - 2, 3차원 인덱싱
 - boolean 인덱싱
"""
import numpy as np

# 1. 인덱싱
'''
1차원 : obj[index]
2차원 : obj[행index, 열index]
3차원 : obj[면index, 행index, 열index]
'''
## 1) list 객체
ldata = [0,1,2,3,4,5]
ldata[:] # 전체 원소
ldata[2:] # [n:end]
ldata[:3] # [~:n]
ldata[-1] # 5

## 2) numpy 객체
arr1d = np.array(ldata)
arr1d.shape # (6,)
arr1d[2:]
arr1d[:3]
arr1d[-1] 
## 1차원까지는 리스트와 동일


# 2. 슬라이싱
arr = np.array(range(1,11)) 
arr # array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]) # 원본

arr_sl = arr[4:8] # 10개 중 해당하는 것만 잘라내기
arr_sl # array([5, 6, 7, 8])                          # 사본

## 블록 수정 : 싸그리 바꾸기 : 리스트에선 불가
arr_sl[:] = 50
arr_sl # array([50, 50, 50, 50])                      # 사본을 수정

arr # array([ 1,  2,  3,  4, 50, 50, 50, 50,  9, 10]) # 사본에 수정된 것이 원본에 반영됨


# 3. 2, 3차 인덱싱
arr2d = np.array([[1,2,3],[2,3,4],[3,4,5]])
arr2d.shape # (3,3)
arr2d
'''
array([[1, 2, 3],
       [2, 3, 4],
       [3, 4, 5]])
'''

# 행 index : default
arr2d[1]    # arr2d[1,:]  : array([2, 3, 4])
arr2d[1:]   # 2~3행
arr2d[:,1:] # 2~3열
arr2d[2,1]  # 3행 2열

arr2d[:2,1:] # 박스 선택

# [면 행 열] : 면index : default
arr3d = np.array([ [[1,2,3],[2,3,4],[3,4,5]], [[2,3,4],[3,4,5],[6,7,8]] ])
'''
array([[[1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]],

       [[2, 3, 4],
        [3, 4, 5],
        [6, 7, 8]]])
'''
arr3d.shape # (2, 3, 3)
arr3d[0]  # 1면에 대한 데이터
arr3d[1]

# 면 -> 행 index
arr3d[0, 2] # [3, 4, 5]

# 면 -> 행 -> 열 index
arr3d[1, 2, 2] # 8 : 두번째 면의 3행의 3열

arr3d[1,1:,1:] # 박스 선택


# 4. boolean indexing
dataset = np.random.randint(1, 10, size=100)
len(dataset)  # 100
dataset

## 5 이상
dataset2 = dataset[dataset >= 5]
len(dataset2)  # 54
## 이렇게 조건식으로 정하는 것을 부울리언 인덱싱이라 함

## 5~8 자료 선택
dataset2 = dataset[dataset >= 5 and data <=8] # 오류 발생
# 단순 관계식까지만 가능하고 저렇게 논리식을 추가해봤자 안된다
# 이래서 넘파이는 논리식을 쓸 수 있는 대안을 제시함
# np.logical_and
# np.logical_or
# np.logical_not
dataset2 = dataset[np.logical_and(dataset >=5, dataset <=8)]
dataset2

# 3장 연습문제3 참










