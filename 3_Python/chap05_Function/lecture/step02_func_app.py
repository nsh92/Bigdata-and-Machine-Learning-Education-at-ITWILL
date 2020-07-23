'''
사용자 정의 함수 응용
'''

# 1. 텍스트 전처리 용도 함수  # 4장 stpe02 복붙
def clean_text(texts):
    from re import sub  # gsub() 유사함
    # 1. 소문자 변경
    texts_re = texts.lower()
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장 부호 제거
    punc_str = '[,.<>/?;:!@#$%^&*()]'
    text_re3 = sub(punc_str, '', texts_re2)
    # 4. 공백 제거
    text_re4 = ' '.join(text_re3.split())
    return text_re4

# 텍스트 전처리
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
print('텍스트 전처리 전')
print(texts)
print(len(texts))

print('텍스트 전처리 후')
texts_re = [clean_text(text) for text in texts]
print(texts_re)

# 2. 표본의 분산과 표준편차
from statistics import mean, variance, stdev
from math import sqrt # 수학함수
dataset = [2, 4, 5, 6, 1, 8]
print(mean(dataset))      # 4.333333333333333
print(variance(dataset))  # 6.666666666666666
print(stdev(dataset))     # 2.581988897471611

'''
분산 = sum((x변량 - 평균)**2) / (n - 1)
표준편차 = sqrt(분산)
'''
def var_std(dataset):
    avg = mean(dataset)
    diff = [(x-avg)**2 for x in dataset]
    diff_sum = sum(diff)
    var = diff_sum / (len(dataset) - 1)
    std = sqrt(var)
    return var, std

# 함수 호출
var, std = var_std(dataset)
print('분산 =', var)
print('표준편차 =', std)






