# -*- coding: utf-8 -*-
"""
step02_features_extract.py

1. 텍스트에서 특징(features) 추출 방법
   - 지도학습에서 text 대상 희소행렬(sparse matrix)
   - 방법 : tf, tfidf

2. num_words(max features)
   - 단어의 차수를 지정하는 속성
   ex) num_words = 500 : 전체 단어(1000)에서 중요단어 500개 선정

3. max length : padding 적용
   - 한 문장을 구성하는 단어 수 지정 속성
   ex) max_length = 100 : 전체 문장을 구성하는 단어수 100개 사용
       1문장 : 150개로 구성 -> 50개 짤림
       2문장 : 70개로 구성 -> 30개 0패딩
"""
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical


# 토큰 생성기
tokenizer = Tokenizer() # num_words 생략 : 전체 단어 이용

texts = ['The dog sat on the table.', 'The dog is my Poodle.']

# 1. 토큰 생성
tokenizer.fit_on_texts(texts) # 텍스트 적용
token = tokenizer.word_index # dict : {word : index}
print(token) # {'the': 1, 'dog': 2, 'sat': 3, 'on': 4, 'table': 5, 'is': 6, 'my': 7, 'poodle': 8}
print("전체 단어 수", len(token)) # 전체 단어 수 8


# 2. 텍스트로부터 특징(features) 추출 : 희소행렬(sparse matrix)
binary = tokenizer.texts_to_matrix(texts, mode='binary')
binary
'''    pad  1   2   3   4   5   6   7   8
array([[0., 1., 1., 1., 1., 1., 0., 0., 0.],
       [0., 1., 1., 0., 0., 0., 1., 1., 1.]])'''

count = tokenizer.texts_to_matrix(texts, mode='count')
count # 빈도수
'''
array([[0., 2., 1., 1., 1., 1., 0., 0., 0.],
       [0., 1., 1., 0., 0., 0., 1., 1., 1.]])'''

freq = tokenizer.texts_to_matrix(texts, mode='freq')
freq  # 빈도수를 비율로
'''
array([[0.        , 0.33333333, 0.16666667, 0.16666667, 0.16666667,
        0.16666667, 0.        , 0.        , 0.        ],
       [0.        , 0.2       , 0.2       , 0.        , 0.        ,
        0.        , 0.2       , 0.2       , 0.2       ]])'''

# 출현빈도 -> 비율(TF*1/DF)
tfidf = tokenizer.texts_to_matrix(texts, mode='tfidf')
tfidf  #  비율에서 가중치로
'''
array([[0.        , 0.86490296, 0.51082562, 0.69314718, 0.69314718,
        0.69314718, 0.        , 0.        , 0.        ],
       [0.        , 0.51082562, 0.51082562, 0.        , 0.        ,
        0.        , 0.69314718, 0.69314718, 0.69314718]])'''
tfidf.shape # (2, 9)






















