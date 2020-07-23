'''
문자열 처리
- 문자열(string) : 문자들의 순서(인덱스) 집합
- indexing / slicing 가능
- 문자열 = 상수 : 수정 불가
'''

# 1. 문자열 처리
# 1) 문자열 유형
lineStr = "this is one line string" # 한 줄 문자열
print(lineStr)

# 여러줄 문자열
multiStr = '''this
is multi line
string
'''
print(multiStr)

multiStr2 = 'this \nis multi line \nstring'
print(multiStr2)

# sql문 : 부서번호
deptno = int(input('부서번호 입력 :'))
query = f"""select * from emp
where deptno = {deptno}
order by sel desc"""
print(query)

# 2) 문자열 연산(+, *) # 결합과 반복
print('python' + ' program') # 결합연산자
print('python' + 37) # 이 상태로는 에러
print('python' + str(37)) # 이렇게 해야댐

print('-'*30)  # 30번 반복

'''
object.member or object.member() # 변수 or 함수
int.member  # int의 멤버들
str.member
'''

# 3) 문자열 처리 함수
print(lineStr, type(lineStr)) # 내용과 자료형을 출력했음
print('문자열 길이 : ', len(lineStr))
print('t의 글자 수 : ', lineStr.count('t'))  # t가 몇개냐

# 접두어 : 시작 문자열  # prefix
lineStr.startswith('this')  # true
lineStr.startswith('that')  # false

# 문자열분리(split) : 토큰 생성 # sep : separate
words = lineStr.split(sep = ' ') # 문장이 들어가서 단어가 생성됨 # 공백을 기준으로 잘라 출력
                      # 기본값임
print(words)  # 5개 원소의 벡터
print('단어의 길이 : ', len(words))

# 문단 -> 문장
multiStr = '''this
is multi line
string'''

sentence = multiStr.split(sep='\n')
print(sentence)  # 3문장의 리스트(벡터)
print('문장 길이 :', len(sentence))

# 결합(join) : '구분자'.join(스트링)  <-> split
sentence = ' '.join(words)  # ' '기준으로 분리되었던 것이 결합됨
print(sentence)

para = ','.join(sentence)
print(para)

print(multiStr.upper())  # 대문자로 바꿈

# 4) 인덱싱 / 슬라이싱
print(lineStr[0]) # 첫번째 문자                        - t
print(lineStr[-1]) # 끝에서 첫번째 문자 = 마지막 문자   - g

# 슬라이싱
print(lineStr[:4])  # 시작을 생략하면 0번 자동 시작 # 0부터 4이전까지 [start : end-1]
print(lineStr[-6:]) # 오른쪽 끝 6개 문자열

# 2. escape 문자 처리
'''
escape 문자 : 명령어 이외 특수문자(', ", \n, \t, \b)
            : 쟤내들 기능으로부터 탈출한다
'''
print("\nescape 문자")
print("\\nescape 문자")  # 특수문자를 반영하지 않도록 한다면 \추가
print(r"\nescape 문자")  # 혹은 이렇게 r을 앞에 추가

# c:\ptyhon\work\test
print('c:\ptyhon\work\test')   # \t 때문에 변질되어 출력됨
print(r'c:\ptyhon\work\test')  # 이렇게 비활성화 시킴
print('c:\ptyhon\work\\test')












