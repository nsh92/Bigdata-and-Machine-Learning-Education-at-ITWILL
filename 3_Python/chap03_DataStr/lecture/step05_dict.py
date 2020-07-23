'''
dict 특징
 - set 구조와 유사함
 set형식) 변수 = {값1, 값2,...}
 dict형식) 변수 = {key1:value1, key2:value2}
 - R의 리스트와 유사함
 - key와 value 한 쌍으로 원소 구성
 - key로 value를 참조
 - 순서 없고 인덱스 없다
 - key 중복 불가능, value 중복 가능
'''

# 1. dict 생성

## 방법1)
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic, len(dic), type(dic))

## 방법2)
dic2 = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(dic2, len(dic2), type(dic2))

# 2. 수정, 추가, 삭제, 검색 : key를 이용함
dic2['age'] = 45   # 수정 : 모양은 인덱스이나 Key임
dic2['pay'] = 350  # 추가
print(dic2)
del dic2['addr']   # 삭제
print(dic2)

## 키 검색
print('age' in dic2)  # True : 있음

# 3. for 이용
for k in dic2:   # 이렇게 하면 키가 넘어올까 값이 넘어올까
    print(k)     # 키가 옴

for k in dic2.keys():  # 위와 같음
    print(k)

for k in dic2.keys():
    print(dic2[k])     # 이렇게 해주면 값이 옴

for k in dic2.keys():
    print(k, end = '->')
    print(dic2[k])

for v in dic2.values():  # 값이 옴
    print(v)

for k, v in dic2.items():  # 둘 다 넘길래
    print(k, end = '->')
    print(v)

for d in dic2.items():  # 이렇게 하면 어떨까
    print(d)            # 둘이 묶여서 튜플이 나옴

# 4. key -> value
print(dic2['name'])      # 홍길동  # 인덱스 형식
print(dic2.get('name'))  # 홍길동  # 함수

# 5. {'key' : [value1, value2, ...]}
# 하나의 키에 리스트
# {'이름' : [급여, 수당]}
emp = {'hong' : [250, 50], 'lee' : [350, 80], 'yoo' : [200, 40]}
print(emp)

for k, v in emp.items():  # key, value
    print(k, end = '->')
    print(v)

# 급여가 250 이상인 사원 정보 출력
for k, v in emp.items():  # key, value
    if v[0] >= 250 :
        print(k, end = '->')
        print(v)

# 급여가 250 이상인 경우의 사원명, 수당 합계 출력
su = []
for k, v in emp.items():  # key, value
    if v[0] >= 250 :
        print(k, end = '->')
        print(v)
        su.append(v[1])
print('수당의 합계 : ', sum(su))

## 교수님 코딩
su = 0
for k, v in emp.items():  # key, value
    if v[0] >= 250 :
        print(k)
        su += v[1]
print('수당의 합계 : ', su)

# 6. 문자 빈도수 구하기
## 방법1)
charset = ['love', 'test', 'love', 'hello', 'test', 'love']
print(len(charset))  # 6
wc = {}  # 빈 set
for word in charset:
    if word in wc:
        wc[word] += 1  # 2회 이상 발견 : 1씩 증가
    else :
        wc[word] = 1   # 최초 발견 : 1을 초기화
print('워드 카운트 : ', wc)
# 워드 카운트 :  {'love': 3, 'test': 2, 'hello': 1}

print(max(wc, key = wc.get))

# love
# print(max(wc))만 하면 test가 뜸

## 방법2)
wc2 = {}  # 빈 set
for word in charset:
    wc2[word] = wc2.get(word, 0) + 1    # key = value
print(wc2)
# {'love': 3, 'test': 2, 'hello': 1}
'''
get(key, 0) + 1
 - key의 값이 없으면 0으로 value값을 설정하고, 있으면 기존 value에 +1
'''

a ={'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
max(a)
max(a, key=a.get)
# 여기서 key는 max함수의 파라미터임

a ={'a': [5, 1], 'b': [4, 2], 'c': [3, 3], 'd': [2, 4], 'e': [1, 6]}
max(a)
max(a, key=a.get)
# 첫번째 값만 비교하내
max(a, key=lambda k: a[k])
