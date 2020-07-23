'''
문) bmi.csv 데이터셋을 이용하여 다음과 같이 sigmoid classifier의 모델을 생성하시오. 
   조건1> bmi.csv 데이터셋 
       -> x변수 : 1,2번째 칼럼(height, weight) 
       -> y변수 : 3번째 칼럼(label)의  normal, fat 관측치 대상
   조건2> 2,000번 학습, 200 step 단위로 loss 출력 
   조건3> 분류정확도 리포트(Accuracy report) 출력  
'''
import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

bmi = pd.read_csv('c:/ITWILL/6_Tensorflow/data/bmi.csv')
print(bmi.info())

# label에서 normal, fat 추출 
bmi = bmi[bmi.label.isin(['normal','fat'])]
print(bmi.head())

# 칼럼 추출 
col = list(bmi.columns)
print(col) 

# x,y 변수 추출 
x_data = bmi[col[:2]] # x변수(1,2칼럼)
y_data = bmi[col[2]] # y변수(3칼럼)
print('정규화 전 ')
print(x_data) 

# label 더미변수 변환(normal -> 0, fat -> 1)
map_data = {'normal': 0,'fat' : 1}
y_data= y_data.map(map_data) # dict mapping
print(y_data) # 0/1

# x_data 정규화 함수 
def normalize(x):
    return (x - min(x)) / (max(x) - min(x))

x_data = x_data.apply(normalize)
print('정규화 후 ')
print(x_data)

# numpy 객체 변환 
x_data = np.array(x_data)
y_data = np.transpose(np.array([y_data])) # (1, 15102) -> (15102, 1)

print(x_data.shape) # (15102, 2)
print(y_data.shape) # (15102, 1)

# 공급data
print(x_data)
print(y_data)


# X,y 변수 정의 
X = tf.placeholder(tf.float32, shape=[None, 2]) # [관측치, 입력수]
Y = tf.placeholder(tf.float32, shape=[None, 1]) # [관측치, 출력수]  

# w,b 변수 정의 : 초기값(정규분포 난수 )
w = tf.Variable(tf.random_normal([2, 1]))# [입력수,출력수]
b = tf.Variable(tf.random_normal([1])) # [출력수] 

# 이항분류기(1~4단계)
# 1. model 
model = tf.matmul(X, w) + b
sigmoid = tf.sigmoid(model)

# 2. cost function
loss = -tf.reduce_mean(Y * tf.log(sigmoid) + (1-Y) * tf.log(1-sigmoid))

# 3. GradientDesent algorithm : 비용함수 최소화
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 4. cut-off 적용  
cut_off = tf.cast(sigmoid > 0.5, tf.float32)

with tf.Session() as sess: # <조건3> ~ <조건4>
    sess.run(tf.global_variables_initializer())
    
    feed_data = {X : x_data, Y : y_data}

    # 반복학습 : 2000회
    for step in range(2000):
        _, loss_val = sess.run([train, loss], feed_dict=feed_data)
        
        if (step+1) % 200 == 0:
            print("step = {}, loss = {}".format(step+1, loss_val))
        
    # 모델 최적화
    y_true = sess.run(Y, feed_dict = feed_data)
    y_pred = sess.run(cut_off, feed_dict = feed_data)
    
    acc = accuracy_score(y_true, y_pred)
    print("accuracy = ", acc)

'''
step = 200, loss = 0.6060866713523865
step = 400, loss = 0.5101534724235535
step = 600, loss = 0.44562435150146484
step = 800, loss = 0.3996407687664032
step = 1000, loss = 0.36523720622062683
step = 1200, loss = 0.33847638964653015
step = 1400, loss = 0.3170071840286255
step = 1600, loss = 0.2993500828742981
step = 1800, loss = 0.2845309376716614
step = 2000, loss = 0.2718835473060608
accuracy =  0.9768904780823732
'''





