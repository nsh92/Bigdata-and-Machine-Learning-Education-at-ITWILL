'''
반복문(for)
형식)
for 변수 : in 열거형 객체 :
    실행문
    실행문

열거형 객체란?
 : 반복 가능하다
 : iterable : string, list, tuple, set/dictr
제너레이터 식 : 변수 in 열거형객체(원소 순회 -> 앞의 변수로 넘김)
'''

# 1. 스트링 열거형 객체
string = "나는 홍길동 입니다."
print(len(string)) # 11개의 문자열
for s in string :        # 11회
    print(s, end=' ')    # 나 는   홍 길 동   입 니 다 .

print(len(string.split(sep=' '))) # 3
for s in string.split(sep=' ') :
    print(s)                     # 3회
'''
나는
홍길동
입니다.
'''

# 2. 리스트 열거형 객체
help(list)
lst = [1,2,3,4,5]   # 리스트객체
print(lst)          # 1차원 벡터
print(type(lst))    # 리스트라는 클래스
print(len(lst))

for i in lst :
    print(i, end = ' ')

print()

print(lst**2)  ## 불가능
# 리스트 자체에 수학적 연산이 가능하지 않음 이런 과정을 거쳐야 함
lst2 = []  # 얘도 리스트임, 빈 리스트
for i in lst :
    print(i, end = ' ')
    lst2.append(i**2)

print('\nlst2 : ', lst2)



# 1~100 원소를 갖는 리스트 객체 생성하라
lst3 = list(range(1, 101))
print(lst3)

# 3. range 열거형 객체 이용
'''
range(n) : 0 ~ n-1 정수 생성
range(start, stop) : start ~ stop-1  정수들 생성
range(start, stop, step) : start ~ stop-1  step정수들 생성
'''
num1 = range(10)        # 0 ~ 9
num2 = range(1,10)      # 1 ~ 9
num3 = range(1,10,2)    # 1, 3, 5, 7, 9
print(num1)             # range(0, 10)
print(num2)             # range(1, 10)
print(num3)             # range(1, 10, 2)
                        # 객체의 정보만이 출력될 뿐
                        # 무엇이 담겨있는지 알려면 추가적인 작업이 필요

for i in num1 :
    print(i, end = ' ')
print()
for i in num2 :
    print(i, end = ' ')
print()
for i in num3 :
    print(i, end = ' ')

# 뭔가 인덱스를 생성할 때 유용

# 4. list + range 열거형 객체 이용
idx = range(5)   # 0 ~ 4
print(idx)       # range(0, 5)

idx = list(range(5))   # 0 ~ 4
print(idx)             # [0, 1, 2, 3, 4]

for i in idx :
    print(i, end = ' ')
    print(i**2)
'''
문) lst1에다 1~100 까지 100개의 원소를 갖는 벡터를 생성하고,
    lst2에다 3의 배수만 저장하기
'''
lst1 = []
lst2 = []
lst1 = list(range(1,101))

for i in lst1 :
    if i % 3 == 0 :
        lst2.append(i)
print(lst2)
print(len(lst2))

# index 이용 : 분류정확도 간단한 예시
y = [1, 0, 2, 1, 0]       # 관측치 : 범주형(0, 1, 2)
y_pred = [1, 0, 2, 0, 0]  # 예측치

size = len(y)
acc = 0
for i in range(size) :  # 관측치의 길이만큼 인덱스 생성 0번~4번
    fit = int(y[i] == y_pred[i])  # int(true or false) 반환 1과 0
    acc += fit * 20      # +=로 안하면 누적 점수가 안 뜨고 최근 데이터만 출력됨

print("분류정확도 =", acc)

# 5. 이중 for문 구구단
for i in range(2, 10) :   # i = 단수
    print("*** %d단***"%i)  # %d 대신 {}, %i대신 .format(i) 넣어도댐
    for j in range(1,10) :  # j = 곱수
        print("%d * %d = %d"%(i, j, (i*j)))
    print("\n") # line skip

for i in range(2, 10) :   # i = 단수
    print("***{}단***".format(i))  # %d 대신 {}, %i대신 .format(i) 넣어도댐
    for j in range(1,10) :  # j = 곱수
        print("%d * %d = %d"%(i, j, (i*j)))
    print("\n") # line skip


para = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""
# 2) 문자열 처리
'''
for 변수 in 문단 :  # 문단 -> 문장 + 문장을 적재할 곳
    for 변수 in 문장 :  # 문장 -> 단어 + 단어를 적재할 곳
'''
sents = []
words = []
for sent in para.split('\n') :
    sents.append(sent)
    for word in sent.split() :
        words.append(word)
print(sents)
print('문장 길이 :', len(sents))
print(words)
print('단어 길이 :', len(words))


# 제너레이터 식 : 변수 in 열거행객체
'''
for 변수 in 열거행객체 :
    -> 객체의 원소 수만큼 반복
if 값 in 열거행객체 :
    -> 객체의 원소 중에서 값이 있으면 True, 아님 False 반환
'''

if "홍길동" in words :
    print("해당 단어 있음")
else :
    print("응 없어")

# 위 응용
search = input("검색 단어 입력 : ")
if search in words :
    print("해당 단어 있음")
else :
    print("응 없어")









