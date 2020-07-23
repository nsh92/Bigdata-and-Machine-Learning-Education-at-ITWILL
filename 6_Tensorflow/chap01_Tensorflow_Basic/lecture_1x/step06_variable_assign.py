# -*- coding: utf-8 -*-
"""
step06_variable_assign

난수 상수 생성 함수 : 정규분포 난수, 균등분포 난수
tf.Variable(난수 상수) -> 변수 값 수정
"""
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior()


# 난수
num = tf.constant(10.0)

# 0차원 변수
var = tf.Variable(num + 20.0) # 상수 + 상수 = scala
print("var =", var) # var = <tf.Variable 'Variable:0' shape=() dtype=float32_ref>

# 1차원 변수
var1d = tf.Variable(tf.random_normal([3])) # 1차원 : [n]
print("var1d =", var1d) # var1d = <tf.Variable 'Variable_1:0' shape=(3,) dtype=float32_ref>

# 2차원 변수
var2d = tf.Variable(tf.random_normal([3,2])) # 2차원 : [r,c]
print("var2d =", var2d) # var2d = <tf.Variable 'Variable_2:0' shape=(3, 2) dtype=float32_ref>

# 3차원 변수
var3d = tf.Variable(tf.random_normal([3,2,4])) # 3차원 : [side, row, col]
print("var3d =", var3d) # var3d = <tf.Variable 'Variable_21:0' shape=(3, 2, 4) dtype=float32_ref>

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init) # 변수 초기화
    
    print("var =", sess.run(var))
    print("var1d =", sess.run(var1d))
    print("var2d =", sess.run(var2d)) 
    
    # 변수의 값 수정
    var1d_data = [0.1, 0.2, 0.3]
    print("var1d assign =", sess.run(var1d.assign(var1d_data)))
    #print("var1d_assign_add =", sess.run(var1d.assign_add(0.01)))
    
    print("var3d =", sess.run(var3d))
    var3d_re = sess.run(var3d)
    print(var3d_re[0].sum())
    print(var3d_re[0,0].mean())

    # 24개 균등분포난수를 생성하여 var3d 변수 값 수정하기
    var3d_data = tf.random_uniform([3,2,4])
    print("var3d assign =", sess.run(var3d.assign(var3d_data)))




















