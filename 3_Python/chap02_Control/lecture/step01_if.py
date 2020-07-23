'''
제어문 : 조건문(if), 반복문(while, for)
python 블럭 : 콜론과 들여쓰기

형식1)
if 조건식 :
    실행문
    실행문
'''

var = 10
if var >= 15 :
    print('var =', var)
    print('var는 10보다 크거나 같다.')

print('항상 실행되는 영역')


'''
형식2)
if 조건식 :
    실행문1
else :
    실행문2
'''
var = 2
if var >= 5 :
    print('var는 5보다 크거나 같다')
else :
    print('var는 5보다 작다')
# answer : var는 5보다 작다

# 키보드 점수 입력 -> 60점 이상 합격 미만 불합격
score = int(input("점수 입력 : "))
if score >= 60 :
    print('합격')
else :
    print('불합격')

import datetime # 모듈 임포트 날짜 시간관리
today = datetime.datetime.now()   # 모듈.클래스.method() or 함수()
print(today)

# 요일 반환
week = today.weekday()
print(week) # 0 ~ 4 평일, 5 ~ 6 휴일
if week >= 5 :
    print("오늘은 휴일")
else :
    print("오늘은 평일")

'''
if 조건식1 :
    실행문1
elif 조건식2 :
    실행문2
else :
    실행문3
'''

# 문2) 키보드 score 입력받음 : A(100~90), B(80), C, D, F(59 미만) 학점
score = int(input("점수 입력(0~100) : "))
if score >= 90 :
    print("A학점")
elif score >= 80 :
    print("B학점")
elif score >= 70 :
    print("C학점")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")

# 이런식으로도 가능함  # 전역변수 : score, grade : 특정한 블록에서도 사용, 범위를 벗어나서도 사용됨
score = int(input("점수 입력(0~100) : "))
grade = ""
if score >= 90 :
    grade = "A학점"
elif score >= 80 :
    grade = "B학점"
elif score >= 70 :
    grade = "C학점"
elif score >= 60 :
    grade = "D학점"
else :
    grade = "F학점"

print("당신의 점수는 %d이고, 등급은 %s이다."%(score, grade))


# 블록형 if  vs  라인형 if

## 블록형 if
num = 9
if num >= 5 :
    result = num * 2
else :
    result = num + 2

print(result)

## 라인형 if
## 형식) 결과를저장할변수 = 참 if 조건문 else 거짓
result = num * 2 if num >= 5 else num + 2
print(result)















