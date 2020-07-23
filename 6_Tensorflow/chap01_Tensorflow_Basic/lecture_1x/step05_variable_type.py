# -*- coding: utf-8 -*-
"""
step05_variable_type

Tensorflow 변수 유형
 1. 초기값을 갖는 변수 : Fetch 방식
    변수 = tf.Variable(초기값)
 2. 초기값이 없는 변수 : Feed 방식
    변수 = tf.placeholder(dtype, shape)
"""
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior()

# 상수 정의
x = tf.constant(100.0)
y = tf.constant(50.0)

# 식 정의
add = tf.add(x, y)  # 150 = 100 + 50

# 변수 정의
var1 = tf.Variable(add) # Fetch방식 : 초기값
var2 = tf.placeholder(dtype = tf.float32) # Feed방식 : 초기값없음 : 값이 없으니 실행시점에서 넣어줘야 함

# 변수 참조하는 식
mul = tf.multiply(x, var1)
mul2 = tf.multiply(x, var2)

with tf.Session() as sess:
    print("add =", sess.run(add)) # 식 실행
    sess.run(tf.global_variables_initializer())  # 변수 초기화 : 구체적으로 Fetch에 대하여 의미있는 것
    print("var1 =", sess.run(var1)) # 변수
    print("var2 =", sess.run(var2, feed_dict = {var2 : 150}))  # feed_dict = {변수 : 값}
    
    mul_re = sess.run(mul) # 상수와 변수 참조
    print("mul =", mul_re)
    
    # feed 방식의 연산 수행
    mul_re2 = sess.run(mul2, feed_dict = {var2 : 150})
    print("mul2 =", mul_re2)

    print("var2 =", sess.run(var2, feed_dict = {var2 : [1.5,2.5,3.5]})) # 이렇게도 가능 # [1.5 2.5 3.5]
    mul_re3 = sess.run(mul2, feed_dict = {var2 : [1.5,2.5,3.5]})
    print("mul2 =", mul_re3) # [150. 250. 350.]

    























