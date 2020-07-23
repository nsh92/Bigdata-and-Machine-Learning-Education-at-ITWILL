# -*- coding: utf-8 -*-
"""
NB vs SVM : 희소행렬(고차원)
 - 가중치 적용 : Tfidf
"""
from sklearn.naive_bayes import MultinomialNB # NB model class
from sklearn.svm import SVC # SVM model class
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np # 파일 업로드 : 7장에서 했던 spam_data.npy

# 1. dataset load
x_train, x_test, y_train, y_test = np.load("C:/ITWILL/4_Python-II/workspace/chap07_textmining/data/spam_data.npy",
                                           allow_pickle=True)

x_train.shape # (3901, 4000)
x_test.shape  # (1673, 4000)
y_train.shape
y_test.shape
# y 얘내는 리스트객체라서 shape이 안댄다(shape은 넘파이객채를 위한 것임)
y_train = np.array(y_train)
y_test = np.array(y_test)
y_train.shape # (3901,)
y_test.shape  # (1673,)


# 2. NB model
nb = MultinomialNB()
model = nb.fit(X=x_train, y=y_train)
y_pred = model.predict(X=x_test)
y_true = y_test

acc_nb = accuracy_score(y_true, y_pred) # 0.9784817692767483
con_nb = confusion_matrix(y_true, y_pred)
'''[[1450,    0],
    [  36,  187]]  '''
print(187/(36+187)) # 스팸에 대한 분류정확도 : 0.8385650224215246


# 3. SVM model
svc = SVC(gamma='auto')
model_svc = svc.fit(X=x_train, y=y_train)
y_pred2 = model_svc.predict(X=x_test)
y_true2 = y_test

acc_svm = accuracy_score(y_true2, y_pred2) # 0.8667065152420801
con_svm = confusion_matrix(y_true2, y_pred2)
'''[[1450,    0],
    [ 223,    0]] : 뭔가 이상하다 모델을 수정하자'''

svc = SVC(kernel='linear')
model_svc = svc.fit(X=x_train, y=y_train)
y_pred2 = model_svc.predict(X=x_test)
y_true2 = y_test
acc_svm = accuracy_score(y_true2, y_pred2) # 0.982068141063957
con_svm = confusion_matrix(y_true2, y_pred2)
'''[[1448,    2],
    [  28,  195]]'''
print(195/(28+195)) # 스팸에 대한 분류정확도 : 0.874439461883408






















