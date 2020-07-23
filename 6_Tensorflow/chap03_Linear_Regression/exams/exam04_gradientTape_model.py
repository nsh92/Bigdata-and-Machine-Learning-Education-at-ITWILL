# -*- coding: utf-8 -*-

'''
문) load_boston() 함수를 이용하여 보스턴 시 주택 가격 예측 회귀모델 생성하기 
  조건1> train/test - 7:3비율 
  조건2> y 변수 : boston.target
  조건3> x 변수 : boston.data
  조건4> learning_rate=0.005
  조건5> optimizer = tf.keras.optimizers.Adam
  조건6> epoch(step) = 5000회
  조건7> 모델 평가 : MSE
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import minmax_scale # 정규화
from sklearn.metrics import mean_squared_error
import tensorflow as tf 
import numpy as np

# 1. data load
boston = load_boston()
print(boston) # "data", "target"

# 변수 선택  
X = boston.data  
y = boston.target
X.shape # (506, 13)

y_nor = minmax_scale(y) # 정규화 

# train/test split(90 vs 10)
x_train, x_test, y_train, y_test = train_test_split(
        X, y_nor, test_size=0.3, random_state=123)

tf.random.set_seed(123)

# 2. Model 클래스 : model = input * w + b
class Model(tf.keras.Model): # 자식클래스(부모클래스)
    def __init__(self):      # 생성자
        super().__init__()   # 부모생성자 호출
        self.W = tf.Variable(tf.random.normal([13, 1])) # 기울기(가중치)
        self.B = tf.Variable(tf.random.normal([1])) # 절편
    def call(self, inputs):  # 메소드 재정의
        return tf.matmul(tf.cast(inputs, tf.float32), self.W) + self.B

# 3. 손실함수 : (예측치, 정답) -> 오차 
def loss(model, inputs, outputs):
  err = model(inputs) - outputs
  return tf.reduce_mean(tf.square(err))


# 4. 기울기 계산 함수 : 오차값 -> 기울기 반환 
def gradient(model, inputs, outputs):
    with tf.GradientTape() as tape:
        loss_value = loss(model, inputs, outputs) # 손실함수 호출  
        grad = tape.gradient(loss_value, [model.W, model.B]) 
        # 미분계수 -> 기울기와 절편 업데이트
    return grad

# 5. 모델 및 최적화 객체   
model = Model()
opt = tf.keras.optimizers.Adam(learning_rate=0.005)
print("초기 손실값 : {:.6f}".format(loss(model, x_train, y_train)))
print("w : {}, b : {}".format(model.W.numpy(), model.B.numpy()))

# 6. 반복 학습 : Model 객체와 손실함수 이용
for step in range(5000):
    grad = gradient(model, x_train, y_train) # 기울기 계산
    # 기울기 -> 최적화 객체 반영
    opt.apply_gradients(zip(grad, [model.W, model.B]))
    if (step+1) % 500 == 0:
        print("step = {}, loss = {:.6f}".format((step+1), loss(model, x_train, y_train)))
    
# 7. 최적화된 model 
print("최적 손실값 : {:.6f}".format(loss(model, x_train, y_train)))
print("w : {}, b : {}".format(model.W.numpy(), model.B.numpy()))

y_pred = model.call(x_test)
mse = mean_squared_error(y_test, y_pred)
print("mse =", mse)
r2 = r2_score(y_test, y_pred)
print("r2 =", r2)

'''
초기 손실값 : 102965.164062
w : [[-0.8980837 ]
 [-1.8259144 ]
 [-0.44441807]
 [-1.4882947 ]
 [-0.7855463 ]
 [ 0.19619656]
 [ 0.17604655]
 [-1.5252506 ]
 [ 0.635294  ]
 [ 0.66812044]
 [ 1.4230527 ]
 [ 0.04561644]
 [-0.21692705]], b : [0.33875433]

최적 손실값 : 2.890493
w : [[-0.00119942]
 [ 0.03664925]
 [-0.21786375]
 [ 0.61787105]
 [-1.1151606 ]
 [-0.30855596]
 [-0.02078074]
 [-1.112954  ]
 [-0.14456108]
 [ 0.00417181]
 [ 0.69109195]
 [-0.0054872 ]
 [-0.03209294]], b : [-0.09131183]

mse = 2.761119563841525
r2 = -68.17480050671179
'''