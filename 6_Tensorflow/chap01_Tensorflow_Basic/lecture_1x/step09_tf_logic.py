# -*- coding: utf-8 -*-
"""
step09_tf_logic
 - if, while 형식 
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


# 1. if문
x = tf.constant(10)
'''
y = tf.cond(pred, true_fn, false_fn)
- 파라미터들
  pred : 조건식 
  true_fn : 조건식이 참인 경우 수행하는 함수(인수없음)
  false_fn : 조건식이 거짓인 경우 수행하는 함수(인수없음)
  조건식은 보통 미리 Def함
'''
def true_fn():
    return tf.multiply(x, 10) # x*10

def false_fn():
    return tf.add(x, 10) # x+10

y = tf.cond(x > 100, true_fn, false_fn)

sess = tf.Session()

print("y = ", sess.run(y)) # y =  20


# 2. while 
i = tf.constant(0) # i = 0 : 반복변수
'''
loop = tf.while_loop(cond, body, (i,))
- 파라미터들
  cond : 조건문(호출가능한 함수)
  body : 반복문(호출가능한 함수)
  loop_vars : 반복변수(튜플 or 리스트)
'''
loop = tf.while_loop(cond, body, (i,))
def cond(i):
    return tf.less(i, 100) # less : < : i가 100보다 작을때까지

def body(i):
    return tf.add(i, 1)    # i = i + 1

sess = tf.Session()
print("y = ", sess.run(y))       # y =  20
print("loop = ", sess.run(loop)) # loop =  100
























