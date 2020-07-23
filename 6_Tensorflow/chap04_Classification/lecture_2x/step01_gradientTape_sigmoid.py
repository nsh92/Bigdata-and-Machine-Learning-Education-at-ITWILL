# -*- coding: utf-8 -*-
"""
step01_gradientTape_sigmoid.py

GradientTape + Sigmoid
"""
import tensorflow as tf
tf.executing_eagerly()


# 1. x, y 공급 data 
# x변수 : [hours, video]
inputs = tf.Variable([[1., 2.], [2., 3.], [3., 1.], [4., 3.], [5., 3.], [6., 2.]]) # [6,2]

# y변수 : binary data (fail or pass)
outputs = tf.Variable([[0.], [0], [0], [1], [1], [1]]) # [6,1] 점은 하나만 찍어도 저 형식으로 인식함

# 2. model : model class
class Model(tf.keras.Model): # 자식클래스(부모클래스)
    def __init__(self):      # 생성자
        super().__init__()   # 부모생성자 호출
        self.W = tf.Variable(tf.random.normal([2, 1])) # 기울기[입력,출력]
        self.B = tf.Variable(tf.random.normal([1])) # 절편[출력]
    def call(self, inputs):  # 메소드 재정의
        return tf.matmul(inputs, self.W) + self.B # 회귀방정식 예측치 반환

# 3. 손실 함수
def loss(model, inputs, outputs):
    sigmoid = tf.sigmoid(model(inputs))
    return -tf.reduce_mean(outputs * tf.math.log(sigmoid) + (1-outputs) * tf.math.log(1-sigmoid)) # Cross Entropy

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
opt = tf.keras.optimizers.Adam(learning_rate=0.001)
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


# 모델 테스트
sigmoid = tf.sigmoid(model.call(inputs))
pred = tf.cast(sigmoid > 0.5, tf.float32)

y_true = tf.squeeze(outputs)
y_pred = tf.squeeze(pred)

print("pred : ", y_pred.numpy())
print("outputs : ", y_true.numpy())





















