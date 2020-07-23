'''
반복문(while)

while 조건식 :
    실행문
    실행문

'''

# 카운터, 누적 변수
cnt = tot = 0  # 변수 초기화

while cnt < 5 :  # 트루 확인 -> 루프(명령문 집합) 실행
    cnt += 1  # 카운터 변수
    tot += cnt  # 누적
print(cnt, tot)

# 1 ~ 100 합 ㄱㄱ
cnt = tot = 0
while cnt < 100 :
    cnt += 1
    tot += cnt
print(cnt, tot)

cnt = tot = 0
data = [] # empty list (짝수를 저장할 것임)
while cnt < 100 :
    cnt += 1
    tot += cnt
    if cnt % 2 == 0:
        data.append(cnt)  # data객체에 짝수 값을 넣음

print("1~100까지 합 : %d"%(tot))
print("짝수 값 :", data)

# 문2) 1~100 사이에서 5의 배수면서 3의 배수가 아닌 값만 appned하기
cnt = 0
data = []
while cnt < 100 :
    cnt += 1
    if cnt % 5 == 0 and cnt % 3 != 0 :
        data.append(cnt)
print(data)
len(data)

# 무한 루프Loop -> 종료 조건이 필요
while True :
    num = int(input("숫자 입력 : "))
    if num == 0 :
        print("프로그램 종료")
        break  # 탈출(exit) : 종료 조건
print("num =", num)
# 0을 넣어줄 때까지 계속 물어봄

# random : 난수 생성
import random  # 난수 생성 모듈
help(random.random)   # 0 ~ 1 난수 실수
help(random.choice)
help(random.randint)  # 난수 정수

r = random.random()  # 모듈.함수(0~1 난수 생성)
print('r=', r)

# 문3) 난수 0.01 미만이면 프로그램 종료, 아니면 난수 개수 출력
num=0
while True :
    num = random.random()
    if num < 0.01 :
        print("프로그램 종료")
        break  # 탈출(exit) : 종료 조건
    else :
        cnt += 1
print('난수 개수 =', cnt)

r = random.randint(1,5)  # 1~5 사이의 난수 정수
print(r)

print(">>> 숫자 맞추기 게임 <<<")
'''
숫자범위 : 1 ~ 10
myInput == computer : 성공(exit) -> 종료 조건
myInput > computer : '더 작은 수 입력'
myInput < computer : '더 큰 수 입력'
'''
myInput = computer = 0
computer = random.randint(1,10)
while True :
    myInput = int(input("예상 숫자 입력 : "))  # 사용자 입력
    if myInput == computer :
        print('성공')
        break
    elif myInput > computer :
        print('~~ 더 작은 수 입력 ~~')
    else : print('~~ 더 큰 수 입력 ~~')


'''
continue  vs  break
 - 반복문에서 사용되는 명령어
 - continue : 반복을 지속, 다음 문장 skip
 - break : 반복을 멈춤
'''

i = 0
while i < 10 :
    i += 1

    if i == 3 :
        continue  # 다음 문장은 skip
    if i == 6 :
        break
    print(i, end='  ')

# 정상적인 결과는 1~10출력인데 if continue break가 1 2 4 5만 출력되도록 제어함
# 3은 continue에 걸려서 출력안됐음







