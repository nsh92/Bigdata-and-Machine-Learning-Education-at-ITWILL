# -*- coding: utf-8 -*-
"""
step01_softmax_cluster_ANN.py

ANN 모델
 - hidden layer : relu 활성함수
 - output layer : Softmax 활성함수
 - 1개의 은닉층을 갖는 분류기, 출력 노드 3 가정
 - node : 5개
 - dataset : iris
"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder # ydata를 이진법 코딩

# 1. x, y 공급 data 
iris = load_iris()
# x변수 : 1 ~ 4 컬럼
x_data = iris.data
# y변수 : 5 컬럼
y_data = iris.target
## y reshape
y_data = y_data.reshape(-1, 1)
y_data.shape


obj = OneHotEncoder()
y_data = obj.fit_transform(y_data).toarray() # toararray가 없으면 150x3 sparse matrix 객체정보만 뜸
# [1,0,0] [0,1,0] [0,0,1] 변환
y_data.shape # 그래서 (150, 3)

# 2. X, Y 변수 정의
X = tf.placeholder(dtype=tf.float32, shape=[None, 4]) # [관측치, 입력수]
Y = tf.placeholder(dtype=tf.float32, shape=[None, 3]) # [관측치, 출력수]

###############################
## ANN network
###############################

hidden_node = 5

# hidden layer
w1 = tf.Variable(tf.random_normal([4, hidden_node])) # [input, output]
b1 = tf.Variable(tf.random_normal([hidden_node]))     # [output]

# output layer
w2 = tf.Variable(tf.random_normal([hidden_node, 3]))
b2 = tf.Variable(tf.random_normal([3]))

# 4. softmax 분류기 
# hidden layer 출력 
hidden_output = tf.nn.relu(tf.matmul(X, w1) + b1) # 회귀모델 -> 활성함수(relu) 장착

# output layer 출력
model = tf.matmul(hidden_output, w2) + b2

# softmax(예측치)
softmax = tf.nn.softmax(model) 

# 2) loss function : Cross Entropy 이용 : -sum(Y * log(model)) 
# loss = -tf.reduce_mean(Y * tf.log(softmax) + (1 - Y) * tf.log(1 - softmax)) # -있음

# 2) 2차 방법 : 소프트맥스 +  크로스엔트로피
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
   labels = Y, logits = model))

# 3) optimizer : 오차 최소화(w, b update) 
train = tf.train.AdamOptimizer(0.1).minimize(loss) # 오차 최소화

# 4) argmax() : encoding(2진수로된 것) -> decoding(10진수)
y_pred = tf.argmax(softmax, axis = 1)
y_true = tf.argmax(Y, axis = 1)

# 5. 모델 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # w b 초기화
    feed_data = {X : x_data, Y : y_data}
    
    # 반복학습 : 500
    for step in range(500):
        _, loss_val = sess.run([train, loss], feed_dict=feed_data)
        
        if (step+1) % 50 == 0:
            print("step = {}, loss = {}".format(step+1, loss_val))
            
    # model result
    # 결과값이 몇 번 클래스인지 알아야하기에 y_data를 10진수 표시로 바꿔야 함 혹은 y1, y2, y3 이런 식이거나
    y_pred_re = sess.run(y_pred, feed_dict = {X : x_data}) # 예측치
    y_true_re = sess.run(y_true, feed_dict = {Y : y_data}) # 정답
    
    print("y pred =", y_pred_re)
    print("y true =", y_true_re)
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("분류정확도 =", acc)
# 분류정확도 = 0.98



































