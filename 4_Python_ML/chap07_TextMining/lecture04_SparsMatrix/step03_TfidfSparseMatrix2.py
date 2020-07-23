# -*- coding: utf-8 -*-
"""
1. csv 읽기
2. 텍스트, 타겟 -> 전처리(불용어 숫자 등등)
3. max features : 최대 단어 갯수
4. Sparse Matrix
5. train / test split
6. binary file save
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
# 1. csv file read
spam_data = pd.read_csv('C:/ITWILL/4_Python-II/workspace/chap07_TextMining/data/temp_spam_data2.csv', 
                        encoding='utf-8', header=None)
spam_data.info()
spam_data.head()

target = spam_data[0]
texts =  spam_data[1]
target
texts

# 2. 전처리
## ham spam을 더미변수로
target = [1 if t == 'spam' else 0 for t in target]
target

# 3. max features
'''
모델에서 사용할 x변수의 개수(열의 차수)
'''
tfidf = TfidfVectorizer()
tfidf_fit = tfidf.fit(texts) # 문장 -> 단어장 생성
vocs = tfidf_fit.vocabulary_
vocs
len(vocs) # 8722
max_features = 4000 # 4000개 단어만 쓴다 : 5574 x 4000
sparse_mat = TfidfVectorizer(stop_words='english', max_features=max_features).fit_transform(texts)
                             # 단어 안의 불용어 제거 설정
print(sparse_mat)

# 4. 사이파이 -> 넘파이
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr.shape # (5574, 4000)
sparse_mat_arr

# 5. train / test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(sparse_mat_arr, target, test_size=0.3)

x_train.shape # (3901, 4000)
x_test.shape  # (1673, 4000)

# 6. numpy binary file save
import numpy as np
spam_data_split = (x_train, x_test, y_train, y_test)
np.save('C:/ITWILL/4_Python-II/workspace/chap07_TextMining/data/spam_data', spam_data_split)
## 확장자 생략하면 npy 기본확장자로 저장됨

## file load
x_train, x_test, y_train, y_test = np.load('C:/ITWILL/4_Python-II/workspace/chap07_TextMining/data/spam_data.npy',
                                           allow_pickle=True)
x_train.shape # (3901, 4000)
x_test.shape  # (1673, 4000)























