# -*- coding: utf-8 -*-
"""
step04_sigmoid_classifier_iris
- 활성함수(activation function) : sigmoid
- 손실함수(loss function) : cross entropy
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris


# 1. x, y 공급 data 
iris = load_iris()
# x변수 : 1 ~ 4 컬럼
x_data = iris.data[:100]

# y변수 : 5 컬럼
y_data = iris.target[:100]
## y reshape
y_data = y_data.reshape(100,1)

# 2. X, Y 변수 정의
X = tf.placeholder(dtype=tf.float32, shape=[None,4])  # [관측치, 입력수]
Y = tf.placeholder(dtype=tf.float32, shape=[None,1])  # [관측치, 출력수]

# 3. w, b 변수 정의
w = tf.Variable(tf.random_normal([4, 1]))  # [입력수, 출력수]
b = tf.Variable(tf.random_normal([1]))     # [출력수]

# 4. sigmoid 분류기
# (1) model : 예측치 
model = tf.matmul(X, w) + b  # 회귀방정식
sigmoid = tf.sigmoid(model)  # 활성함수 적용(0~1 확률)

# (2) loss function : Entropy수식 = -sum(Y * log(model)) 
loss = -tf.reduce_mean(Y * tf.log(sigmoid) + (1-Y) * tf.log(1-sigmoid))

# (3) optimizer
'''
opt = tf.train.GradientDescentOptimizer(0.1)
trint = opt.minimize(loss)
'''
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss) # 최적화 객체

# (4) cut-off : 0.5
cut_off = tf.cast(sigmoid > 0.5, tf.float32) # T/F반환 -> 1.0/0.0 반환

# 5. model training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed_data = {X : x_data, Y : y_data}

    # 반복학습 : 500회
    for step in range(500):
        _, loss_val = sess.run([train, loss], feed_dict=feed_data)
        
        if (step+1) % 50 == 0:
            print("step = {}, loss = {}".format(step+1, loss_val))
        
    # 모델 최적화
    y_true = sess.run(Y, feed_dict = feed_data)
    y_pred = sess.run(cut_off, feed_dict = feed_data)
    
    acc = accuracy_score(y_true, y_pred)
    print("accuracy = ", acc)
    print(y_true)
    print(y_pred)













































