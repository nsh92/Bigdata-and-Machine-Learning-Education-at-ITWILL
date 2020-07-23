'''
tuple 특징
 - 순서가 존재함 : 인덱스가 있음
 - 1차원의 배열구조(벡터)
 - 수정 불가, 처리 속도 빠름
 - 수정 불가 : 제공하는 함수, 멤버가 없음
 형식) 변수 = (원소1, 원소2, ...)
'''
tp = 10      # 스칼라
tp1 = (10)   # 얘도 스칼라
tp2 = (10,)  # 이러면 튜플이 됨
print(tp, tp1)  # 10  10
print(tp2, type(tp2))  # (10,) <class 'tuple'>

# 인덱스
tp3 = (10, 58, 4, 96, 55, 2)
print(tp3[:4])
print(tp3[-3:])

# 수정 불가
tp3[0] = 100  # 에러뜸

# max / min
vmax = vmin = tp3[0]  # 첫번째 원소 초기화

for t in tp3 :  #(10, 58, 4, 96, 55, 2)
    if vmax < t :
        vmax = t         # 조건에 부합하다면 스와핑
    if vmin > t :
        vmin = t
print('최댓값 = ', vmax)
print('최솟값 = ', vmin)

# list -> tuple
lst = list(range(10000))
print(len(lst))
tlst = tuple(lst)
print(type(tlst))