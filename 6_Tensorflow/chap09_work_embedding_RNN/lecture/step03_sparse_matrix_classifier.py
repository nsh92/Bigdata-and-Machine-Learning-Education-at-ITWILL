# -*- coding: utf-8 -*-
"""
step03_sparse_matrix_classifier.py

Sparse Matrix(Tfidf) + DNN model

1. csv file load
2. label + texts
3. texts 전처리 : 텍스트 벡터화
4. 희소행렬(sparse matrix)
5. DNN model 생성
"""
import pandas as pd
import numpy as np
import string
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense


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

# 3. 텍스트 토큰화
tokenizer = Tokenizer(num_words = 4000) # 총 약8천개 중 -> 4천
tokenizer.fit_on_texts(texts)
token = tokenizer.word_index
print("전체 단어 수 = ", len(token)) # 전체 단어 수 =  8629

# 4. 희소행렬(sparse matrix) : tfidf
x_data = tokenizer.texts_to_matrix(texts, mode='tfidf')
x_data.shape # (5574:docs, 4000:terms)

# 5. dataset split
x_train, x_val, y_train, y_val = train_test_split(x_data, target, test_size = 0.3)


# 6. DNN layer
input_shape = (4000, )
model = Sequential()
model.add(Dense(64, input_shape = input_shape, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.summary()

# 7. model compile / training
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']) 
model.fit(x_train, y_train, batch_size = 512, epochs = 5, validation_data = (x_val, y_val))

loss, score = model.evaluate(x_val, y_val)
print("loss =", loss)    # loss = 0.07692885741360989
print("score =", score)  # score = 0.98684996











