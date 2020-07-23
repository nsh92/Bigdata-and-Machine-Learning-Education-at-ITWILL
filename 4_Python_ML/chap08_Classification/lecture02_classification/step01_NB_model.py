# -*- coding: utf-8 -*-
"""
NB 모델
 GaussianNB : x변수가 실수형, 정규분포 형태
 MultinomialNB : 희소행렬과 같은 고차원 데이터를 이용하여 다항분류
"""
import pandas as pd # csv 읽기
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB # 모델 클래스
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score # 모델 평가
from scipy import stats # 이전에 쓰던 정규분포 검정 모듈

######################################
### GaussianNB
######################################

# 1. 데이터 업로드 및 정규성 검정
iris = pd.read_csv("C:/ITWILL/4_Python-II/data/iris.csv")
iris.info()
# 0~3번은 실수형, 아마 정규분포일 듯

## 정규성 검정
stats.shapiro(iris['Sepal.Width']) # pvalue = 0.10113201290369034 : 0.05보다 큼 : 정규분포다


# 2. x, y변수 선택
cols = list(iris.columns)
cols
x_cols = cols[:4]
y_cols = cols[-1] # 변수명만 나눔


# 3. train / test split
train, test = train_test_split(iris, test_size=0.3, random_state=123)


# 4. NB model
nb = GaussianNB()
model = nb.fit(X=train[x_cols], y=train[y_cols])
model


# 5. model 평가
y_pred = model.predict(X = test[x_cols])
y_true = test[y_cols]

acc = accuracy_score(y_true, y_pred) # 0.9555555555555556  # 분류정확도
con_mat = confusion_matrix(y_true, y_pred)                 # 교차분할표
f1score = f1_score(y_true, y_pred, average='micro')        # 불균형인 경우
f1score # 0.9555555555555556 : 정확률, 재현율 -> 조화평균


######################################
### MultinomialNB
######################################
# 1. 문서분류를 위한 데이터셋 업로드
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
newsgroups = fetch_20newsgroups(subset='all') # 'train', 'test'
# Downloading 20news dataset.

print(newsgroups.DESCR)
'''
x변수 : neow 기사 내용(text자료)
y변수 : 해당 news의 group(20개)
'''
newsgroups.target_names
cats = newsgroups.target_names[:4]
cats

# 2. text -> sparse matrix : fetch_20newsgroups(subset='train')
news_train = fetch_20newsgroups(subset='train', categories=cats)
news_train.data
news_train.target # 멀티노미널

## sparse matrix
tfidf = TfidfVectorizer()
sparse_mat = tfidf.fit_transform(news_train.data)
sparse_mat.shape # (2245, 62227)

# 3. model
nb = MultinomialNB()
model = nb.fit(X=sparse_mat, y=news_train.target)

# 4. model 평가 : fetch_20newsgroups(subset='test')
news_test = fetch_20newsgroups(subset='test', categories=cats)
news_test.data
news_test.target

sparse_test = tfidf.transform(news_test.data) # .fit_transform이 아님!
sparse_test.shape # (1494, 62227)

'''
obj.fit_tranform(train_data)
odj.transform(test_data)
즉, tfidf = TfidfVectorizer() 한번만 정의해야 함
'''

y_pred = model.predict(X = sparse_test)
y_true = news_test.target

acc = accuracy_score(y_true, y_pred)
acc # 0.8520749665327979

con_mat = confusion_matrix(y_true, y_pred)
'''
array([[312,   2,   1,   4],
       [ 12, 319,  22,  36],
       [ 16,  26, 277,  75],
       [  1,   8,  18, 365]], dtype=int64)
'''
y_pred[:20]
y_true[:20]




















