'''
리스트 내포
 - list에서 for문 사용
 형식1) 변수 = [실행문   for 변수 in 열거형객체]
  실행순서 : 1. for문 -> 2. 실행문 -> 3. 변수 저장
 형식2) 변수 = [실행문   for 변수 in 열거행객체 if 조건식]
  실행순서 : 1. for문 -> 2. if문 -> 3. (참)실행문 or (거짓)생략 -> 4. 변수 저장
'''

# 형식1) 변수 = [실행문   for 변수 in 열거형객체]
# x 각 변량에 제곱
x = [2, 4, 1, 3, 7]
x**2  # 안댐

datas = []
for i in x:
    print(i**2)
    datas.append(i**2)
print(datas)
# 이걸 갖다
# 형식1) 변수 = [실행문   for 변수 in 열거형객체]   에 맞추자
data2 = [i**2 for i in x]
print(data2)

# 형식2) 변수 = [실행문   for 변수 in 열거행객체 if 조건식]
# 1~100 -> 3의 배수 뽑겠다
num = list(range(1,101))
print(num)

data3 = [i for i in num if i % 3 == 0]
print(data3)

data3 = [i*2 for i in num if i % 3 == 0]
print(data3)

# 내장함수 + 리스트 내포
print('sum =', sum(x))
# 저런 sum같은 애들을 내장함수라 함
data4 = [[1,3,5], [4,5], [7,8,9]]  # 중첩 리스트 생성
# 예를들면, for d in data4:   # 저 d는 중첩리스트의 한 덩어리를 받음
result = [sum(d) for d in data4]
print(result)

















