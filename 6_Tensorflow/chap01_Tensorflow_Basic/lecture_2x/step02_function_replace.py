# -*- coding: utf-8 -*-
"""
step02_function_replace
 - 텐서플로우2.0 특징
   2. 세션 대신 함수
      - ver2.0 : 파이썬 함수 사용 권장
      - API 정리 : tf.placeholder(dtype, shape) 삭제 : 함수 인수로 대체
                   tf.random_uniform -> tf.random.uniform()
                   tf.random_normal -> tf.random.normal()
"""
import tensorflow as tf

# lecture1x_step07 -> ver2.0
# 처음부터 session부분 날림
'''
'''변수 정의'''
a = tf.placeholder(dtype=tf.float32)            # 가변형
b = tf.placeholder(dtype=tf.float32)            # 가변형
c = tf.placeholder(dtype=tf.float32, shape=[5]) # 고정형
d = tf.placeholder(dtype=tf.float32, shape=[None,3]) # 고정형 : 2d(행 가변)

c_data = tf.random_uniform([5])

# 식 정의
mul = tf.multiply(a, b)
add = tf.add(mul, 10)
c_calc = c * 0.5  # vector * scala
'''

def mul_fn(a, b):  # tf.placeholder() -> 인수 대체
    return tf.multiply(a, b)

def add_fn(mul):
    return tf.add(mul, 10)

def c_calc_fn(c):
    return tf.multiply(c, 0.5)

# data 생성
a_data = [1.0, 2.5, 3.5]
b_data = [2.0, 3.0, 4.0]

mul_re = mul_fn(a_data, b_data)
print(mul_re.numpy())
print(add_fn(mul_re))

# tf.random_uniform() : 버전1 : 얘도 api 정리
c_data = tf.random.uniform(shape=[3,4], minval=0, maxval=1)
print(c_data)
print(c_calc_fn(c_data).numpy())










