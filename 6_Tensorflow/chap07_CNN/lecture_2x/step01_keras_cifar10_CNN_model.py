# -*- coding: utf-8 -*-
"""
step01_keras_cifar10_CNN_model.py
- keras CNN model + cifar10

1. 이미지 데이터셋 로드
2. 이미지 전처리 : 실수형, 정규화, one-hot encoding
3. 케라스 모델
4. 모델 평가
5. 모델 히스토리
"""
import tensorflow as tf
from tensorflow.keras.datasets.cifar10 import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Flatten, Dropout
import time

start_time = time.time()

# 1. dataset load
(x_train, y_train), (x_val, y_val) = load_data()

x_train.shape # (50000, 32, 32, 3) : (size, h, w, color)
y_train.shape # (50000, 1)

# image 전처리 : 실수형 -> 정규화
x_train[0] # 0~255 확인
x_train = x_train.astype("float32")
x_val = x_val.astype("float32")

# 정규화
x_train = x_train / 255
x_val = x_val / 255
x_train[0]

# label 전처리 : one-hot
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)


# 2. keras CNN model layer
model = Sequential()
input_shape = (32, 32, 3)

# conv layer1
# [5, 5, 3, 32] 커널사이즈 -> 필터
model.add(Conv2D(32, kernel_size=(5,5), input_shape = input_shape, 
                 activation="relu"))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2)))
model.add(Dropout(0.2))

# conv layer2
# [5, 5, 3, 64]
model.add(Conv2D(64, kernel_size=(5,5), activation="relu"))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2)))
model.add(Dropout(0.2))

# Flatten layer : 3d -> 1d 알아서 해줌
model.add(Flatten())

# DNN hidden layer
model.add(Dense(64, activation = "relu"))

# DNN output layer
model.add(Dense(10, activation = "softmax"))

## 6장 1강 step2에서 퍼옴
# 4. model compile 
model.compile(optimizer = 'adam',                 # 최적화알고리즘
              loss='categorical_crossentropy',    # 손실
              metrics=['accuracy'])               # 평가 방법

model.summary()

# 5. model training
model_fit = model.fit(x=x_train, y=y_train,           
                      batch_size=100,
                      epochs=10,
                      verbose=1,
                      validation_data=(x_val, y_val))


# 6. model evaluation : 모델 검증
loss, acc = model.evaluate(x=x_val, y=y_val)
# loss: 0.8285 - accuracy: 0.6630
print('loss = {}, accuracy = {}'.format(loss,acc))
# loss = 0.9686919748306274, accuracy = 0.6629999876022339


# 6. model history
print(model_fit.history.keys())

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

# 7.model test(new dataset)
from sklearn.metrics import classification_report
import numpy as np

labels = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

idx = np.random.choice(a=x_val.shape[0], size=100, replace=False)
x_test = x_val[idx]
y_test = y_val[idx]

y_pred = model.predict(x_test)
y_true = y_test

y_pred = np.argmax(y_pred, axis = 1)
y_true = np.argmax(y_true, axis = 1)
report = classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.82      0.75      0.78        12
           1       0.71      0.83      0.77         6
           2       0.80      0.44      0.57         9
           3       0.43      0.33      0.38         9
           4       0.64      0.82      0.72        11
           5       0.38      0.45      0.42        11
           6       1.00      1.00      1.00         8
           7       0.78      0.82      0.80        17
           8       0.85      0.92      0.88        12
           9       1.00      0.80      0.89         5

    accuracy                           0.72       100
   macro avg       0.74      0.72      0.72       100
weighted avg       0.73      0.72      0.72       100
'''

# 성공여부
for i in range(100):
    if y_true[i] == y_pred[i]:
        print("success :", labels[y_pred[i]])
    else:
        print("fail : real({}) -> pred({})".format(labels[y_true[i]],
                                                   labels[y_pred[i]]))

end_time = time.time() = start_time
print("소요 시간 :", end_time)
















