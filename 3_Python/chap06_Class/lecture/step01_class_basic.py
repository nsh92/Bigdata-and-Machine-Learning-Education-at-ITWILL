'''
클래스(class)
 - 함수의 모임
 - 역할 : 다수의 함수와 공유 자료를 묶어서 객체(object) 생성
 - 유형 : 사용자 정의 클래스, 라이브러리 클래스(python)
 - 구성 요소 : 멤버(member) + 생성자
 - 멤버(member) : 변수(자료 저장) + 메소드(자료 처리, 거의 함수와 동일)
 - 생성자 : 객체 생성
 형식)
 class 클래스명 :
    멤버변수 = 자료
    def 멤버메소드() : 자료 처리
    생성자 : 객체 생성
'''

# 1. 중첩합수와의 비교(5장)
def calc_func(a, b):   # outer : 자료 저장
    x = a
    y = b
    # inner : 자료 처리(조작)
    def plus():
        return x + y
    def minus():
        return x - y
    return plus, minus

p, m = calc_func(10, 20)  # 일급함수
print('plus = ', p())     # plus =  30
print('minus = ', m())    # minus =  -10
# 함수를 호출해야만 결과 값을 볼 수 있음

# 자료를 저장하는 곳, 처리하는 곳이 따로 따로
# 클래스는   멤버,    메소드
# 가장 중요한 것은 결과값으로 객체를 만들어낸다는 것임


# 2. 클래스 정의
class calc_class:
    # 멤버변수(클래스 안에서 통하는 전역변수) : 자료 저장할 곳을 정의
    x = y = 0
    # 생성자 : 객체 생성 + 멤버변수 값 초기화, 항상 이름이 정해져있음
    def __init__(self, a, b):        # self는 멤버가 접근하는 걸 연결시켜주는 매게체
        # 멤버변수 초기화
        self.x = a
        self.y = b
    # 멤버 메소드 : 클래스에서 정의한 함수, 함수 가로를 열면 셀프가 자동으로 지정됨, 셀프가 없으면 그 함수 안에서의 지역변수에 불과해짐
    def plus(self):
        return self.x + self.y
    def minus(self):
        return self.x - self.y
# self : 클래스 자기 자신을 의미함

# 클래스(1개) vs 객체(n개) : '1:n관계'
## 생성자 -> 객체1 생성
## calc_class() # 클래스명() : 생성자
obj1 = calc_class(10, 20)  # 객체를 만듦과 동시에 멤버 초기화
# obj1. 을 하면 호출할 수 있는 멤버가 보임 : plus, minus
# object.member() : 객체.멤버메소드 : 메소드 호출
print('plus = ', obj1.plus())     # plus =  30
print('minus = ', obj1.minus())   # minus =  -10
# object.member 이런 형태 : 멤버변수 호출(데이터만 부름)
print('x = ', obj1.x)   # x =  10
print('y = ', obj1.y)   # y =  20

# 하나의 클래스를 잘 만들어두면 여러 개의 객체를 만들어낼 수 있다

## 생성자 -> 객체2
obj2 = calc_class(100, 200)
print('plus = ', obj2.plus())    # plus =  300
print('minus = ', obj2.minus())  # minus =  -100
print('x = ', obj2.x)   # x =  100
print('y = ', obj2.y)   # y =  200


# 출처는 같지만 데이터는 다르기에 다른 객체가 만들어진다.
# 출처는 같지만 객체가 위치하는 주소값이 다르다
print(id(obj1), id(obj2))   # 1294225151880 1294225269960

obj3 = calc_class(100, 200)
print(id(obj1), id(obj2), id(obj3))  # 1294225151880 1294225269960 1294225271752
# 한 객체엔 그 객체에 담겨있는 데이터, 함수 정보가 담겨있음
# 그래서 클래스를 두고 설계도라 자주 말함

# 여기까지 했던 건 사용자 정의 클래스고

# 3. 라이브러리 클래스
from datetime import date   # from 모듈 import 클래스
today = date(2020, 4, 13)  # 생성자로 today객체 생성

# object.member : 객체에 달려있는 멤버들을 호출
print('year : ', today.year)
print('month : ', today.month)
print('day = ', today.day)

week = today.weekday()
print('week : ', week)  # 0 = 월요일











