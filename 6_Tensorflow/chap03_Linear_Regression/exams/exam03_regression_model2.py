'''
문3) iris.csv 데이터 파일을 이용하여 선형회귀모델  생성하시오.
     [조건1] x변수 : 2,3칼럼,  y변수 : 1칼럼
     [조건2] 7:3 비율(train/test set)
         train set : 모델 생성, test set : 모델 평가  
     [조건3] learning_rate=0.01
     [조건4] 학습 횟수 1,000회
     [조건5] model 평가 - MSE출력 
'''
import pandas as pd
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 
from sklearn.metrics import mean_squared_error # model 평가 
from sklearn.preprocessing import minmax_scale # 정규화 
from sklearn.model_selection import train_test_split # train/test set

iris = pd.read_csv('C:/ITWILL/6_Tensorflow/data/iris.csv')
print(iris.info())
cols = list(iris.columns)
iris_df = iris[cols[:3]] 

# 1. x data, y data
x_data = iris_df[cols[1:3]] # x train
y_data = iris_df[cols[0]] # y tran

# 2. x,y 정규화(0~1) 
x_data = minmax_scale(x_data)

# 3. train/test data set 구성 
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size = 0.3)

# 4. 변수 정의
X = tf.placeholder(dtype=tf.float32, shape = [None,2])
Y = tf.placeholder(dtype=tf.float32, shape = [None])

a = tf.Variable(tf.random_normal(shape = [2, 1]))
b = tf.Variable(tf.random_normal(shape = [1]))

# 5. model 생성 
model = tf.matmul(X, a) + b
loss = tf.reduce_mean(tf.square(Y - model))
opt = tf.train.AdamOptimizer(0.01)
train = opt.minimize(loss)

# 6. model training
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())
    a_val, b_val = sess.run([a, b])
    print("최초 기울기 : {}, 절편 : {}".format(a_val, b_val))
    
    feed_data = {X : x_train, Y : y_train}
    
    for step in range(1000) :
        _, loss_val = sess.run([train, loss], feed_dict = feed_data)
        print("step = {}, loss = {:.5f}".format(step+1, loss_val))
    
    a_up, b_up = sess.run([a, b])
    print("수정된 기울기 : {}, 절편 : {}".format(a_up, b_up)) 
    
    feed_data_test = {X : x_test, Y : y_test}
    
    y_true = sess.run(Y, feed_dict = feed_data_test)
    y_pred = sess.run(model, feed_dict = feed_data_test)
    
    mse = mean_squared_error(y_true, y_pred)
    print("MSE = ", mse)
    
'''
수정된 기울기 : [[3.047763 ]
 [1.0799981]], 절편 : [3.9529645]
MSE =  0.59611356
'''




