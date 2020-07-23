'''
 문4) 팩토리얼(Factorial) 계산 함수를 정의하시오.
     예) 5! -> 5*4*3*2*1 : 120
'''

def Factorial(n):
    if n == 1:
        return 1
    else:
        result = n * Factorial(n-1)
        print(result, end=' ')
        return result

    


print('팩토리얼 결과:', Factorial(5)) #  팩토리얼 결과: 120


