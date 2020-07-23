# -*- coding: utf-8 -*-
"""
step05_keras_mnist_DNN_EarlyStop.py

Keras + MNIST(0~9) + Flatten layer + History + Dropout + EarlyStopping
# 에폭은 지정하나, 개선되지 않으면 알아서 조기종료 시켜라 기능
1차 : 1차원 : 28 * 28 -> 784
2차 : 2차원 : 28 * 28 -> Flatten 적용

"""
import tensorflow as tf
from tensorflow.keras.datasets.mnist import load_data
from sklearn.datasets import load_iris
from tensorflow.keras.utils import to_categorical 
from tensorflow.keras import Sequential           
from tensorflow.keras.layers import Dense, Flatten, Dropout        
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score
from tensorflow.keras.callbacks import EarlyStopping

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
Dropout(rate=0.5) # 노드 중 50% 제거
# hidden layer2
model.add(Dense(64, activation='relu')) # 2층
Dropout(rate=0.3)
# hidden layer3
model.add(Dense(32, activation='relu')) # 3층
Dropout(rate=0.3)
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
callback = EarlyStopping(monitor="val_loss", patience=2)
# 콜백 : 특정 메소드에서 또 다른 메소드를 호출기법
# 최소 2에폭은 하고 조기종료를 고려하라

model_fit = model.fit(x=x_train, y=y_train,           
                      epochs=15, # 10->15 수정 너무 작으면 차이가 미미함
                      verbose=1,
                      validation_data=(x_val, y_val),
                      callbacks=[callback]) # 조기종료


# 6. model histiory
print(model_fit.history.keys()) # dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])
train_loss = model_fit.history['loss']
train_acc = model_fit.history['accuracy']
val_loss = model_fit.history['val_loss']
val_acc = model_fit.history['val_accuracy']

# train vs val loss
import matplotlib.pyplot as plt
plt.plot(train_loss, color = 'y', label = 'train loss')
plt.plot(val_loss, color = 'r', label = 'val loss')
plt.legend(loc='best')
plt.xlabel("epochs")
plt.show()


# train vs val accuracy
plt.plot(train_acc, color = 'y', label = 'train acc')
plt.plot(val_acc, color = 'r', label = 'val acc')
plt.legend(loc='best')
plt.xlabel("epochs")
plt.show()


# 15까지 가지 않고 조기종료 됐음
# 선이 좁혀지지 않고 더 벌어지자 종료된 거임








