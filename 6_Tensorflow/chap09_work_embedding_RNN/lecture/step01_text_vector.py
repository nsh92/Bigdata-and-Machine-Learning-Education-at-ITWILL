# -*- coding: utf-8 -*-
"""
step01_text_vector.py

1. 텍스트 벡터화
  - 텍스트를 숫자형 벡터로 전환
  - 작업절차
    단계1 : 토큰 생성 : 텍스트 -> 토큰(단어 or 문자)
    단계2 : 정수 인덱스 : 토큰에 고유숫자 할당
    단계3 : 인코딩 : 정수 인덱스 -> 숫자형 벡터 할당
2. 인코딩 방법 : one-hot(sparse matrix), word embedding
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

# 2. 정수 인덱스 : 토큰 -> 정수 인덱스
seq_index = tokenizer.texts_to_sequences(texts) 
print(seq_index) # [[1, 2, 3, 4, 1, 5], [1, 2, 6, 7, 8]]
                 # texts를 순서대로 토큰번호를 메김

# 3. 패딩(padding) : 관측치 벡터들의 길이를 동일하게 맞춤
padding = pad_sequences(seq_index)
print(padding)
#[[1 2 3 4 1 5]
# [0 1 2 6 7 8]] -> 0패딩이라고도 함

# 4. 인코딩(one-hot encoding) : true(1) or false(0)
one_hot = to_categorical(padding)
print(one_hot)
'''
[[[0. 1. 0. 0. 0. 0. 0. 0. 0.]
  [0. 0. 1. 0. 0. 0. 0. 0. 0.]
  [0. 0. 0. 1. 0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 1. 0. 0. 0. 0.]
  [0. 1. 0. 0. 0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0. 1. 0. 0. 0.]]

 [[1. 0. 0. 0. 0. 0. 0. 0. 0.]
  [0. 1. 0. 0. 0. 0. 0. 0. 0.]
  [0. 0. 1. 0. 0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0. 0. 1. 0. 0.]
  [0. 0. 0. 0. 0. 0. 0. 1. 0.]
  [0. 0. 0. 0. 0. 0. 0. 0. 1.]]]
'''
one_hot.shape # (2, 6, 9) 3차원
              # 2 : 전체 문서 수
              # 6 : 1문서의 전체 단어 수
              # 9 : 전체 단어 수 + 1 -> 원래 단어수8개 + 패딩되었다는 의미 1








