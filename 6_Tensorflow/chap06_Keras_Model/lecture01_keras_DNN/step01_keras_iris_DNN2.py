# -*- coding: utf-8 -*-
"""
step01_keras_iris_DNN2
- 텐서플로우2 케라스 + 아이리스
- 케라스 : DNN model 생성을 위한 고수준 API
- Y 변수 : ☆십진수 데이터 그대로★
    loss = 'sparse_categorical_crossentropy'
    metrics=['sparse_categorical_accuracy']
"""
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale     # x변수 전처리
from tensorflow.keras.utils import to_categorical  # y변수 전처리
from tensorflow.keras import Sequential            # 케라스 모델 생성
from tensorflow.keras.layers import Dense          # layer 생성
from tensorflow.keras.models import load_model     # model save/load

# 1. x, y 공급 data 
iris = load_iris()

# x변수 : 1 ~ 4 컬럼
x_data = iris.data
x_data = minmax_scale(x_data)

# y변수 : 5 컬럼
y_data = iris.target

x_train, x_val, y_train, y_val = train_test_split(x_data, y_data) # 75:25 기본값
print(x_train.shape) # (112, 4)


# 2. 케라스 모델 생성
model = Sequential()
model # <tensorflow.python.keras.engine.sequential.Sequential at 0x2ac64f3c408>


# 3. model layer
'''
model.add(Dense(node수, input_shape최초투입변수 수, activation활성함수))  # hidden layer1
model.add(Dense(node수, activation활성함수))  # hidden2 ~ n
'''
# hidden layer1 = [4입력, 12출력]
model.add(Dense(12, input_shape=(4,), activation='relu')) # 이전보다 코드가 간소화됨
# hidden layer2 = [12입력, 6출력]
model.add(Dense(6, activation='relu')) # 2층
# output layer = [6입력, 3출력]
model.add(Dense(3, activation='softmax')) # 출력층


# 4. model compile : 학습 환경 설정
'''
model.compile(optimizer = 'adam',                
              loss='sparse_categorical_crossentropy',   
              metrics=['sparse_categorical_accuracy']) 
'''
from tensorflow.keras import optimizers, losses, metrics
## 학습 환경 class로 변경
model.compile(optimizer = optimizers.Adam(),             
              loss = losses.SparseCategoricalCrossentropy(from_logits=True),   
              metrics= [metrics.SparseCategoricalAccuracy()]) # 해당 클래스를 임포트했으나 []처리는 필요함

# y_true : integer vs y_pred : 확률(from_logits=True)
# metrics : list type 요구
# layer 확인
model.summary()
'''
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 12)                60            
_________________________________________________________________
dense_1 (Dense)              (None, 6)                 78         
_________________________________________________________________
dense_2 (Dense)              (None, 3)                 21         
=================================================================
Total params: 159
Trainable params: 159
Non-trainable params: 0
_________________________________________________________________
'''


# 5. model training : train(112) vs val(38)
model.fit(x=x_train, y=y_train,           # 학습용
          epochs=300,
          verbose=1,
          validation_data=(x_val, y_val)) # 평가용


# 6. model evaluation : 모델 검증
model.evaluate(x=x_val, y=y_val)
# [0.5937868388075578, 0.9736842]









