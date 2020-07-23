# -*- coding: utf-8 -*-
"""
step03_gradientTape_model2_iris.py

tf.GradientTape + regression model
 - x변수 : 2 ~ 4 컬럼
 - y변수 : 1컬럼
 - 모델 최적화 알고리즘 : Adam
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf

# 1. input/output 변수 정의 
iris = load_iris()
inputs = iris.data[:, 1:]
outputs = iris.data[:, 0]
inputs.shape   # X
outputs.shape  # Y

tf.random.set_seed(123) # W, B에 대한 시드

x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size = 0.3, random_state=123)

# 2. model : model class
class Model(tf.keras.Model): # 자식클래스(부모클래스)
    def __init__(self):      # 생성자
        super().__init__()   # 부모생성자 호출
        self.W = tf.Variable(tf.random.normal([3, 1])) # 기울기(가중치)
        self.B = tf.Variable(tf.random.normal([1])) # 절편
    def call(self, inputs):  # 메소드 재정의
        return tf.matmul(tf.cast(inputs, tf.float32), self.W) + self.B # 회귀방정식 예측치 반환
                                 # 데이터타입 일치화시켜야 함 텐서플로우는 특히 민감함

# 3. 손실 함수
def loss(model, inputs, outputs):
  err = model(inputs) - outputs
  return tf.reduce_mean(tf.square(err)) # MSE

# 4. 미분계수(기울기) 계산  
def gradient(model, inputs, outputs):
    with tf.GradientTape() as tape:
        loss_value = loss(model, inputs, outputs) # 손실함수 호출  
        grad = tape.gradient(loss_value, [model.W, model.B]) 
        # 미분계수 -> 기울기와 절편 업데이트
    return grad # 업데이트 결과 반환

# 5. 모델 생성
model = Model() # 생성자

# 6. 모델 최적화 객체
opt = tf.keras.optimizers.SGD(learning_rate=0.001)

print("초기 손실값 : {:.6f}".format(loss(model, x_train, y_train)))
print("w : {}, b : {}".format(model.W.numpy(), model.B.numpy()))

# 7. 반복학습
for step in range(300):
    grad = gradient(model, x_train, y_train) # 기울기 계산
    # 기울기 -> 최적화 객체 반영
    opt.apply_gradients(zip(grad, [model.W, model.B]))
    if (step+1) % 20 == 0:
        print("step = {}, loss = {:.6f}".format((step+1), loss(model, x_train, y_train)))

# 최적화된 변수들 조회
print("최적 손실값 : {:.6f}".format(loss(model, x_train, y_train)))
print("w : {}, b : {}".format(model.W.numpy(), model.B.numpy()))

# 모델 테스트
y_pred = model.call(x_test)
# print(y_pred.numpy())

mse = mean_squared_error(y_test, y_pred)
print("mse =", mse)

r2 = r2_score(y_test, y_pred)
print("r2 =", r2)

'''
초기 손실값 : 261.838470
w : [[-0.8980837 ]
 [-1.8259144 ]
 [-0.44441807]], b : [0.33875433]

최적 손실값 : 1.705331
w : [[ 0.7612573 ]
 [-0.20238313]
 [ 1.1611581 ]], b : [1.9997358]
mse = 1.0807632023184397
r2 = -0.349987345292778
모델 성능 구림 : 튜닝 필요

학습 횟수나 학습률 조절
Adam -> SGD 바꾸거나

'''



























