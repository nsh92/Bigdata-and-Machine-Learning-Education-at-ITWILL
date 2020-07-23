# -*- coding: utf-8 -*-
"""
step06_regression_model2_iris.py

 y 변수 : 1칼럼 
 x 변수 : 2~4칼럼
 model 최적화 알고리즘 : GD -> Adam 
 model 평가 : MSE 
"""

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.x 사용 안함 
import pandas as pd  # csv file read
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import mean_squared_error # model 평가 

# 1. 공급 data 생성 
iris = pd.read_csv("C:/ITWILL/6_Tensorflow/data/iris.csv")

cols = list(iris.columns)
x_data = iris[cols[1:4]] # 2~4컬럼  
y_data = iris[cols[0]] # 1칼럼 
x_data.shape # (150, 3) : 2차원 
y_data.shape # (150,) : 1차원 

x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size = 0.3)

x_train.shape # (105, 3)
x_test.shape # (45, 3)

# 2. X,Y 변수 정의 : 공급형 변수 
X = tf.placeholder(dtype=tf.float32, shape = [None,3]) # [관측치,입력수]
Y = tf.placeholder(dtype=tf.float32, shape = [None])#[관측치]

# 3. a(w), b 변수 정의 : 난수 초기값 
a = tf.Variable(tf.random_normal(shape = [3, 1])) # [입력수,출력수]
b = tf.Variable(tf.random_normal(shape = [1])) # [출력수]

# 4. model 생성 
model = tf.matmul(X, a) + b # 예측치 

loss = tf.reduce_mean(tf.square(Y - model))

opt = tf.train.AdamOptimizer(0.5) # 학습율 = 0.5 > 0.4 > 0.8

train = opt.minimize(loss) # 손실 최소화 식 

# 5. model 학습 -> model 최적화(최적의 a, b update됨)
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer()) # a, b 초기화 
    a_val, b_val = sess.run([a, b])
    print("최초 기울기 : {}, 절편 : {}".format(a_val, b_val))
    
    # 훈련용 공급 data 
    feed_data = {X : x_train, Y : y_train}
    
    # 반복학습 100회 > 200
    for step in range(100) :
        _, loss_val = sess.run([train, loss], feed_dict = feed_data)
        print("step = {}, loss = {:.5f}".format(step+1, loss_val))
    
    # model 최적화 
    a_up, b_up = sess.run([a, b])
    print("수정된 기울기 : {}, 절편 : {}".format(a_up, b_up)) 
    
    # 테스트용 공급 data 
    feed_data_test = {X : x_test, Y : y_test}
    
    # Y(정답) vs model(예측치)
    y_true = sess.run(Y, feed_dict = feed_data_test)
    y_pred = sess.run(model, feed_dict = feed_data_test)
    
    # model 평가 
    mse = mean_squared_error(y_true, y_pred)
    print("MSE = ", mse)
        
'''
1차 : 학습율 = 0.5, 반복학습 100회
MSE =  0.72902936
2차 : 학습율 = 0.4, 반복학습 100회
MSE =  0.5829428
3차 : 학습율 = 0.4, 반복학습 200회
MSE =  0.7733004
'''        
        
        
    





