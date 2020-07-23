'''
중첩함수(inner function)

형식)
def outer_function(인수):
    실행문
    def inner_func(인수):
        실행문
    return inner_func
'''

# 1. 중첩합수 예
def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b  # inner func

a()  # outer 호출
# <function a.<locals>.b at 0x000001AC24297708>
# 함수a의 inner함수b 가 나옴

b() # 이것만 하면 오류뜸

b = a()  # outer 호출 - a 함수 = 일급함수
b()      # inner 호출

# 2. 중첩 함수 응용
'''
inner 함수 종류
getter() : 함수 내의 data를 외부 획득자  :  외부 반환  : 어떤 데이터가 들어갔었는지 알려줌
setter() : 함수 내의 data를 지정자  :  함수 내에 받은 data를 새롭게 세팅
'''
def outer_func(data):  # 역할 : 데이터 저장, inner 포함
    dataSet = data

    # inner : 데이터 조작
    def tot():  # 합계
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):  # 평균 = 합계/n
        avg_val = tot_val / len(dataSet)
        return avg_val

    return tot, avg

data = list(range(1,101))
tot, avg = outer_func(data)  # 일급함수(tot,avg)

tot_val = tot()   # 합계 계산
avg_val = avg(tot_val)   # 평균 계산
print('tot =', tot_val)  # tot = 5050
print('avg =', avg_val)  # avg = 50.5

# 위 함수에 getter 추가
def outer_func(data):  # 역할 : 데이터 저장, inner 포함
    dataSet = data

    # inner : 데이터 조작
    def tot():  # 합계
        tot_val = sum(dataSet)
        return tot_val

    def avg(tot_val):  # 평균 = 합계/n
        avg_val = tot_val / len(dataSet)
        return avg_val

    # getter
    def getData():
        return dataSet
    return tot, avg, getData

data = list(range(1,101))
tot, avg, getData = outer_func(data)  # 이번엔 배출하는 것이 3개겠지
print('tot =', tot_val)
print('avg =', avg_val)
print('dataset = ', getData)  # dataset 반환

# 위 함수에 setter 추가
def outer_func(data):  # 역할 : 데이터 저장, inner 포함
    dataSet = data

    # inner : 데이터 조작
    def tot():  # 합계
        tot_val = sum(dataSet)
        return tot_val

    def avg(tot_val):  # 평균 = 합계/n
        avg_val = tot_val / len(dataSet)
        return avg_val

    # getter
    def getData():
        return dataSet

    # setter
    def setData(newData):
        nonlocal dataSet
        dataSet = newData    # 회색 : 지역변수다 그래서 nonlocal로 전역변수로 교체 : outer로 인식되게끔

    return tot, avg, getData, setData

data = list(range(1,101))
newData = list(range(1,51))
setData(newData)

# getter 이용 : dataset이 바뀌었는지 확인
print('dataSet =', newData)

tot, avg, getData, setData = outer_func(data)  # 이번엔 배출하는 것이 4개겠지 (일급함수의 수)
print('tot =', tot_val)
print('avg =', avg_val)
print('dataset = ', getData)  # dataset 반환

# 참조만 하는 것과 바꿔버리는 것을 잘 구분하자자


# 3. 함수 장식자 : Tensorflow2.0에서 적용
# - 기존 함수의 시작부분과 종료부분에 기능을 추가해서 장식 역할
'''
@ 함수장식자
def 함수명():
    실행문
'''

# 함수장식자 작성
def hello_deco(func):  # outer : 함수를 인수로 받음
    def inner():       # inner인데 장식하는 역할임
        print('-' * 20)  # 함수 앞부분 데코
        func()         # 함수 실행
        print('-' * 20)  # 함수 뒷부분 데코
    return inner
## ---무더기로 장식해주는 함수를 만듬

@hello_deco  # @가 연결시켜줌
def hello():
    print("my name is 남승현!!")

# 장식되는지 확인
hello()
# --------------------
# my name is 남승현!!
# --------------------

# 이걸 응용해보자
# 구체적으로 연결될 수 있게 inner와 func에 변수 지정
def hello_deco(func):  # outer : 함수를 인수로 받음
    def inner(name):       # inner인데 장식하는 역할임
        print('-' * 20)  # 함수 앞부분 데코
        func(name)         # 함수 실행
        print('-' * 20)  # 함수 뒷부분 데코
    return inner

# 원하는 와꾸와 연결될 수 있는 변수 지정
@hello_deco  # @가 연결시켜줌
def hello(name):
    print("my name is " + name + "!!")

hello('아이유')
hello('홍길동')

# 응용) 구구단 장식하기
'''
**** 2단 ****
2 * 1 = 2
주루룩
2 * 9 = 18
*************
'''
# 구구단 장식
def gugu_deco():
    pass
# 구구단 계산
def gugu():
    pass

dan = int(input("단 입력 : "))
gugu(dan)


def gugu_deco(func):
    def inner(dan):
        print("****", dan, "단 ****")         # 교수님은 ("****", {}단, "단 ****".format(dat))
        func(dan)
        print("*" * 16)
    return inner

@gugu_deco
def gugu(dan):
    for i in range(1,10):
        print("  %d * %d = %d"%(dan, i, dan*i))

dan = int(input("단 입력 : "))
gugu(dan)

# 정확히 꾸며준다기 보다 해당하는 함수에
# 앞단에 뭘 넣고 뒷단에 뭘 넣어서 더 완성도있게끔 해주는 것임






