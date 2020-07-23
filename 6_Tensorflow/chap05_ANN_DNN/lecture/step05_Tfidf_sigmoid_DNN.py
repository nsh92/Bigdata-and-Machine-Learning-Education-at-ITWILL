# -*- coding: utf-8 -*-
"""
step05_Tfidf_sigmoid_DNN.py

1. Tfidf 가중치 기법 : 희소행렬
2. Sigmoid 활성함수 : ham / spam
3. Hyper parameters
   max features = 4000(input node)
   lr = 0.01
   epochs = 50
   batch size = 500
   iter size = 10
    -> 1epoch = 500개씩 * 10번 = 5천
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from sklearn.metrics import accuracy_score
import numpy as np

## file load
x_train, x_test, y_train, y_test = np.load('C:/ITWILL/6_Tensorflow/data/spam_data.npy',
                                           allow_pickle=True)
x_train.shape # (3901, 4000)
x_test.shape  # (1673, 4000)
type(x_train) # numpy.ndarray
type(y_train) # list

# 리스트 -> 넘파이
y_train = np.array(y_train)
y_test = np.array(y_test)
y_train.shape
y_train = y_train.reshape(-1, 1)  # (60000,) -> (60000, 1)
y_test = y_test.reshape(-1, 1) 

# Hyper parameters
max_features = 4000
lr = 0.01
epochs = 50
batch_size = 500
iter_size = 10

# X, Y 변수 정의
X = tf.placeholder(dtype=tf.float32, shape = [None, max_features])
Y = tf.placeholder(dtype=tf.float32, shape = [None, 1]) # ham / spam

# DNN Network
hidden1_nodes = 6
hidden2_nodes = 3

# hidden layer : 1층 : relu()
w1 = tf.Variable(tf.random_normal([max_features, hidden1_nodes])) # [input, output]
b1 = tf.Variable(tf.random_normal([hidden1_nodes]))     # [output]
hidden1_output = tf.nn.relu(tf.matmul(X, w1) + b1)

# hidden layer : 2층 : relu()
w2 = tf.Variable(tf.random_normal([hidden1_nodes, hidden2_nodes])) # [input, output]
b2 = tf.Variable(tf.random_normal([hidden2_nodes]))     # [output]
hidden2_output = tf.nn.relu(tf.matmul(hidden1_output, w2) + b2)

# output layer : 3층 : softmax()
w3 = tf.Variable(tf.random_normal([hidden2_nodes, 1]))
b3 = tf.Variable(tf.random_normal([1]))

# 4. sigmoid 분류기 
# output layer 출력
model = tf.matmul(hidden2_output, w3) + b3

# softmax(예측치)
sigmoid = tf.sigmoid(model) 

# 손실함수
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(
   labels = Y, logits = model))

# optimizer : 오차 최소화(w, b update) 
train = tf.train.AdamOptimizer(0.1).minimize(loss) # 오차 최소화

# cut-off
y_pred = tf.cast(sigmoid > 0.5, tf.float32)

# 6. model training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for epoch in range(epochs): # 1세대
        tot_loss = 0
        
        # 1epoch = 500 * 10
        for step in range(iter_size):
            idx = np.random.choice(a=x_train.shape[0], size=batch_size, replace=False)
            
            #Mini batch dataset
            feed_data = {X : x_train[idx], Y : y_train[idx]}
            _, loss_val = sess.run([train, loss], feed_dict = feed_data)
            
            tot_loss += loss_val
        
        # 1epoch 종료
        avg_loss = tot_loss / iter_size
        print("epoch = {}, loss = {}".format(epoch+1, avg_loss))

    # 모델 최적화 : test
    feed_data2 = {X : x_test, Y : y_test}
    y_pred_re = sess.run(y_pred, feed_dict = feed_data2)
    y_true_re = sess.run(Y, feed_dict = feed_data2)
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("분류정확도 :", acc)

'''
epoch = 1, loss = 0.3201764985918999
epoch = 2, loss = 0.12139738351106644
epoch = 3, loss = 0.08068116717040538
epoch = 4, loss = 0.04784115515649319
epoch = 5, loss = 0.036650591529905796
epoch = 6, loss = 0.02379591753706336
epoch = 7, loss = 0.02008139556273818
epoch = 8, loss = 0.013228409737348557
epoch = 9, loss = 0.01389047671109438
epoch = 10, loss = 0.011957559920847415
epoch = 11, loss = 0.012306007463485003
epoch = 12, loss = 0.010551395500078798
epoch = 13, loss = 0.011425824277102948
epoch = 14, loss = 0.01012858939357102
epoch = 15, loss = 0.012334763910621405
epoch = 16, loss = 0.00908417694736272
epoch = 17, loss = 0.00748496139422059
epoch = 18, loss = 0.01043386075180024
epoch = 19, loss = 0.00802763206884265
epoch = 20, loss = 0.007175359595566988
epoch = 21, loss = 0.007595310127362609
epoch = 22, loss = 0.00900378783699125
epoch = 23, loss = 0.00417977124452591
epoch = 24, loss = 0.0073856719536706805
epoch = 25, loss = 0.007177503220736981
epoch = 26, loss = 0.007204906828701496
epoch = 27, loss = 0.005606194399297238
epoch = 28, loss = 0.003773997980169952
epoch = 29, loss = 0.005342025042045862
epoch = 30, loss = 0.005894470075145364
epoch = 31, loss = 0.010609801136888563
epoch = 32, loss = 0.004522522259503603
epoch = 33, loss = 0.004355877393390983
epoch = 34, loss = 0.005887816555332393
epoch = 35, loss = 0.007731025724206119
epoch = 36, loss = 0.007804915227461606
epoch = 37, loss = 0.005087757704313844
epoch = 38, loss = 0.0032339915167540314
epoch = 39, loss = 0.006127330998424441
epoch = 40, loss = 0.00704039455158636
epoch = 41, loss = 0.009755165502429008
epoch = 42, loss = 0.005895449698437005
epoch = 43, loss = 0.007656178320758045
epoch = 44, loss = 0.0040137333329766985
epoch = 45, loss = 0.014677116926759482
epoch = 46, loss = 0.006866311491467059
epoch = 47, loss = 0.00779901392525062
epoch = 48, loss = 0.006856866495218128
epoch = 49, loss = 0.005001333821564913
epoch = 50, loss = 0.00555550092831254
분류정확도 : 0.9772863120143455
'''











