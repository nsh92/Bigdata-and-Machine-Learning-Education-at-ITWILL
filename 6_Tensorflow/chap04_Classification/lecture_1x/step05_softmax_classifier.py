# -*- coding: utf-8 -*-
"""
step04_softmax_classifier.py
- 활성함수 : Sotfmax(model)
- 손실함수 : Cross Entropy
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
from sklearn.metrics import accuracy_score

# 1. x, y 공급 data 
# [털, 날개]
x_data = np.array(
    [[0, 0], [1, 0], [1, 1], [0, 0], [0, 1], [1, 1]]) # [6, 2]

# [기타, 포유류, 조류] : [6, 3]  -> one hot encoding : 1과 0으로 표시
y_data = np.array([
    [1, 0, 0],  # 기타[0]
    [0, 1, 0],  # 포유류[1]
    [0, 0, 1],  # 조류[2]
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 1]
])

# 2. X, Y 변수 정의
X = tf.placeholder(dtype=tf.float32, shape=[None, 2]) # [관측치, 입력수]
Y = tf.placeholder(dtype=tf.float32, shape=[None, 3]) # [관측치, 출력수]

# 3. w, b변수 정의 : 초기값은 난수
w = tf.Variable(tf.random_normal([2,3])) # [입력수, 출력수]
b = tf.Variable(tf.random_normal([3]))   # [출력수]

# 4. softmax 분류기 
# 1) 회귀방정식 : 예측치 
model = tf.matmul(X, w) + b # 회귀모델 

# softmax(예측치)
softmax = tf.nn.softmax(model) 

# 2) loss function : Cross Entropy 이용 : -sum(Y * log(model)) 
loss = -tf.reduce_mean(Y * tf.log(softmax) + (1 - Y) * tf.log(1 - softmax))

# 3) optimizer : 오차 최소화(w, b update) 
train = tf.train.AdamOptimizer(0.1).minimize(loss) # 오차 최소화

# 4) argmax() : encoding(2진수로된 것) -> decoding(10진수)
y_pred = tf.argmax(softmax, axis = 1)
y_true = tf.argmax(Y, axis = 1)

# 5. 모델 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # w b 초기화
    feed_data = {X : x_data, Y : y_data}
    
    # 반복학습 : 500ghl
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
    
'''
step = 50, loss = 0.08309727162122726
step = 100, loss = 0.02883036620914936
step = 150, loss = 0.016369767487049103
step = 200, loss = 0.01092542801052332
step = 250, loss = 0.007947643287479877
step = 300, loss = 0.0061068180948495865
step = 350, loss = 0.004874517675489187
step = 400, loss = 0.004001634661108255
step = 450, loss = 0.003356706351041794
step = 500, loss = 0.0028643012046813965
y pred = [0 1 2 0 0 2]
y true = [0 1 2 0 0 2]
분류정확도 = 1.0
'''
    
    
    
    
    
    
    
    
    
    
    