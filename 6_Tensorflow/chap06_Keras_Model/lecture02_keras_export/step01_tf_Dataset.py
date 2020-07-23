# -*- coding: utf-8 -*-
"""
step01_tf_Dataset.py

Dataset 클래스
 - dataset으로 부터 사용가능한 데이터를 메모리에 로딩 기능
 - batch sizee 지정 가능
"""
import tensorflow as tf
from tensorflow.python.data import Dataset

dir(Dataset) # 호출 가능한 멤버 확인
'''
batch()
from_tensor_slices()
shuffle()
'''

# 1. from_tensor_slices() 
## 입력 텐서로부터 slice 생성
## ex) MNIST(6만, 28, 28) -> 6만개 이미지를 각각 1개씩 슬라이스

## 1) x, y 변수 생성
x = tf.random.normal([5, 2])
y = tf.random.normal([5])

## 2) Dataset : 5개 slice
train_ds = Dataset.from_tensor_slices((x,y))
train_ds # ((2,), ()), types: (tf.float32, tf.float32)

## 5개 관측치 -> 5개 슬라이스
for train_x, train_y in train_ds:
    print("x = {}, y = {}".format(train_x.numpy(), train_y.numpy()))
'''
x = [2.2025957  0.79551417], y = 0.12186430394649506       x는 1차원, y는 0차원으로 출력
x = [ 0.26492685 -3.000617  ], y = 0.7401158809661865
x = [-0.545242    0.19966635], y = -0.8997529745101929
x = [-1.0785236  -0.71421874], y = -0.013430232182145119
x = [0.94405663 1.0415919 ], y = -0.40118172764778137
'''


# 2. from_tensor_slices(x, y).shuffle(buffer size).batch(size)
'''
shuffle(buffer size) : tensor 행단위 셔플링
    - buffer size : 선택된 data size
batch : model에 1회 공급할 dataset size
ex) 6만개(mnist) -> shuffle(1만).batch(100)
    1번째 slice data : 1만개 셔플링 -> 100개씩 추출
    2번째 slice data : 그다음 1만개 셔플링 -> 100개씩 추출 3번째 이후도 반복
'''

## 1) x, y 변수 생성
x2 = tf.random.normal([5, 2])
y2 = tf.random.normal([5])

## 2) Dataset : 5개 관측치, 3개의 슬라이스
train_ds2 = Dataset.from_tensor_slices((x2,y2)).shuffle(5).batch(2)
train_ds2 # ((None, 2), (None,)), types: (tf.float32, tf.float32) : 차원이 유지됨
for train_x, train_y in train_ds2:
    print("x = {}, y = {}".format(train_x.numpy(), train_y.numpy()))
'''
x = [[-1.5151623  -0.8977753 ]
 [-0.88290524 -0.3257981 ]], y = [-0.18649748  0.08860542]
x = [[-0.4744716  -0.12001058]
 [-1.0668246   0.7251385 ]], y = [ 2.2599542 -0.611284 ]
x = [[ 0.45056912 -1.7622323 ]], y = [-1.5616568]
'''


# 3. keras dataset 적용
from tensorflow.keras.datasets.cifar10 import load_data

## 1. dataset load
(x_train, y_train), (x_val, y_val) = load_data()

x_train.shape # (50000, 32, 32, 3) : (size, h, w, color)
y_train.shape # (50000, 1)

import matplotlib.pyplot as plt
plt.imshow(x_train[0])
plt.show()
y_train[0] # [6] : 10종류 중 6번 : 개구리

# batci size = 100 images
train_ds = Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(100)

cnt = 0
for image_x, label_x in train_ds:
    print("image = {}, label = {}".format(image_x.shape, label_x.shape))
    cnt += 1

print("slice 개수 =", cnt) # slice 개수 = 500
# 1epochs = iter size(500) * batch size(100)

# val set batch size = 100 image
val_ds = Dataset.from_tensor_slices((x_val, y_val)).shuffle(10000).batch(100)

cnt = 0
for image_x, label_x in val_ds:
    print("image = {}, label = {}".format(image_x.shape, label_x.shape))
    cnt += 1

print("slice 개수 =", cnt) # 100

'''
문) MNIST 데이터셋을 이용하여 train_ds, val_ds 생성하기
    train_ds : shuffle = 10,000, batch size = 32
    val_ds : batch size = 32
'''
from tensorflow.keras.datasets.mnist import load_data
(x_train, y_train), (x_val, y_val) = load_data()
train_ds = Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32)

cnt = 0
for image_x, label_x in train_ds:
    print("image = {}, label = {}".format(image_x.shape, label_x.shape))
    cnt += 1

print("slice 개수 =", cnt) # slice 개수 = 1875

val_ds = Dataset.from_tensor_slices((x_val, y_val)).shuffle(10000).batch(32)

cnt = 0
for image_x, label_x in val_ds:
    print("image = {}, label = {}".format(image_x.shape, label_x.shape))
    cnt += 1

print("slice 개수 =", cnt) # slice 개수 = 313





























