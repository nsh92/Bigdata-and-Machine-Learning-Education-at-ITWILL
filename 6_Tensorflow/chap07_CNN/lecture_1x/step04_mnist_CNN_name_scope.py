# -*- coding: utf-8 -*-
"""
step04_mnist_CNN_name_scope.py

0. input layer : image(?*28*28 -> ?*28*28*1) -> ?(-1)
1. Conv layer1(Conv -> relu -> Pool)
2. Conv layer2(Conv -> relu -> Pool)
3. Flatten layer : [s,h,w,c] 3D -> 1D[s, n=h*w*c] 챠원축소
4. DNN hidden layer : [s, n] * [n, node]
5. DNN output layer : [n, node] * [node, 10]
"""
import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets.mnist import load_data # dataset load
import numpy as np
from sklearn.metrics import accuracy_score

# 텐서보드 초기화
tf.reset_default_graph()

# 1. image read 
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape) # (60000, 28, 28)
print(y_train.shape) # (60000,) : 10진수 

# 2. 실수형 변환 : int -> float32
x_train = x_train.astype('float32') 
x_test = x_test.astype('float32')

# 3. 정규화 
x_train = x_train / 255 # x_train = x_train / 255
x_test = x_test / 255

# 4. input image reshape : 2d -> 3d
x_train = x_train.reshape(-1, 28, 28, 1) # (size, h, w, color)
x_test = x_test.reshape(-1, 28, 28, 1)

# 5. y_data 전처리 : one-hot encoding
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
y_train.shape # (60000, 10)
y_test.shape

# 6. X, Y 변수 정의
X_img = tf.placeholder(tf.float32, shape = [None, 28, 28, 1]) # input image
Y = tf.placeholder(tf.float32, shape = [None, 10])


#########################################
### 1. Conv layer1(Conv -> relu -> Pool)
#########################################
with tf.name_scope("convoulution1") as scope:
    Filter1 = tf.Variable(tf.random_normal([3,3,1,32])) # 특징32가지를 추출하겠다 : 너무많아도 좀그렇고 적어도 좀그렇고
    conv2 = tf.nn.conv2d(input=X_img, filter=Filter1, strides=[1,1,1,1], padding='SAME') # [1, 가로, 세로, 1] 4차원이니 4칸임
    L1 = tf.nn.relu(conv2) # 정규화 0~x
    L1_out = tf.nn.max_pool(L1, ksize = [1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    print(L1_out) # Tensor("MaxPool_9:0", shape=(?, 14, 14, 32), dtype=float32)


#########################################
### 2. Conv layer2(Conv -> relu -> Pool)
#########################################
with tf.name_scope("convoulution2") as scope:
    Filter2 = tf.Variable(tf.random_normal([3,3,32,64])) # 3번째칸 수일치가 포인트, 64특징 증설
    conv2_l2 = tf.nn.conv2d(input=L1_out, filter=Filter2, strides=[1,1,1,1], padding='SAME') 
    L2 = tf.nn.relu(conv2_l2) # 정규화 0~x
    L2_out = tf.nn.max_pool(L2, ksize = [1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    print(L2_out) # Tensor("MaxPool_10:0", shape=(?, 7, 7, 64), dtype=float32)


#########################################
### 3. Flatten layer (3d -> 1d)
#########################################
with tf.name_scope("Flatten") as scope:
    n = 7 * 7 * 64  # 3d -> 1d
    L2_Flat = tf.reshape(L2_out, [-1, n])

# DNN layer : chap05 step3 퍼옴

# Hyper parameters
lr = 0.01 # 학습률
epochs = 3 # 전체 데이터 재사용 횟수
batch_size = 200 # 1회 데이터 공급 횟수
iter_size = 600 # 반복횟수
hidden_nodes = 128

##########################################
## DNN network
##########################################
with tf.name_scope("DNN_hidden_layer") as scope:
    w1 = tf.Variable(tf.random_normal([n, hidden_nodes]), name="w1")
    b1 = tf.Variable(tf.random_normal([hidden_nodes]), name="b1") 
    hidden_output = tf.nn.relu(tf.matmul(L2_Flat, w1) + b1)

with tf.name_scope("DNN_output_layer") as scope:
    w3 = tf.Variable(tf.random_normal([hidden_nodes, 10]), name="w2")
    b3 = tf.Variable(tf.random_normal([10]), name="b2")
    model = tf.matmul(hidden_output, w3) + b3
    # 5. softmax algorithm
    ## (2) softmax
    softmax = tf.nn.softmax(model)

with tf.name_scope("lossFuction") as scope:
    ## (3) loss function
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
            labels = Y, logits = model))
with tf.name_scope("optimizer") as scope:
    ## (4) optimaizer
    train = tf.train.AdamOptimizer(lr).minimize(loss)

with tf.name_scope("Prediction") as scope:
    ## (5) encoding -> decoding
    y_pred = tf.argmax(softmax, axis=1)
    y_true = tf.argmax(Y, axis=1)


# 6. model training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    tf.summary.merge_all()
    writer = tf.summary.FileWriter(r"C:/ITWILL/6_Tensorflow/graph", sess.graph)
    print("tensorboard 시각화 완료")
    writer.close()
    
    feed_data = {X_img : x_train, Y : y_train}
    
    for epoch in range(epochs): # 1세대
        tot_loss = 0
        
        # 1epoch = 200 * 300 # 랜덤하지만 아무튼 6만장 학습
        for step in range(iter_size): # 300 반복 학습
            idx = np.random.choice(a=y_train.shape[0], size=batch_size, replace=False)
            
            #Mini batch dataset
            feed_data = {X_img : x_train[idx], Y : y_train[idx]}
            _, loss_val = sess.run([train, loss], feed_dict = feed_data)
            
            tot_loss += loss_val
        
        # 1epoch 종료
        avg_loss = tot_loss / iter_size
        print("epoch = {}, loss = {}".format(epoch+1, avg_loss))

    # 모델 최적화 : test
    feed_data2 = {X_img : x_test, Y : y_test}
    y_pred_re = sess.run(y_pred, feed_dict = feed_data2)
    y_true_re = sess.run(y_true, feed_dict = feed_data2)
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("분류정확도 :", acc)





