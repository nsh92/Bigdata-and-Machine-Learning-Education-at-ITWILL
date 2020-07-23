# -*- coding: utf-8 -*-
"""
step02_gradientTape_softmax.py

- GradientTape + Softmax
"""
import tensorflow as tf
tf.executing_eagerly()


# 1. x, y 공급 data 
# [털, 날개]
inputs = tf.Variable(
    [[0., 0.], [1, 0], [1, 1], [0, 0], [0, 1], [1, 1]]) # [6, 2]

# [기타, 포유류, 조류] : [6, 3]  -> one hot encoding : 1과 0으로 표시
outputs = tf.Variable([
    [1., 0., 0.],  # 기타[0]
    [0, 1, 0],     # 포유류[1]
    [0, 0, 1],     # 조류[2]
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 1]
])

# 2. model : model class
class Model(tf.keras.Model): # 자식클래스(부모클래스)
    def __init__(self):      # 생성자
        super().__init__()   # 부모생성자 호출
        self.W = tf.Variable(tf.random.normal([2, 3])) # 기울기[입력,출력]
        self.B = tf.Variable(tf.random.normal([3])) # 절편[출력]
    def call(self, inputs):  # 메소드 재정의
        return tf.matmul(inputs, self.W) + self.B # 회귀방정식 예측치 반환

# 3. 손실 함수
def loss(model, inputs, outputs):
    softmax = tf.nn.softmax(model(inputs))
    return -tf.reduce_mean(outputs * tf.math.log(softmax) + (1-outputs) * tf.math.log(1-softmax)) # Cross Entropy

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
opt = tf.keras.optimizers.Adam(learning_rate=0.01)
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
y_true = tf.argmax(outputs, axis=1) # 정답 2진수 -> 10진수 디코딩
y_pred = tf.argmax(tf.nn.softmax(model.call(inputs)), axis=1)  # 0~1 확률값 -> 10진수 디코딩

print("정답 :", y_true.numpy())
print("예측치 :", y_pred.numpy())
'''
최적 손실값 : 0.073713
w : [[-2.7708268  3.6349316  2.3955162]
 [ 1.3302442 -1.3148247  2.9133623]], b : [ 1.1513255 -2.2335455 -2.6571314]
정답 : [0 1 2 0 0 2]
예측치 : [0 1 2 0 0 2]
'''
