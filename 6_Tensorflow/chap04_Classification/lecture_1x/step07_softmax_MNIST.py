# -*- coding: utf-8 -*-
"""
step07_softmax_MNIST.py
Softmax + MNIST
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. MNIST dataset load
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train.shape # (60000, 28, 28) 픽셀
y_train.shape # (60000,) 10진수들

## 첫번째 이미지 확인
plt.imshow(x_train[0])
plt.show()

y_train[0]
x_train[0]

# 2. impages 전처리
## 1) images 정규화
x_train_nor, x_test_nor = x_train / 255.0, x_test / 255.0 # 실수화도 겸함

x_train_nor[0]
x_test_nor[0]

## 2) 3차원 -> 2차원
x_train_nor = x_train_nor.reshape(-1, 784)
x_test_nor = x_test_nor.reshape(-1, 784)
x_train_nor.shape # (60000, 784)
x_test_nor.shape  # (10000, 784)
# 28*28 = 784

# 3. labels 전처리
## 1) 1차원 -> 2차원
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

## 2) one-hot encoding
obj = OneHotEncoder()
y_train_one = obj.fit_transform(y_train).toarray()
y_test_one = obj.fit_transform(y_test).toarray()
y_train_one.shape # (60000, 10)
y_test_one.shape  # (10000, 10)

# 4. X ,Y 변수 정의
X = tf.placeholder(dtype=tf.float32, shape=[None, 784]) # x data
Y = tf.placeholder(dtype=tf.float32, shape=[None, 10])  # y data

w = tf.Variable(tf.random_normal([784, 10])) # [input, output]
b = tf.Variable(tf.random_normal([10]))      # [output]

# 5. softmax algorithm
'''(1) model
   (2) softmax
   (3) loss function
   (4) optimizer
   (5) encoding -> decoding '''

## (1) model
model = tf.matmul(X, w) + b

## (2) softmax
softmax = tf.nn.softmax(model)

## (3) loss function
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
        labels = Y, logits = model))

## (4) optimaizer
train = tf.train.AdamOptimizer(0.1).minimize(loss)

## (5) encoding -> decoding
y_pred = tf.argmax(softmax, axis=1)
y_true = tf.argmax(Y, axis=1)


# 6. model training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed_data = {X : x_train_nor, Y : y_train_one}
    
    for step in range(300):
        _, loss_val = sess.run([train, loss], feed_dict = feed_data)
        print("step = {}, loss = {}".format(step+1, loss_val))        

    # model test
    feed_data2 = {X : x_test_nor, Y : y_test_one}
    y_pred_re = sess.run(y_pred, feed_dict = feed_data2)
    y_true_re = sess.run(y_true, feed_dict = feed_data2)
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("분류정확도 :", acc)
    
    # 분류정확도 : 0.9053 / 횟수100
    # 분류정확도 : 0.9202 / 횟수300
    
    
# 손실함수 와꾸가 달라지는 것이지 모델의 변화는 딱히 없다    
    
    
    
    
    