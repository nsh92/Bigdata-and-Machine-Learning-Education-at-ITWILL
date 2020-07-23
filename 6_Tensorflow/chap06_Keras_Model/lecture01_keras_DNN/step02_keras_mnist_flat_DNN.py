# -*- coding: utf-8 -*-
"""
step02_keras_mnist_DNN.py

Tensorflow2.0 Keras + MNIST(0~9) + Flatten layer

1차 : 1차원 : 28 * 28 -> 784
2차 : 2차원 : 28 * 28 -> Flatten 적용

"""
import tensorflow as tf
from tensorflow.keras.datasets.mnist import load_data # 텐서플로우2.0의 데이터셋
from sklearn.datasets import load_iris
from tensorflow.keras.utils import to_categorical 
from tensorflow.keras import Sequential           
from tensorflow.keras.layers import Dense, Flatten        
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score

# 1. x, y 공급 data 
(x_train, y_train), (x_val, y_val) = load_data()
x_train.shape # (60000, 28, 28) # 원래는 컬러값까지 해서 한 칸 더 있는데 이건 흑백이라 없음
y_train.shape # (60000,)

# x변수 : 정규화
x_train[0] # 정규화 필요
x_train = x_train/255.
x_val = x_val/255.
'''
## 2d -> 1d
x_train = x_train.reshape(-1, 784)
x_val = x_val.reshape(-1, 784)
'''
# y변수 전처리 : one hot encoding
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_train.shape # (60000, 10)


# 2. 케라스 모델 생성
model = Sequential()
model # <tensorflow.python.keras.engine.sequential.Sequential at 0x2ac64f3c408>


# 3. model layer
'''
model.add(Dense(node수, input_shape최초투입변수 수, activation활성함수))  # hidden layer1
model.add(Dense(node수, activation활성함수))  # hidden2 ~ n
'''
input_shape = (28,28) # 2차원

## Flatten layer : 2d -> 1d
model.add(Flatten(input_shape = input_shape)) # 실질적으로 0층
# hidden layer1
model.add(Dense(128, activation='relu')) # 1층
# hidden layer2
model.add(Dense(64, activation='relu')) # 2층
# hidden layer3
model.add(Dense(32, activation='relu')) # 3층
# output layer
model.add(Dense(10, activation='softmax')) # 출력층


# 4. model compile : 학습 환경 설정
model.compile(optimizer = 'adam',                 # 최적화알고리즘
              loss='categorical_crossentropy',    # 손실
              metrics=['accuracy'])               # 평가 방법

# layer 확인
model.summary()
'''
Model: "sequential_6"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten (Flatten)            (None, 784)               0         
_________________________________________________________________
dense_16 (Dense)             (None, 128)               100480    
_________________________________________________________________
dense_17 (Dense)             (None, 64)                8256      
_________________________________________________________________
dense_18 (Dense)             (None, 32)                2080      
_________________________________________________________________
dense_19 (Dense)             (None, 10)                330       
=================================================================
Total params: 111,146
Trainable params: 111,146
Non-trainable params: 0
_________________________________________________________________'''


# 5. model training
model.fit(x=x_train, y=y_train,           
          epochs=10,
          verbose=1,
          validation_data=(x_val, y_val))


# 6. model evaluation : 모델 검증
model.evaluate(x=x_val, y=y_val)
# [0.08748876404065159, 0.9779]

























