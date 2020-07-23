'''
정규 표현식

[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc)
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
'''

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
import re                           # 방법1) 정규표현식 모듈
from re import findall, match, sub  # 방법2) from 모듈 import 함수
'''
# 방법1)
re.findall()
# 방법2)
findall()
# 보통 이 걸 주로 쓰지
'''

# 1. findall 함수
# 형식) findall(pattern= '메타문자', string= '문자열')

# 1) 숫자 찾기
print(re.findall('1234', st1))     # ['1234'] 리스트 형태 및 하나의 원소로 반환
print(findall('[0-9]{3}', st1))    # ['123', '555'] 숫자가 연달아 3번 나오는 패턴, 리스트로 반환
print(findall('[0-9]{3,}', st1))  # ['1234', '555'] 숫자가 연달아 3번 이상 나오는 패턴, 리스트로 반환
print(findall('\\d{3,}', st1))    # 위와 동일  # r'd{3,}' 과 동일

# 2) 문자열 찾기
print(findall('[가-힣]{3,}', st1))    # ['홍길동', '이사도시']
print(findall('[a-z]{3}', st1))      # ['abc']
print(findall('[a-z|A-Z]{3}', st1))  # ['abc', 'ABC']

str_list = st1.split(sep=' ')
print(str_list)  # ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']
names = []
for s in str_list:
    tmp = findall('[가-힣]{3,}', s)
    print(tmp)
    # [], ['홍길동'], [], ['이사도시']
    # 불일치 되는 원소는 빈 리스트로 반환, 일치되는 애들은 일치되는만큼만 반환됨
    # 반환되는 걸 왔으니 원하는 걸 적재시켜야 함 : [] -> false, [홍길동] -> true
    if tmp:  # 원소가 있는지 없는지 여부만 판단할 때 이렇게
        names.append(tmp[0])   # 그냥 tmp로 해놓으면 중첩리스트가 되어서 값만 가도록 함
print(names)

# 3) 접두어 / 접미어 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
print(findall('^test', st2))   # ['test']  test가 접두어인 거
print(findall('st$', st2))     # ['st']    st가 접미어

# 종료 문자 찾기
print(findall('.bc', st2))     # ['abc', 'mbc'] bc로 끝나는 암거나 : bc앞에 점

# 시작 문자 찾기
print(findall('t.', st2))      # ['te', 't1', 'te'] t로 시작하는 암거나 : t뒤에 점

# 4) 단어 찾기(\\w) : 한글 영문자 숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3)
print(words)  # ['test', '홍길동', 'abc', '123', 'tbc']
              # 3자 이상 단어 암거나

# 5) 특정 문자열 제외
print(findall('[^t]+', st3))  # ['es', '^홍길동 abc 대한*민국 123$', 'bc']
print(findall('[^t]', st3))   # ['e', 's', '^', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', '*', '민', '국', ' ', '1', '2', '3', '$', 'b', 'c']

# 특수 문자 제외
print(findall('[^^*$]+', st3))  # ['test', '홍길동 abc 대한', '민국 123', 'tbc']


# 2. match() 함수
# match(pattern= '패턴', string='문자열')
# - 패턴 일치 여부를 반환 (일치 : object 반환, 불일치 : null 반환)

jumin = "123456,1234567"
result = match("[0-9]{6}-[1-4]\\d{6}", jumin)
print(result)

if result:                        # object
    print("정상 주민번호")
else:                             # None(Null)
    print("비정상 주민번호")


# 3. sub('pattern', 'rep', 'string')
print(findall('[^^*$]+', st3))  # 이거 불편했음, 서브가 더 편함

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
result = sub('[\^*$]', '', st3)    # \ : ^을 메타문자로 보지 말고 그냥 문자로 취급하라
print(result)  # test홍길동 abc 대한민국 123tbc
               # 족칠 거 족쳐주고 반환값을 스트링 그대로 넘김
