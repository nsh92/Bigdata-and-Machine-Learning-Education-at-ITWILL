# -*- coding: utf-8 -*-
"""
1. image shape : 3차원(세로,가로,컬러)
2. reshape : size 변경은 안됨
   ex) (2, 5) -> (5, 2) 가능, (3, 4) -> (4, 2) 불가능
"""
import numpy as np
from matplotlib.image import imread # 이미지 읽어오는 함수
imread("C:/ITWILL/4_Python-II/workspace/chap04_numpy/images/test1.jpg")
import matplotlib.pylab as plt


# 1. image shape
file_path = './images/test1.jpg'
image = imread(file_path)
type(image) # numpy.ndarray 넘파이객체

image.shape # (360, 540, 3) 세로크기, 가로크기, 3원색
print(image) # 0~255 색상값

plt.imshow(image) 

## RGB 색상 분류
#[128 113  94]
#  R   G    B
r = image[:,:,0] # R
g = image[:,:,1] # G
b = image[:,:,2] # B
r.shape # (360, 540)
g.shape
b.shape

plt.imshow(r) 
plt.imshow(g) 
plt.imshow(b) 


# 2. image data reshape
from sklearn.datasets import load_digits # 데이터셋 제공

digit = load_digits()
digit.DESCR # 데이터셋 설명 보기

X = digit.data    # x변수(입력변수 : 이미지)
y = digit.target  # y변수(정답 : 정수)
X.shape # (1797, 64) = 8*8 2차원으로 reshape할 예정
y.shape # (1797,)

img_0 = X[0].reshape(8,8) # 행 인덱스 
img_0 # 64개의 한 줄의 벡터를 8,8 2차원으로
plt.imshow(img_0)
y[0] # 0 반환

X_3d = X.reshape(-1, 8, 8) # 2차원을 3차원으로
X_3d.shape # (1797, 8, 8) : (전체이미지, 세로, 가로, 컬러) 4차원 # 끝에 , 3이 없으므로 흑백인듯

# (1797, 8, 8, 1)
X_4d = X_3d[:,:,:,np.newaxis] # 4번축 새로 추가
X_4d.shape # (1797, 8, 8, 1)


# 3. reshape
'''
전치행렬 : T
swapaxis = 전치행렬
transpose() : 3차원 이상 모양 변경
'''
## 1) 전치행렬
data = np.arange(10).reshape(2,5)  # 10짜리 벡터를 2,5 행렬로
data
'''
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
'''
print(data.T)
'''
[[0 5]
 [1 6]
 [2 7]
 [3 8]
 [4 9]]
'''

## 2) transpose()
'''
1차원 : 효과 없음
2차원 : 전치행렬 동일함
3차원 : (0,1,2) -> (2,1,0) 축의 위치 변경
'''
arr3d = np.arange(1,25).reshape(4,2,3)
arr3d.shape # (4, 2, 3)
arr3d

## (0,1,2) -> (2,1,0) 축의 위치 변경
arr3d_tran = arr3d.transpose(2,1,0) # 2,1,0 이건 걍 디폴트
arr3d_tran.shape # (3, 2, 4)
arr3d_tran

## (0,1,2) -> (1,2,0)
arr3d_tran = arr3d.transpose(1,2,0)
arr3d_tran.shape # (2, 3, 4)
arr3d_tran









