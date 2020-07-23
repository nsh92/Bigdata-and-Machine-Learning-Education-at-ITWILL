'''
문) DNN Layer를 적용하여 다음과 같이 DNN 모델을 생성하시오.
  조건1> hyper parameters
    learning_rate = 0.01
    training_epochs = 15
    batch_size = 100
    iter_size = 600
  조건2> DNN layer
    Layer1 =  784 x 512
    Layer2 =  512 x 256
    Layer3 =  256 x 10 
    
<<출력 예시>>
epoch = 1 cost= 55.16994312942028
epoch = 2 cost= 8.41355741351843
epoch = 3 cost= 4.618276522534089
epoch = 4 cost= 3.1665531673272898
epoch = 5 cost= 2.419369451348884
epoch = 6 cost= 1.9141375153187972
epoch = 7 cost= 1.4185047257376269
epoch = 8 cost= 1.3425187619523207
epoch = 9 cost= 1.1093137870219107
epoch = 10 cost= 0.9633290690958626
epoch = 11 cost= 0.7082862980902166
epoch = 12 cost= 0.7516645132078936
epoch = 13 cost= 0.5149420341080038
epoch = 14 cost= 0.3507416256171109
epoch = 15 cost= 0.26566603047227244
------------------------------------
accuracy = 0.9507        
'''  

import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함
from sklearn.preprocessing import OneHotEncoder # y data -> one hot
from sklearn.metrics import accuracy_score
import numpy as np

tf.set_random_seed(123) # w,b seed

# 1. MNIST dataset load
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# train set shape 확인 
x_train.shape # (60000, 28, 28) -> image(입력) : (size, h, w)
y_train.shape # (60000,) -> label(정답)

# test set shape
x_test.shape # (10000, 28, 28) -> image(입력)
y_test.shape # (10000,) -> label(정답)

# 2. 전처리 : X변수 정규화, Y변수 one-hot encoding  
x_train_nor, x_test_nor = x_train / 255.0, x_test / 255.0

# one-hot encoding
obj = OneHotEncoder()
train_labels = obj.fit_transform(y_train.reshape([-1, 1])).toarray()
train_labels.shape # (60000, 10)

test_labels = obj.fit_transform(y_test.reshape([-1, 1])).toarray()
test_labels.shape # (10000, 10)


# 3. 공급 data : image reshape(3d -> 2d)
train_images = x_train_nor.reshape(60000, 784)
test_images = x_test_nor.reshape(10000, 784)
train_images.shape # (60000, 784)
test_images.shape # (10000, 784)


X = tf.placeholder(tf.float32, [None, 784]) # [관측치, 입력수]
Y = tf.placeholder(tf.float32, [None, 10]) # [관측치, 출력수]

# hyper parameters
lr = 0.01
epochs = 15 # 전체 images(60,000) 20번 재사용 
batch_size = 100 # 1회 data 공급 size
iter_size = 600 # 반복횟수 

##############################
### MNIST DNN network
##############################
hidden1_nodes = 512
hidden2_nodes = 256

w1 = tf.Variable(tf.random_normal([784, hidden1_nodes]))
b1 = tf.Variable(tf.random_normal([hidden1_nodes])) 
hidden1_output = tf.nn.relu(tf.matmul(X, w1) + b1)

w2 = tf.Variable(tf.random_normal([hidden1_nodes, hidden2_nodes]))
b2 = tf.Variable(tf.random_normal([hidden2_nodes]))
hidden2_output = tf.nn.relu(tf.matmul(hidden1_output, w2) + b2)

w3 = tf.Variable(tf.random_normal([hidden2_nodes, 10]))
b3 = tf.Variable(tf.random_normal([10]))
model = tf.matmul(hidden2_output, w3) + b3

# 5. softmax algorithm
## (2) softmax
softmax = tf.nn.softmax(model)

## (3) loss function
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
        labels = Y, logits = model))

## (4) optimaizer
train = tf.train.AdamOptimizer(lr).minimize(loss)

## (5) encoding -> decoding
y_pred = tf.argmax(softmax, axis=1)
y_true = tf.argmax(Y, axis=1)


# 6. model training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed_data = {X : train_images, Y : train_labels}
    
    for epoch in range(epochs): # 1세대
        tot_loss = 0
        
        # 1epoch = 200 * 300 # 랜덤하지만 아무튼 6만장 학습
        for step in range(iter_size): # 300 반복 학습
            idx = np.random.choice(a=train_labels.shape[0], size=batch_size, replace=False)
            
            #Mini batch dataset
            feed_data = {X : train_images[idx], Y : train_labels[idx]}
            _, loss_val = sess.run([train, loss], feed_dict = feed_data)
            
            tot_loss += loss_val
        
        # 1epoch 종료
        avg_loss = tot_loss / iter_size
        print("epoch = {}, loss = {}".format(epoch+1, avg_loss))

    # 모델 최적화 : test
    feed_data2 = {X : test_images, Y : test_labels}
    y_pred_re = sess.run(y_pred, feed_dict = feed_data2)
    y_true_re = sess.run(y_true, feed_dict = feed_data2)
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("분류정확도 :", acc)

'''
epoch = 1, loss = 51.58125614708344
epoch = 2, loss = 8.249385139501344
epoch = 3, loss = 4.1408593996626
epoch = 4, loss = 2.449247063203899
epoch = 5, loss = 1.9738232552073198
epoch = 6, loss = 1.6716998412948818
epoch = 7, loss = 1.2545703926740337
epoch = 8, loss = 0.9215879582637165
epoch = 9, loss = 0.8449211991691579
epoch = 10, loss = 0.6043072080388348
epoch = 11, loss = 0.46946294296018704
epoch = 12, loss = 0.37149978914918996
epoch = 13, loss = 0.3604011772518667
epoch = 14, loss = 0.24679445487563498
epoch = 15, loss = 0.28198535552675214
분류정확도 : 0.9389
'''