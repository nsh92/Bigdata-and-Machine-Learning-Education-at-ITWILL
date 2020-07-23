# -*- coding: utf-8 -*-
"""
step02_celeb_crop_data_CNN_model.py
1. file load
2. CNN layer
3. CNN model
4. CNN model save
"""
import tensorflow as tf
from tensorflow.keras.datasets.cifar10 import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Flatten, Dropout
import numpy as np
## 7장 lecture2 step1 퍼옴

# 1. file load
# 현재위치 lecture03
x_train, y_train, x_val, y_val = np.load(file="./create_file/image_train_val.npy", allow_pickle=True)

x_train.shape # (740, 150, 150, 3)
y_train.shape # (740, 5)
x_val.shape   # (250, 150, 150, 3)


# 2. keras CNN model layer
model = Sequential()
input_shape = (150, 150, 3)

# conv layer1
model.add(Conv2D(32, kernel_size=(5,5), input_shape = input_shape, 
                 activation="relu"))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2)))

# conv layer2
model.add(Conv2D(64, kernel_size=(5,5), activation="relu"))
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2)))

# Flatten layer : 3d -> 1d 알아서 해줌
model.add(Flatten())

# DNN hidden layer
model.add(Dense(256, activation = "relu"))

# DNN output layer
model.add(Dense(5, activation = "softmax"))


# 4. model compile 
model.compile(optimizer = 'adam',                 # 최적화알고리즘
              loss='categorical_crossentropy',    # 손실
              metrics=['accuracy'])               # 평가 방법

model.summary()


# 5. model training (양이 많지 않아서 batch size 제외)
model_fit = model.fit(x=x_train, y=y_train,           
                      epochs=15,
                      verbose=1,
                      validation_data=(x_val, y_val))


# 6. model evaluation : 모델 검증
loss, acc = model.evaluate(x=x_val, y=y_val)
print('loss = {}, accuracy = {}'.format(loss,acc))
# loss = 0.4075018733739853, accuracy = 0.9039999842643738

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


# 7. model save
model.save("./create_file/celab_CNN_model.h5")
