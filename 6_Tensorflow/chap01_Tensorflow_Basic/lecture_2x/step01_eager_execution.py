# -*- coding: utf-8 -*-
"""
step01_eager_execution 즉시 실행 환경
 - 텐서플로우2.0 특징
   1. 즉시 실행 모드
      - session object 없이 즉시 실행 환경(auto graph)
      - 파이썬 실행 환경과 동일함
      - API 정리 : tf.global_variables_initializer() 삭제

"""
import tensorflow as tf # 2.0 임포트
print(tf.__version__)   # 2.0.0


# 상수 정의
a = tf.constant([[1, 2, 3], [1.0, 2.5, 3.5]])
print("a : ")
print(a)
'''
a : 
tf.Tensor(
[[1.  2.  3. ]
 [1.  2.5 3.5]], shape=(2, 3), dtype=float32)
텐서정보만 나오지 않고 결과까지 출력 : 즉시 실행 환경
'''
print(a.numpy())
#[[1.  2.  3. ]
# [1.  2.5 3.5]] 알맹이(상수)만 조회


# 식 정의 : 상수 참조 -> 즉시 연산
b = tf.add(a, 0.5)
print("b :")
print(b)


# 변수 정의
x = tf.Variable([10,20,30])
y = tf.Variable([1,2,3])
print(x.numpy())
print(y.numpy())
mul = tf.multiply(x, y)
print(mul)


# 파이썬 코드 -> 텐서플로우 즉시 실행
x = [[2.0, 3.0]]   # (1,2)가 되는 중첩리스트
a = [[1.0], [1.5]] # (2, 1)

# 행렬곱 연산
mat = tf.matmul(x, a)
print("matrix multiply = {}".format(mat)) 
# matrix multiply = [[6.5]]



'''lecture_1x의 step02_tf_variable -> 버전2'''
''' 프로그램 정의 영역 '''
print("~~ 즉시 실행 ~~")
# 상수 정의
x = tf.constant([1.5, 2.5, 3.5], name = 'x') # 1차원 : 수정 불가

# 변수 정의
y = tf.Variable([1.0, 2.0, 3.0], name = 'y') # 1차원 : 수정 가능

# 식 정의
mul = x * y # 상수 * 변수

''' 프로그램 실행 영역 '''
print("x =", x.numpy()) 
print("y =", y.numpy()) 

# 식 할당 : 연산
print("mul =", mul.numpy()) # mul = [ 1.5  5.  10.5]
# 뭐 대충 많이 간소화되었음











