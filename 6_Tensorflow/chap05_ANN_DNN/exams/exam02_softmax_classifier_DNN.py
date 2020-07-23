'''
문) wine data set을 이용하여 다음과 같이 DNN 모델을 생성하시오.
  <조건1>   
   - Hidden layer : relu()함수 이용  
   - Output layer : softmax()함수 이용 
   - 2개의 은닉층을 갖는 DNN 분류기
     hidden1 : nodes = 6
     hidden2 : nodes = 3  
  <조건2> hyper parameters
    learning_rate = 0.01
    iter_size = 1,000
  <조건3>  
    train/test(80:20)
    x_data : 정규화 
    y_data : one-hot encoding
'''

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함
from sklearn.datasets import load_wine # data set
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale
import numpy as np
from sklearn.metrics import accuracy_score

# 1. wine data load
wine = load_wine()

# 2. 변수 선택/전처리  
x_data = wine.data # 178x13
y_data = wine.target # 3개 domain
print(y_data) # 0-2
print(x_data.shape) # (178, 13)

# x_data : 정규화 
x_data = minmax_scale(x_data) # 0~1

# y변수 one-hot-encoding : 0=[1,0,0] / 1=[0,1,0] / 2=[0,0,1]
num_class = np.max(y_data)+1 # 2+1
print(num_class) # 3

y_data = np.eye(num_class)[y_data]
print(y_data.shape) # (178, 3)

# 4. train/test split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=123)

# 5. X,Y 변수 정의  
X = tf.placeholder(tf.float32, shape=[None, 13]) # [n, 13개 원소]
Y = tf.placeholder(tf.float32, shape=[None, 3]) # [n, 3개 원소]

# 6. Hypter parameters
learning_rate = 0.01
iter_size = 1000

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)
    
##############################
### DNN network
##############################
hidden1_nodes = 6
hidden2_nodes = 3  

w1 = tf.Variable(tf.random_normal([13, hidden1_nodes]))
b1 = tf.Variable(tf.random_normal([hidden1_nodes])) 
hidden1_output = tf.nn.relu(tf.matmul(X, w1) + b1)

w2 = tf.Variable(tf.random_normal([hidden1_nodes, hidden2_nodes]))
b2 = tf.Variable(tf.random_normal([hidden2_nodes]))
hidden2_output = tf.nn.relu(tf.matmul(hidden1_output, w2) + b2)

w3 = tf.Variable(tf.random_normal([hidden2_nodes, 3]))
b3 = tf.Variable(tf.random_normal([3]))
model = tf.matmul(hidden2_output, w3) + b3

softmax = tf.nn.softmax(model)
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
   labels = Y, logits = model))

train = tf.train.AdamOptimizer(0.01).minimize(loss)

y_pred = tf.argmax(softmax, axis = 1)
y_true = tf.argmax(Y, axis = 1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # w b 초기화
    feed_data = {X : x_data, Y : y_data}
    
    for step in range(1000):
        _, loss_val = sess.run([train, loss], feed_dict=feed_data)
        
        if (step+1) % 100 == 0:
            print("step = {}, loss = {}".format(step+1, loss_val))
            
    y_pred_re = sess.run(y_pred, feed_dict = {X : x_data}) # 예측치
    y_true_re = sess.run(y_true, feed_dict = {Y : y_data}) # 정답
    
    print("y pred =", y_pred_re)
    print("y true =", y_true_re)
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("분류정확도 =", acc)

# 분류정확도 = 1.0


























