'''
재귀 호출 : 자기 자신을 반복적으로 부른다 : recursive call
 - 함수 내에서 자신의 함수를 반복적으로 호출하는 기법
 - 반복적으로 변수의 값을 조정해서 연산 수행
 ex) 1 ~ n (1+2+3+4...n)
 - 반드시 종료조건을 필요로 함
'''

# 1. 카운터 관련 재귀 호출 : 1 ~ n
def Counter(n):
    if n == 0:        # 종료 조건
        print("프로그램 종료")
        return 0      # 0이라는 값을 반환하고 함수 종료
    else:
        Counter(n-1)       # 1. 재귀 호출
        '''
        1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1), 1(2-1)] 처음에 5가 들어오고 4번의 재귀호출, 0(1-1)은 여기에 저장 안댐
        2. stack 역순으로 출력
        '''
        print(n, end=' ')  # 2. 카운트 : 1 2 3 4 5

print(Counter(0))  # 0
(Counter(5))  # 1 2 3 4 5

print()
# 2. 누적(1 + 2 + 3 + ...~ + n) 재귀 호출
def Adder(n):
    if n == 1:
        return 1
    else:
        result = n + Adder(n-1)  # 재귀 호출   ->  누적
        '''
        stack : 후입선출 LIFO
        1. stack[5(first), 4(5-1), 3(4-1), 2(3-1)] 1(2-1)얘는 밖으로
        2. stack에 역순으로 값이 누적됨 : 1+[2+3+4+5]      밖으로 갔었지만 맨 앞으로 보내져서 더해짐
        '''
        print(result, end=' ')
        return result

print(Adder(1))  # 1을 반환
print(Adder(5))  # 15 : 3 6 10 15
print(Adder(10))
