'''
exam_mnist_cnn_layer
 ppt-p.31 내용으로 CNN model를 설계하시오.
'''

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함
from tensorflow.keras.datasets.mnist import load_data # ver2.0 dataset
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score
import numpy as np

# minst data read
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape) # (60000, 28, 28)
print(y_train.shape) # (60000,) : 10진수 
print(x_test.shape) # (10000, 28, 28)
print(y_test.shape) # (10000,) : 10진수 

# image data reshape : [s, h, w, c]
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
print(x_train.shape) # (60000, 28, 28, 1)

# x_data : int -> float
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
print(x_train[0]) # 0 ~ 255

# x_data : 정규화 
x_train /= 255 # x_train = x_train / 255
x_test /= 255
print(x_train[0])

# y_data : 10 -> 2(one-hot)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# hyper parameters
learning_rate = 0.001
epochs = 15
batch_size = 100
iter_size = int(60000 / batch_size) # 600

# X, Y 변수 정의 
X_img = tf.placeholder(tf.float32, shape=[None, 28, 28, 1]) # (?, 784)
Y = tf.placeholder(tf.float32, shape=[None, 10]) # (?, 10)


#########################################
### 1. Conv layer1(Conv -> relu -> Pool)
#########################################
Filter1 = tf.Variable(tf.random_normal([5,5,1,32])) # 특징32가지를 추출하겠다 : 너무많아도 좀그렇고 적어도 좀그렇고

conv2 = tf.nn.conv2d(input=X_img, filter=Filter1, strides=[1,1,1,1], padding='SAME') # [1, 가로, 세로, 1] 4차원이니 4칸임
L1 = tf.nn.relu(conv2) # 정규화 0~x
L1_out = tf.nn.max_pool(L1, ksize = [1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
print(L1_out) # Tensor("MaxPool_9:0", shape=(?, 14, 14, 32), dtype=float32)


#########################################
### 2. Conv layer2(Conv -> relu -> Pool)
#########################################
Filter2 = tf.Variable(tf.random_normal([5,5,32,64])) # 3번째칸 수일치가 포인트, 64특징 증설

conv2_l2 = tf.nn.conv2d(input=L1_out, filter=Filter2, strides=[1,1,1,1], padding='SAME') 
L2 = tf.nn.relu(conv2_l2) # 정규화 0~x
L2_out = tf.nn.max_pool(L2, ksize = [1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
print(L2_out) # Tensor("MaxPool_10:0", shape=(?, 7, 7, 64), dtype=float32)


#########################################
### 3. Flatten layer (3d -> 1d)
#########################################

n = 7 * 7 * 64  # 3d -> 1d
L2_Flat = tf.reshape(L2_out, [-1, n])

w3 = tf.Variable(tf.random_normal([n, 10]))
b3 = tf.Variable(tf.random_normal([10]))
model = tf.matmul(L2_Flat, w3) + b3

softmax = tf.nn.softmax(model)

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
        labels = Y, logits = model))

train = tf.train.AdamOptimizer(learning_rate).minimize(loss)

y_pred = tf.argmax(softmax, axis=1)
y_true = tf.argmax(Y, axis=1)


# 6. model training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed_data = {X_img : x_train, Y : y_train}
    
    for epoch in range(epochs): 
        tot_loss = 0
        
        for step in range(iter_size): 
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
    # 분류정확도 : 0.9729






















