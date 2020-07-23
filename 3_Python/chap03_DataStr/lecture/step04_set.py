'''
set 특징
 - 순서 없음(index 사용 불가)
 - 중복 허용 불가
 - 형식) 변수 = {값1, 값2, ...}
 - 집합 개념
'''
s = {1, 3, 5}
print(len(s))  # 3

s = {1, 3, 5, 1, 5}
print(len(s))  # 3

for d in s:
    print(d, end =' ')  # 1, 3, 5 순서 없음 이리 나온 건 우연임

s2 = {3, 6}

# 집합 관련 함수
print(s.union(s2))         # 합집합 {1, 3, 5, 6}
print(s.difference(s2))    # 차집합 {1, 5}
print(s.intersection(s2))  # 교집합 {3}

# list : gender
gender = ['남자', '여자', '남자', '여자']  # 중복이 허용되는 리스트임
# set으로 형변환
sgender = set(gender)
print(sgender)   # 중복 불가라서 {'남자', '여자'}
print(sgender[1])  # 타입 오류 인덱스가 없기에 추출 불가능

# set -> list
lgender = list(sgender)
print(lgender[0])  # 이래야 추출 가능

# 인덱스는 없지만
# 원소 추가 / 삭제는 가능하다
s3 = {1, 3, 5, 7}
print(s3, type(s3))  # {1, 3, 5, 7} <class 'set'>
s3.add(9)      # 원소 추가
print(s3)      # {1, 3, 5, 7, 9}
s3.discard(3)  # 원소 삭제
print(s3)
# 수정하거나 삽입은 불가능