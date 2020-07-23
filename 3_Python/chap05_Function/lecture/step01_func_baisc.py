'''
함수
 - 중복 코드 제거
 - 재사용 가능
 - 특정 기능 1개 정의
 - 유형) 사용자 정의 함수, 라이브러리 함수
'''

# 1. 사용자 정의 함수
'''
형식)
def 함수명(매개변수):
    실행문
    실행문
    return 값1, 값2, ...   # R에선 하나의 값만, 필요하다면 데이터프레임으로 출력시키도록 해야 했음
    ## 리턴 값이 딱히 없다면 생략 가능 
'''

## 1) 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')
             # 함수를 정의해놓고
userFunc1()  # 함수를 호출한다

## 2) 인수(매개변수)가 있는 함수
def userfunc2(x, y):
    adder = x + y
    print('adder =', adder)

userfunc2(10,20)  # adder = 30

## 3) 리턴이 있는 함수
# 위에선 출력만 해줬는데 나온 값을 어딘가에 적재시키고 싶다
def userFunc3(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div

userFunc3(100,20)  # 암 것도 안뜸
a, s, m, d = userFunc3(100,20)  # 적재시킬 곳 지정, R에선 저 객체들을 df로 묶음
print('add = ', a)
print('sub = ', s)
print('mul = ', m)
print('div = ', d)


# 2. 라이브러리 함수
'''
1) built-in : 내장함수 or 기본함수
2) import : 모듈, 함수()
'''

## 1) built-in : 내장함수 or 기본함수
dataset = list(range(1,6))
print(dataset)  # [1, 2, 3, 4, 5]

print('sum = ', sum(dataset))  # 빌트인이라 바로 쓸 수 있음
print('max = ', max(dataset))
print('min = ', min(dataset))
print('len = ', len(dataset))

print(mean(dataset))  # 얘는 오류뜸 : 빌트인이 아니라서 : 관련 모듈을 임포트해야 함

## 2) import : 모듈.함수()
### 모듈 가져오는 방법1
import statistics  # 수학 통계 관련 모듈  # 컨트롤을 누른체로 커서를 대면 모듈 링크로 갈 수 있음 : 오픈소스
statistics.mean()  # 이렇게 해야 쓸 수 있음

### 모듈 가져오는 방법2
from statistics import mean
mean() # 가능해짐

print(dir(statistics))
# 해당 모듈의 정보
# __이런애들은 클래스 내에서 쓰는 거
# 맨 끝에서부터 봐야 쓸 함수들이 보임















