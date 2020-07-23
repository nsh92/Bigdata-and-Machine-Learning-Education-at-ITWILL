# -*- coding: utf-8 -*-
"""
step02_gradientTape_model
tf.GradientTape + regression model
 -> 미분계수 자동 계산 -> 모델 최적화(최적의 기울기와 절편 업데이트)
"""
import tensorflow as tf
tf.executing_eagerly()

# 1. input/output 변수 정의 
inputs = tf.Variable([1.0, 2.0, 3.0]) # x변수 
outputs = tf.Variable([2.0, 4.0, 6.0]) # y변수 ==> 후에 x에 2.5를 넣으면 5 쯤이 나오면 학습이 됐구나 판단

# 2. model : model class
class Model(tf.keras.Model): # 자식클래스(부모클래스)
    def __init__(self):      # 생성자
        super().__init__()   # 부모생성자 호출
        self.W = tf.Variable(tf.random.normal([1])) # 기울기(가중치)
        self.B = tf.Variable(tf.random.normal([1])) # 절편
    def call(self, inputs):  # 메소드 재정의
        return inputs * self.W + self.B # 회귀방정식 예측치 반환

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
'''
mse = loss(model, inputs, outputs)
print("mse =", mse.numpy())

grad = gradient(model, inputs, outputs)
print("grad =", grad)
'''

# 6. 모델 최적화 객체
opt = tf.keras.optimizers.SGD(learning_rate=0.01)
print("초기 손실값 : {:.6f}".format(loss(model, inputs, outputs)))
print("w : {}, b : {}".format(model.W.numpy(), model.B.numpy()))

# 7. 반복학습
for step in range(300):
    grad = gradient(model, inputs, outputs) # 기울기 계산
    # 기울기 -> 최적화 객체 반영
    opt.apply_gradients(zip(grad, [model.W, model.B]))
    if (step+1) % 20 == 0:
        print("step = {}, loss = {:.6f}".format((step+1), loss(model, inputs, outputs)))

# 최적화된 변수들 조회
print("최적 손실값 : {:.6f}".format(loss(model, inputs, outputs)))
print("w : {}, b : {}".format(model.W.numpy(), model.B.numpy()))


'''
초기 손실값 : 58.644318
w : [-1.3348361], b : [-0.48785752]

step = 20, loss = 0.618525
step = 40, loss = 0.084454
step = 60, loss = 0.072375 주루룩

최적 손실값 : 0.022782
w : [1.8246958], b : [0.3985078]

'''

# 1 2 3을 넣어서 4 5 6이 나오게끔 학습시켰으니 테스트를 해봅시다
# 모델 테스트
y_pred = model.call(2.5) # x = 2.5
print("y_pred =", y_pred.numpy())
# y_pred = [4.960247]








    
    