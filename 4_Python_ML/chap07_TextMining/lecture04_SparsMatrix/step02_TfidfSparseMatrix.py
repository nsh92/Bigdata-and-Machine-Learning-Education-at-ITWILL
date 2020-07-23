# -*- coding: utf-8 -*-
"""
1. csv 읽기
2. 텍스트, 타겟 -> 전처리(불용어 숫자 등등)
3. max features : 최대 단어 갯수
4. Sparse Matrix
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
# 1. csv file read
spam_data = pd.read_csv('C:/ITWILL/4_Python-II/workspace/chap07_TextMining/data/temp_spam_data.csv', 
                        encoding='utf-8', header=None)
spam_data'''
      0                        1
0   ham    우리나라    대한민국, 우리나라 만세
1  spam      비아그라 500GRAM 정력 최고!
2   ham               나는 대한민국 사람
3  spam  보험료 15000원에 평생 보장 마감 임박
4   ham                   나는 홍길동        '''

target = spam_data[0]
texts =  spam_data[1]
target
texts

# 2. 전처리
## ham spam을 더미변수로
target = [1 if t == 'spam' else 0 for t in target]
target # [0, 1, 0, 1, 0]

## texts 전처리
import string # text 전처리 : 문단(input) -> 문장(string) -> 음절
def text_prepro(texts):
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts_result = text_prepro(texts)'''
['우리나라 대한민국 우리나라 만세',
 '비아그라 gram 정력 최고',
 '나는 대한민국 사람',
 '보험료 원에 평생 보장 마감 임박',
 '나는 홍길동']'''


# 3. max features
'''
모델에서 사용할 x변수의 개수(열의 차수)
'''
tfidf = TfidfVectorizer()
tfidf_fit = tfidf.fit(texts_result) # 문장 -> 단어장 생성
vocs = tfidf_fit.vocabulary_
vocs
len(vocs) # 16
max_features = len(vocs) # 16개의 단어 모드 쓴다
'''
만약 16개인데, 10으로 한다면, 16단어 중 10단어만 이용하겠다는 의미
sparse matrix = [5 x 10]
'''
sparse_mat = TfidfVectorizer().fit_transform(texts_result)
sparse_mat # <5x16 sparse matrix of type '<class 'numpy.float64'>'
sparse_mat2 = TfidfVectorizer(max_features = max_features).fit_transform(texts_result)
                                            # 인수를 지정하면 열의 차수를 조정함

## 사이파이 -> 넘파이
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr.shape # (5, 16)
sparse_mat_arr # 열에 따른 가중치

# 근데, tfidf 얘는 공백을 기준으로 단어냐 아니냐를 구분하기에
# 형태소분석하는 절차가 필요하다
# 그래서 순수하게 명사만 뽑아야 함 (나는 -> 나)
























