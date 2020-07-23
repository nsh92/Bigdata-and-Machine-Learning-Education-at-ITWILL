# -*- coding: utf-8 -*-
"""
python code vs tensorflow code
"""

# 파이썬 코드 : 직접 실행 환경
x = 10
y = 20
z = x + y
print("z = ", z)

import tensorflow.compat.v1 as tf # 1.x버전 임포트
tf.disable_v2_behavior()          # 2.x버전 안쓰겠다
print(tf.__version__)

''' 프로그램 정의 영역 '''
x = tf.constant(10) # 상수를 정의함
y = tf.constant(20) # 또 다른 상수를 정의함
z = x + y
# 식을 정의함
print("z = ", z)
# z =  Tensor("add_2:0", shape=(), dtype=int32)
# 30이 아닌 텐서 정보 결과가 뜸 : 아직 연산 안 함
print(x, y)
# Tensor("Const_2:0", shape=(), dtype=int32) Tensor("Const_3:0", shape=(), dtype=int32)
# 얘내도 아직 10, 20이 아님
# 디바이스에 할당 안 된 상태

# session
sess = tf.Session() # 프로그램에서 정의한 상수, 변수, 식을 device(CPU, GPU, TPU)에 할당하는 역할

''' 프로그램 실행 영역 '''
print("x = ", sess.run(x))
print("y = ", sess.run(y))
print("z = ", sess.run(z)) # x, y 상수 참조 -> 연산
sess.run(x, y) # 오류 발생 : 하나의 세션 안에서 여러 상수 식 ㄴㄴ함
sess.run([x, y]) # 이렇게는 가능
x_val, y_val = sess.run([x, y])
print(x_val, y_val)

# 객체 닫기
sess.close()































