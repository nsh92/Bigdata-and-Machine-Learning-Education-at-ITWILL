# -*- coding: utf-8 -*-
"""
step02_tf_variable
 - 변수 정의와 초기화
 - 상수 vs 변수
 - 상수 : 수정 불가, 초기화 필요 없음
 - 변수 : 수정 가능, 초기화 필요

"""
import tensorflow.compat.v1 as tf # 1.x버전 임포트
tf.disable_v2_behavior()  

'''프로그램 정의 영역 '''
# 상수 정의
x = tf.constant([1.5, 2.5, 3.5], name = 'x') # 1차원 : 수정 불가
print(x)
# 변수 정의
y = tf.Variable([1.0, 2.0, 3.0], name = 'y') # 1차원 : 수정 가능
print(y)
# 식 정의
mul = x * y # 상수 * 변수

# graph = node(연산자 : +-*/) + edge(데이터 : x, y)
# tensor : 데이터의 자료구조(scala(0), vector(1), matrix(2), array(3), n-array)

sess = tf.Session()

'''프로그램 실행 영역 '''
print("x =", sess.run(x)) # x = [1.5 2.5 3.5] 상수 할당
print("y =", sess.run(y)) # 오류 뜸 : 변수가 초기화되지 않았다는 의미
# 변수 초기화
init = tf.global_variables_initializer() # 초기화라는 모듈을 init이란 객체화
sess.run(init) # 이렇게 초기화 함
print("y =", sess.run(y)) # y = [1. 2. 3.] 

# 식 할당 : 연산
mul_re = sess.run(mul)
print("mul =", mul_re) # mul = [ 1.5  5.  10.5]
type(mul_re) # numpy.ndarray 텐플은 넘파이랑 궁합이 잘 맞음
mul_re.sum()






sess.close()
