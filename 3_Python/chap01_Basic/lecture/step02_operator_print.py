'''
연산자 : Operator
1. 변수에 값을 할당하는 방법 (=)
2. 연산자 : 산술, 관계, 논리
3. print 형식
4. input : 키보드 입력
'''

# 1. 변수에 값을 할당하는 방법 (=)
i = tot = 10
i += 1 # i = i + 1             # 카운터 변수
tot += i # tot = tot + i       # 누적 변수
print('i =', i)
print('tot =', tot)

v1, v2 = 100, 200  # 이렇게 넣는 것이 가능
print('v1 =', v1, 'v2 =', v2)
v1, v2 = v2, v1    # 이렇게 스왑이 가능

# 패킹(packing) 할당
lst = [1,2,3,4,5]  # vector : 1차원  = List (Not same with List in R)
v1, *v2 = lst  # v1에 하나, 나머지 v2에
print('v1 =', v1, 'v2 =', v2)

*v1, v2 = lst
print('v1 =', v1, 'v2 =', v2)  # 아까랑 반대


# 2. 연산자 : 산술, 관계, 논리
num1 = 100  # 피연산자1
num2 = 20.5   # 피연산자2
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div1 = num1 / num2
div2 = num1 // num2      # 정수만
div3 = num1 % num2       # 나머지만
square = num1**2
print(add, sub, mul)
print(div1, div2, div3)
print(square)

print("관계연산자")  # True or False
# 1) 동등비교
bool_re = num1 == num2  # 같다
print(bool_re)

bool_re = num1 != num2  # 같지않다
print(bool_re)

# 2) 대소 관계 : >, >=, <, <=
bool_re = num1 >= num2
print(bool_re)

bool_re = num1 <= num2
print(bool_re)

print("논리 연산자")  # or, and, not # R에서는 기호를 썼어야 했음
bool_re = num1 >= num2 or num1 <= 10  # 우선순위는 왼쪽, 얘가 트루면 걍 트루 폴스면 or 옆으로 넘어감
print(bool_re)

bool_re = num1 >= num2 and num1 <= 10  # 둘 다 맞아야 함
print(bool_re)

bool_re = not(num1 <= 10)  # False -> True
print(bool_re)


# 3. print 형식
help(print) # 함수 도움말
# 패키지 > 모듈 > function or class
# R에서는 패키지에서 바로 함수였는데 여기엔 모듈이 사이에 있음
# Help on built-in function print in module builtins:
# built-in : 기본 함수, module builtins : 기본 모듈
# 내장 기본 모듈(help)의 내장 기본 함수(print)다
# print(value, ..., sep = ' ', end = '\n'
"""
함수의 인수
매개변수 : (외부에서)값을 넘겨 받는 변수
파라미터 : (연산되지 전에 이미)값을 갖는 변수 sep라던가 end라던가
"""

# 1) 기본 인수
print("values = ", 10+20+30)  # values =  60
print("출력1", end=', ')    # end의 효과, 다음 값이 줄바껴서 출력안되게끔 설정함
print("출력2")              # 출력1, 출력2
print("010", "1111", "2222", sep = "-") # 010-1111-2222 지정한 구분자(sep)로 출력됨

# 2) format(value, '형식')
     # 지정한 양식문자로 출력되게끔 포맷을 정함 # 강의자료 22p

print("원주율=", format(3.14159, "8.3f") )
                               # 8 : 전체자릿수, 3 : 소수점 자릿수, 앞의 공백은 정수자리수 5중(5자리.3자리) 4칸

print("금액 =", format(10000, "10d"))
                             # 10자릿수로 + 10진수로
print("금액 =", format(125000, "3,d")) # 10진수에 세자리수마다 콤마

# 3) print("양식문자" %(값)) # 강의자료 22p
num1 = 10; num2 = 20
tot = num1 + num2
print("%d + %d = %d" %(num1, num2, tot)) # 10 + 20 = 30
# 각 자리에 일대일로
print("8진수 = %o, 16진수 = %x" %(num1, num1))
print("%s = %.4f" %("PI", 3.14159))
# 소수점 자리수는 %와 f 사이에 와야 함 : 강의자료22p가 틀림

# 4) 외부 상수 받기
# "{}, {}".format(value1, value2)
print("name : {}, age : {}".format("홍길동", 35))
# name : 홍길동, age : 35

print("name : {1}, age : {0}".format("홍길동", 35))
# 가로 안에다 집어넣을 순번을 정의할 수 있음 # 35, 홍길동
# 파이썬의 스타트 넘버는 0번임

# format 축약형
# select * from emp where name = '홍길동'
name = "홍길동"
age = 35
sql = f"select * from emp where name = '{name}' and age = {age}"
print(sql) # 따옴표 안에서도 외부의 함수를 적용시킬 수 있음 : 맨 앞의 f표시가 포인트

# 4. input("prompt") : 키보드 입력(문자로 인식하는 것이 기본값)
a = int(input("첫번째 숫자 입력 : ")) # 스트링 -> 인티져
b = int(input("두번째 숫자 입력 : "))
print("a + b = ", a + b)
# 문자로 인식하면 그냥 나열함 그래서 숫자로 변환하도록 int로 감싸줌

'''
형 변환 관련 함수들
int(value) : value -> integer(정수)
float(value) : value -> float(실수)
str(value) : value -> string
bool(value) : value -> T or F
'''

a = float(input("첫번째 숫자 입력 : "))
b = float(input("두번째 숫자 입력 : "))
print("a + b = ", a + b)
print('b=', b)
print(type(b))

# boolean -> int
print(int(False)) # 0으로 반환
print(int(True))  # 1로 반환

# int -> boolean
print(bool(-2))  # True : 0이 아닌 모든 값들에 해당
print(bool(0))  # False







