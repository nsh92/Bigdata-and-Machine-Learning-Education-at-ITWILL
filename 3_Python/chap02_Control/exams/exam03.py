'''
step3 관련 문제

문) word counter
   - 여러줄의 문장을 단어로 분류하고, 단어 수 출력하기
'''

# <<출력 결과>>
'''
안녕하세요.
Python
세계로
오신걸
환영합니다.
파이션은
비단뱀
처럼
매력적인
언어입니다.
단어수 : 10
'''

multiline="""안녕하세요. Python 세계로 오신걸
환영합니다.
파이션은 비단뱀 처럼 매력적인 언어입니다."""

sents1 = []
words1 = []
for sent1 in multiline.split('\n'):
    sents1.append(sent1)
    for word1 in sent1.split():
        print(word1)
        words1.append(word1)

print("단어수 :", len(words1))


'''
문제 추가

문) 3개의 단어를 키보드로 입력 받아서 각 단어의 첫자를 추출하여 단어의 약자를 출력하시오.
  조건1) 각 단어 변수(word1, word2, word3) 저장 
  조건2) 입력과 출력 구분선 : 문자열 연산 

   <<화면출력 결과>>  
 첫번째 단어 : Korea 
 두번째 단어 : Baseball
 세번째 단어 : Orag
 =================
 약자 : KBO
 =================
'''

word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
print("=" * 20)
print("약자 : ", word1[0] + word2[0] + word3[0])
print("=" * 20)