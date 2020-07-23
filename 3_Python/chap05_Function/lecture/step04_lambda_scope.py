'''
1. 축약함수(lambda)
 - 한 줄 함수
 형식) 변수 = lambda 인수 : 리턴값
 ex) lambda x,y : x+y

2. scope
 - 전역변수 (함수 밖에서도 됨)
 - 지역변수 (함수 내에서만 쓰이는)
'''

# 1. 축약함수
def adder(x,y):
    add = x+y
    return add
    # 일반적인 블록형 함수

add = lambda x, y: x + y

# 리스트내포를 갖다
# [실행문 for 변수 in 열거형객체]
# [add = lambda x, y: x + y for 변수 in 열거형객체]
# 이렇게 가능해짐

re = add(10, 20)
print(re)


# 2. scope
'''
전역변수 : 전 지역에서 사용되는 변수
지역변수 : 특정 지역(함수)에서만 사용되는 변수
'''

x = 50 # 전역변수

def local_func(x):
    x += 50

local_func(x)

print('x=', x)
# 50을 더했는데 여전히 50임
# 따라서 local_func(x) 안에서 50이 더해지는 x는
# 저 함수가 끝나면 자동으로 소멸된 거임

def global_func():
    global x         # x를 전역변수로 써라
    x += 50

global_func()
print('x=', x)
# 바깥에 있었던 x를 썼고, 소멸되지 않고 그대로, 100으로 존재
# 글로벌 설정이 없으면 알아서 지역변수 취급됨






