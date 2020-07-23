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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale    
from tensorflow.keras.utils import to_categorical 
from tensorflow.keras import Sequential           
from tensorflow.keras.layers import Dense        
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score

# 1. x, y 공급 data 
(x_train, y_train), (x_val, y_val) = load_data()
x_train.shape # (60000, 28, 28)
y_train.shape # (60000,)

# x변수 : 정규화
x_train[0] # 정규화 필요
x_train = x_train/255.
x_val = x_val/255.
## 2d -> 1d
x_train = x_train.reshape(-1, 784)
x_val = x_val.reshape(-1, 784)

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
# hidden layer1 = [784입력, 128츨력]
model.add(Dense(128, input_shape=(784,), activation='relu')) # 1층
# hidden layer2 = [128입력, 64출력]
model.add(Dense(64, activation='relu')) # 2층
# hidden layer3 = [64입력, 32출력]
model.add(Dense(32, activation='relu')) # 3층
# output layer = [32입력, 10출력]
model.add(Dense(10, activation='softmax')) # 출력층


# 4. model compile : 학습 환경 설정
model.compile(optimizer = 'adam',                 # 최적화알고리즘
              loss='categorical_crossentropy',    # 손실
              metrics=['accuracy'])               # 평가 방법

# layer 확인
model.summary()
'''
Model: "sequential_5"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_12 (Dense)             (None, 128)               100480    
_________________________________________________________________
dense_13 (Dense)             (None, 64)                8256      
_________________________________________________________________
dense_14 (Dense)             (None, 32)                2080      
_________________________________________________________________
dense_15 (Dense)             (None, 10)                330       
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
# [0.09309118615567595, 0.978]

# 7. model save / load
model.save("keras_model_mnist.h5")
print("saved")

new_model = load_model("keras_model_mnist.h5")


# 8. loaded model test : new dataset
y_pred = new_model.predict(x_val) # 예측치
y_true = y_val
y_pred = tf.argmax(y_pred, axis=1)
y_true = tf.argmax(y_true, axis=1)

acc = accuracy_score(y_true, y_pred)
print(acc) # 0.978

























