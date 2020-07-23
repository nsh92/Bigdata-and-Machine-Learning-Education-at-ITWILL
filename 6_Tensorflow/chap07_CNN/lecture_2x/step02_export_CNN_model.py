# -*- coding: utf-8 -*-
"""
step02_export_CNN_model.py
텐서플로우2 전문가용 CNN model 구축
    - tensorflow2.0 저수준 API
    - Dataset 클래스 이용 : 공급 data 생성
    - 순방향 step : 회귀방정식 연산 -> 예측치 -> loss
    - 역방향 step : 자동 미분계수 계산 -> w, b 업데이트(모델 최적화)
    - 손실함수, 최적화, 모델평가 API
"""
import tensorflow as tf
from tensorflow.python.data import Dataset
from tensorflow.keras.layers import Conv2D, MaxPooling2D  # CNN layer
from tensorflow.keras.layers import Dense, Flatten        # DNN layer
from tensorflow.keras import optimizers, losses, metrics
from tensorflow.keras import datasets 

# 1. dataset load
mnist = datasets.mnist
(x_train, y_train), (x_val, y_val)= mnist.load_data()
x_train.shape # (60000, 28, 28)
y_train.shape # (60000,)


## images 2d -> 3d
x_train = x_train.reshape(-1, 28, 28, 1) # (60000, 28, 28, 1)
x_val = x_val.reshape(-1, 28, 28, 1)     # (10000, 28, 28, 1)
x_train.shape
x_val.shape

## 정규화
x_train = x_train/255.
x_val = x_val/255.

## labels
y_train[0] # 5 : integer


# 2. Dataset 생성
train_ds = Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32)
train_ds # ((None, 784), (None,)), types: (tf.float64, tf.uint8)
test_ds = Dataset.from_tensor_slices((x_val, y_val)).batch(32)
test_ds  # ((None, 784), (None,)), types: (tf.float64, tf.uint8)


input_shape = (28,28,1)

# 3. 순방향 step : 연산 -> (예측치vs관측치) -> 손실
class Model(tf.keras.Model): # chap4-lecture2-step2에 해놓은 클래스
    def __init__(self):      
        super().__init__()
        # w, b 자동 생성(자동 초기화)이라 지움
        # self.W = tf.Variable(tf.random.normal([2, 3])) 
        # self.B = tf.Variable(tf.random.normal([3])) 
        
        # CNN layer 설계
        self.conv2d = Conv2D(32, kernel_size=(5,5), activation="relu")
        self.pool = MaxPooling2D(pool_size=(3,3), strides=(2,2))
        self.flatten = Flatten() # flatten : 3d image -> 1d image
        self.d1 = Dense(128, activation='relu') # hidden layer1
        self.d2 = Dense(64, activation='relu') # hidden layer2
        self.d3 = Dense(10, activation='softmax') # output layer
        
    def call(self, inputs):  # 메소드 재정의
        # 회귀방정식 생략
        x = self.conv2d(inputs)
        x = self.pool(x)
        x = self.flatten(x)
        x = self.d1(x)
        x = self.d2(x)
        return self.d3(x)    # 예측치(확률) 반환


# 4. loss function : 손실 함수 : 오차 반환
loss = losses.SparseCategoricalCrossentropy(from_logits = True)        
# y_true(integer) vs y_pred(prop) : from_logits = True
## 정수 vs 확률값인데 저 설정으로 비교 가능해짐

import numpy as np
# 손실이 작은 경우
y_true = np.array([0, 2]) # 정답 : 10진수
y_pred = np.array([[0.9, 0.02, 0.08],[0.1, 0.1, 0.8]]) # 예측치 확률
loss(y_true, y_pred).numpy() # 손실함수 0.6538635492324829

# 손실이 큰 경우
y_true = np.array([0, 1]) # 정답 : 10진수
y_pred = np.array([[0.9, 0.02, 0.08],[0.1, 0.1, 0.8]]) # 예측치 확률
loss(y_true, y_pred).numpy() # 1.0038635730743408 : 차이가 클수록 손실값이 커진다


# 5. model & optimizer
model = Model()
optimizer = optimizers.Adam()


# 6. 모델 평가 : loss, accuracy -> 1epoch 단위
train_loss = metrics.Mean() # loss mean
train_acc = metrics.SparseCategoricalAccuracy()

val_loss = metrics.Mean()
val_acc = metrics.SparseCategoricalAccuracy()


# 7. 역방향 step : 자동 미분계수 계산 -> w, b 업데이트
@tf.function # 연산 속도 향상 목적
def train_step(images, labels):
    with tf.GradientTape() as tape:
        # 1) 순방향 : loss 계산
        preds = model(images) # model.call(images) : 예측치를 받음
        loss_value = loss(labels, preds) # 손실함수(y_true, y_pred)
        
        # 2) 역방향 : 손실값 -> w,b update
        grad = tape.gradient(loss_value, model.trainable_variables) # [model.W, model.B]
        # 모델 최적화 : 기울기 -> 최적화 객체 반영
        optimizer.apply_gradients(zip(grad, model.trainable_variables))
        
        # 3) 1epoch -> loss, accuracy save
        train_loss(loss_value) # loss mean
        train_acc(labels, preds) # accuracy
        

@tf.function # 연산 속도 향상 목적
def test_step(images, labels):  # 최적화된 것이 맞는지 확인하는 게 목적이라 역방향이 필요 없지
    # 1) 순방향 : loss 계산
    preds = model(images) # model.call(images) : 예측치를 받음
    loss_value = loss(labels, preds) # 손실함수(y_true, y_pred)
        
    # 2) 역방향 : 없음
        
    # 3) 1epoch -> loss, accuracy save
    val_loss(loss_value) # loss mean
    val_acc(labels, preds) # accuracy


# 8. model training
epochs = 10
for epoch in range(epochs): # 10번
    # next epoch
    train_loss.reset_states()
    train_acc.reset_states()
    val_loss.reset_states()
    val_acc.reset_states()
    
    # model train
    for images, labels in train_ds:
        train_step(images, labels)
    
    # model val
    for images, labels in test_ds:
        test_step(images, labels)
        
    form = "epoch = {}, Train loss = {:.6f}, Train Acc = {:.6f}, Val loss = {:.6f}, Val acc = {:.6f}"
    print(form.format(epoch+1, train_loss.result(),
                      train_acc.result(),
                      val_loss.result(),
                      val_acc.result()))

# epoch = 10, Train loss = 1.470951, Train Acc = 0.990217, Val loss = 1.475232, Val acc = 0.985600
