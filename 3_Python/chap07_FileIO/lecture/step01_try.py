'''
예외 : 프로그램 실행 상태에서 예기치 않은 상황(오류)
try :
    예외 발생 코드
except :
    예외 처리 코드
finally :
    항상 처리 코드
'''

print('프로그램 시작')
x = [10, 20, 35.5, 15, 'num', 14.5]         # 저런 num같은 애들이 예외
for i in x:
    print(i)
    y = i ** 2
    print('y = ', y)
print('프로그램 종료')
# num에서 중단이 되고 오류 뜸
# 근대 14.5는 연산이 가능하지
# 어찌되었든 print('프로그램 종료') 이 구문도 실행이 가능했지


# 예외를 처리하도록 만들어보자 트라이부분은 그대로, 프로그램종료만 예외처리 블록으로 옮김
print('프로그램 시작')
x = [10, 20, 35.5, 15, 'num', 14.5]
for i in x:
    print(i)
    y = i ** 2
    print('y = ', y)

# 1. 간단한 예외처리
for i in x:
    try:
        print(i)
        y = i ** 2
        print('y = ', y)
    except:
        print('예외발생(숫자 ㄴㄴ) : ', i)
print('프로그램 종료')
# 끝까지 모든 구문이 실행되었음
# 예기치 않은 문제가 발생하더라도 되는데로 실행시키도록 하는 거임


# 2. 유형별 예외처리
print('유형별 예외처리')
try:
    div = 1000 / 2.5  # 정상
    print('div = %.3f'%div)
    div2 = 1000 / 0    # 당연히 비정상, 산술적 예외
    print('div = %.3f' % div2)
except ZeroDivisionError as e:     # 빌트인 클래스 : 0으로 나눴음을 설명하는
    print('예외발생', e)           # division by zero
finally:
    print('프로그램 종료')

## 파일 예외
print('유형별 예외처리')
try:
    div = 1000 / 2.5  # 정상
    print('div = %.3f'%div)
    #div2 = 1000 / 0
    #print('div = %.3f' % div2)
    f = open('c:/text.txt')  # 2차 예외 : 파일 열기 인데 그런 파일은 존재하지 않음
except ZeroDivisionError as e:  # class as object : 클래스에 의해 객체를 만듦
    print('예외발생', e)
except FileNotFoundError as e:
    print('예외발생 : ', e)     # [Errno 2] No such file or directory: 'c:/text.txt' : 이런 애 없다
finally:
    print('프로그램 종료')

## 기타 예외
print('유형별 예외처리')
try:
    div = 1000 / 2.5  # 정상
    print('div = %.3f'%div)
    #div2 = 1000 / 0
    #print('div = %.3f' % div2)
    #f = open('c:/text.txt')
    num = int(input('숫자입력해 : '))  # 3차 예외 : 기타 예외
    print('num = ', num)
except ZeroDivisionError as e:  # class as object : 클래스에 의해 객체를 만듦
    print('예외발생', e)
except FileNotFoundError as e:
    print('예외발생 : ', e)
except Exception as e:          # 기타 나머지 예외 처리 : 최상위 예외
    print('기타 예외발생 : ', e)  # invalid literal for int() with base 10: 'ㅋ', 물론 숫자를 넣으면 정상적으로 실행됨
finally:
    print('프로그램 종료')
# Exception : 기본 값임 except에 아무런 클래스를 지정하지 않으면 걍 설정되는 놈임
# 예외처리를 딱 순서대로 실행하기 때문에 Exception을 맨 앞에 넣으면 다른 예외처리가 의미가 없어진다
# 따라서 어떤 내용인지 보고싶으면 저렇게 구체적으로 지정하는 거임























