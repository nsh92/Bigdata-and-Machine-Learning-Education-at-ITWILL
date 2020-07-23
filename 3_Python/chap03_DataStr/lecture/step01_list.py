'''
list 특징
- 1차원 배열 구조
  형식) 변수 = [값1, 값2, ...]       (이더러블)

- 다양한 자료형 저장 가능

- index 사용, 순서 존재
  형식) 변수[index], index = 0

- 값 수정(추가, 삽입, 수정, 삭제)
'''

# 1. 단일 list
lst = [1, 2, 3, 4, 5]
print(lst, type, len(lst))    # [1, 2, 3, 4, 5] <class 'type'> 5

for i in lst :
    # print(i, end=' ')  # 1 2 3 4 5
    print(lst[i-1: ])  # 변수[start : stop]
    '''
    [1, 2, 3, 4, 5]
    [2, 3, 4, 5]
    [3, 4, 5]
    [4, 5]
    [5]
    '''
for i in lst :
    print(lst[:i])   # 변수[start : stop]
    '''
    [1]
    [1, 2]
    [1, 2, 3]
    [1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    '''

'''
처음/마지막 데이터 추출
'''
x = list(range(1,101))   # 1 ~ 100 벡터
print(x)
print(x[:5])    # [1, 2, 3, 4, 5]
print(x[-5:])   # [96, 97, 98, 99, 100]

'''
index 형식
변수[start : stop-1 : step]  start=0, step=1 기본값
'''
print(x[:])     # 전체 데이터
print(x[::2])   # [::step=2] : 홀수
print(x[1::2])  # [start=1::step=2] : 짝수

# 2. 중첩 list : [[], []]
a = ['a', 'b', 'c']
b = [10, 20, 5, True, "hong"]
print(b)  # 서로 다른 타입을 저장하고 출력할 수 있다.

b = [10, 20, 5, a, True, "hong"]
print(b)     # 리스트 안에 리스트 자체를 넣을 수 있다.  # 이래봤자 1차원임
print(b[3])  # ['a', 'b', 'c']
print(b[3][0])   # a
print(b[3][1:])  # ['b', 'c']
len(b)

print(type(a), type(b))  # 둘 다 리스트
print(id(a), id(b))      # 서로 다른 주소

# 3. 값 수정(추가, 삽입, 수정, 삭제)
num = ['one', 'two', 'three', 'four']
print(len(num))  # 4

num.append('five')
print(num)
num.remove('five')
print(num)
num.insert(0, 'zero')
print(num)
num[0] = 0
print(num)

# 4. list 연산(+, *)

# 1) list 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y      # 새로운 객체
print(z, type(z))       # [1, 2, 3, 4, 1.5, 2.5] <class 'list'>

# 2) list 확장
x.extend(y)  # 기존 객체
print(x)     # [1, 2, 3, 4, 1.5, 2.5]

# 3) list 추가
x.append(y)
print(x)     # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# 4) list 곱셈(*)
lst = [1, 2, 3, 4]
result = lst * 2
print(result)  # [1, 2, 3, 4, 1, 2, 3, 4]
result = lst * 3
print(result)  # 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# 5. list 정렬
result.sort()              # 오름차순이 기본값
print(result)
result.sort(reverse=True)  # 내림차순
print(result)

# 6. scala vs vector
'''
scala 변수 : 한 개의 상수(값)를 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기, 방향)
'''
dataset = []                              # 빈 리스트 : 벡터
size = int(input("vector size : "))       # 스칼라

for i in range(size):
    dataset.append(i+1)                   # 벡터 변수
print(dataset)

# 7. list에서 원소 찾기
'''
if 값 in list :
    참 실행문
else :
    거짓 실행문
'''
if 5 in dataset:
    print("5가 있음")
else:
    print("5가 없음")