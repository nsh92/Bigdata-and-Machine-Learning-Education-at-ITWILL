# -*- coding: utf-8 -*-
"""
step03_@tf.function.py
 - 텐서플로우2.0 특징
   3. @tf.function 함수 장식자(데코레이터)
      - 이점 : 
        -> 파이썬 코드 => 텐서플로우 코드 변환(auto graph)
        -> 로직 처리 : 쉬운 코드 대체
        -> 속도 향상
"""
import tensorflow as tf

''' step09 -> 버전2
# 1. if문
x = tf.constant(10)

def true_fn():
    return tf.multiply(x, 10) # x*10

def false_fn():
    return tf.add(x, 10) # x+10

y = tf.cond(x > 100, true_fn, false_fn)

sess = tf.Session()

print("y = ", sess.run(y)) # y =  20

# 2. while 
i = tf.constant(0) # i = 0 : 반복변수

loop = tf.while_loop(cond, body, (i,))
def cond(i):
    return tf.less(i, 100) # less : < : i가 100보다 작을때까지

def body(i):
    return tf.add(i, 1)    # i = i + 1

sess = tf.Session()
print("y = ", sess.run(y))       # y =  20
print("loop = ", sess.run(loop)) # loop =  100
'''

@tf.function
def if_func(x):
    if x > 100:
        y = x * 10
    else :
        y = x + 10
    return y

x = tf.constant(10)

print("y =", if_func(x).numpy()) # y = 20


@tf.function
def while_func(i):
    while i < 100:
        i += 1
    return i

i = tf.constant(0)
print("loop =", while_func(i).numpy()) # loop = 100





















