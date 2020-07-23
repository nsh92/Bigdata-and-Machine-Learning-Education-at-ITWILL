# -*- coding: utf-8 -*-
"""
step04_word_embedding_LSTM.py

1. encoding 유형 : 딥러닝 모델에서 사용되는 데이터
  - one hot encoding : texts -> sparse matrix(encoding) -> DNN -> label 분류
   -> DNN : 단어출현빈도수 입력 -> label 분류
  - word_enbedding : texts -> sequence(10진수) -> embedding -> RNN -> label 분류
   -> RNN : 자연어입력 -> label 분류

2. Embedding(input_dim, output_dim, input_length)
  - input_dim : 임베딩층에 입력되는 전체 단어 수
  - output_dim : 임베딩층에서 출력되는 벡터의 수
  - input_len : 1문장을 구성하는 단어 수
"""
import pandas as pd
import numpy as np
import string
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten, LSTM
from tensorflow.keras.preprocessing.sequence import pad_sequences

# step03 퍼옴
temp_spam = pd.read_csv("C:/ITWILL/6_Tensorflow/data/temp_spam_data2.csv",
                        header = None, encoding = "utf-8")
temp_spam.info()
'''
 0   0       5574 non-null   object : label(ham or spam)
 1   1       5574 non-null   object : texts(영문장)
'''
# 1. 변수 선택
label = temp_spam[0]
texts = temp_spam[1]
len(label)

# 2. data 전처리
# target dummy('spam'=1, 'ham'=0)
target = [1 if x=='spam' else 0 for x in label]
print('target :', target)
target = np.array(target)

# texts 전처리
def text_prepro(texts):
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts] # not in string.punctuation : 문장 부호가 아닌 거
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]      # not in string.digits : 숫자가 아닌 거
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts = text_prepro(texts)
texts[0]



# step01 퍼옴
# 1. 토큰 생성
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
token = tokenizer.word_index
print(token) 
print("전체 단어 수", len(token)) # 전체 단어 수 8629

voc_size = len(token) + 1 # 8630

# 2. 정수 인덱스 : 토큰 -> 정수 인덱스
seq_index = tokenizer.texts_to_sequences(texts) 
print(seq_index)
len(seq_index)      # 전체 문장 수 : 5574
len(seq_index[0])   # 첫번째 문장의 단어 길이 : 20
len(seq_index[-1])  # 마지막 문장의 단어 길이 : 6

lens = [len(seq) for seq in seq_index]
maxlenth = max(lens) # 171

# 3. 패딩(padding) : 관측치 벡터들의 길이를 동일하게 맞춤
x_data = pad_sequences(seq_index, maxlen = maxlenth)
print(x_data)

x_data[0] # 151ro 0패딩

# 4. dataset split
x_train, x_val, y_train, y_val = train_test_split(x_data, target)
x_train.shape # (4180, 171)
x_val.shape   # (1394, 171)

# 5. embedding 층 : 인코딩
embedding_dim = 32  # 64, 128, 256 ... 전체 단어 길이 따라서 변경됨

model = Sequential() # model 객체 생성

## embedding layer 추가
model.add(Embedding(input_dim = voc_size, output_dim = embedding_dim, input_length = maxlenth))

## 2d -> 1d
# model.add(Flatten())

## LSTM(RNN)
model.add(LSTM(32)) # RNN layer : Flatten 기능 포함

## DNN hidden layer
model.add(Dense(32, activation="relu"))

## DNN output layer
model.add(Dense(1, activation="sigmoid"))

model.summary()

# 6. 모델 생성 및 평가
model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy']) 
model.fit(x_train, y_train, batch_size = 512, epochs = 5, validation_data = (x_val, y_val))

loss, score = model.evaluate(x_val, y_val)
print("loss =", loss)    
print("score =", score)  

# Flatten 사용 : 임베딩 + DNN
# loss = 0.1626110991070226
# score = 0.96269727

# RNN 사용 : 임베딩 + RNN + DNN
# loss = 0.1263835071512582
# score = 0.9684362








