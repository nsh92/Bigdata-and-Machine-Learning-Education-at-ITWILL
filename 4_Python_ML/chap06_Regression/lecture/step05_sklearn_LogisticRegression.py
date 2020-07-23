# -*- coding: utf-8 -*-
"""
sklearn 로지스틱 회귀모델
 - y변수가 범주형인 경우
"""
from sklearn.datasets import load_breast_cancer, load_iris # 유방암(이항), 아이리스(다항)데이터
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix # 모델 평가 도구 : 분류정확도, 교차분할표
from sklearn.model_selection import train_test_split
import numpy as np

############################
### 1. 이항분류 모델
############################
# 1. 데이터셋 로드
breast = load_breast_cancer()
X = breast.data
y = breast.target
X.shape # (569, 30)
y.shape # (569,)

# 2. 모델 생성
# 앞서 했던 것들과는 파라미터 구조가 좀 다르다
help(LogisticRegression)
# LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
# 졸라 많은데 주요한 것은
# random_state=None, solver='lbfgs', max_iter=100, multi_class='auto'
# random_state=None  : 난수 시드값
# solver='lbfgs'     : 알고리즘
# max_iter=100       : 반복학습횟수
# multi_class='auto' : 다항분류 여부
# help문에서 또 아래로 가면 각 파라미터에 대한 설명이 있음 : 쓸 수 있는 범주 확인
# solver : {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'}
# multi_class : {'auto', 'ovr', 'multinomial'}
'''
바람직한 적용 예)
(많지 않은)일반데이터, 이항분류 : defalut
일반데이터, 다향분류 : solver='lbfgs', multi_class='multinomial' 
빅데이터, 이항분류 : solver='sag'or'saga'
빅데이터, 다항분류 : solver='sag'or'saga', multi_class='multinomial'
'''

y # 0음성 1악성, 일반데이터, 이항분류
lr = LogisticRegression(random_state=123)
model = lr.fit(X=X, y=y)
model

# 3. 모델 평가
acc = model.score(X, y)
print('accuracy =', acc) # 0.9472759226713533 약 95%
y_pred = model.predict(X)
acc2 = accuracy_score(y, y_pred)
print('accuracy =', acc2) # 0.9472759226713533

con_mat = confusion_matrix(y, y_pred)
#array([[193,  19],
#       [ 11, 346]], dtype=int64) : 교차분할표
type(con_mat) # numpy.ndarray 넘파이 행렬
acc3 = (con_mat[0,0] + con_mat[1,1]) / con_mat.sum() # 0.9472759226713533 = acc1, acc2

# 혹은
import pandas as pd
tab = pd.crosstab(y,y_pred,rownames=['관측치'], colnames=["예측치"])
acc4 = (tab.loc[0,0] + tab.loc[1,1])/len(y) # 0.9472759226713533


############################
### 2. 다항분류 모델
############################
# 1. 데이터셋
iris = load_iris()
iris.target_names # ['setosa', 'versicolor', 'virginica']

X, y = load_iris(return_X_y=True)
X.shape # (150, 4)
y.shape # (150,)
y # 0~2

# 2. 모델 생성
# 일반 데이터, 다항분류 solver='lbfgs', multi_class='multinomial' 
lr = LogisticRegression(random_state = 123, solver='lbfgs', multi_class='multinomial')
# sigmoid : 0~1 확률 -> 컷오프0.5 -> 이항분류
# softmax : 전체합 1이 되게끔 -> 0~1 확률 -> 1(c0:0.1, c1:0.1, c2:0.8) -> 다향분류
model = lr.fit(X,y)
y_pred = model.predict(X)         # y의 예측한 데이터의 이름인 0과 2 사이의 이름을 배출함
y_pred2 = model.predict_proba(X)  # 각 행은 해당하는 열에 대한 확률값을 배출함
y_pred2.shape                     # (150, 3) 각 행의 합은 1에 수렴함

# 3. 모델 평가
acc = accuracy_score(y, y_pred) # 0.9733333333333334
con_max = confusion_matrix(y, y_pred)
'''
array([[50,  0,  0],
       [ 0, 47,  3],
       [ 0,  1, 49]], dtype=int64)
'''
acc = (con_max[0,0] + con_max[1,1] + con_max[2,2]) / con_max.sum()
# 0.9733333333333334


# 히트맵 : 시각화
import seaborn as sn # heatmap - Accuracy Score

# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_max, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map 색상
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 18)
plt.show()


############################
### 3. digits -> multi class
############################
from sklearn.datasets import load_digits
# 1. dataset load
digits = load_digits()
digits.target_names # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 모델의 정답 이름
X = digits.data
y = digits.target
X.shape # (1797, 64) 1797장의 이미지
y.shape # (1797,)

# 2. data split
img_train, img_test, lable_train, lable_test = train_test_split(X, y, test_size=0.25)

# 이미지가 어떻게 생겼나
import matplotlib.pyplot as plt
img2d = img_train[0].reshape(-1,8,8)
img2d.shape
plt.imshow(img2d[0])
lable_train[0] # 2 이름 확인
img2d[0]
'''
array([[ 0.,  3., 13., 16.,  9.,  0.,  0.,  0.],
       [ 0., 10., 15., 13., 15.,  2.,  0.,  0.],
       [ 0., 15.,  4.,  4., 16.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  5., 16.,  2.,  0.,  0.],
       [ 0.,  0.,  1., 14., 13.,  0.,  0.,  0.],
       [ 0.,  0., 10., 16.,  5.,  0.,  0.,  0.],
       [ 0.,  4., 16., 13.,  8., 10.,  9.,  1.],
       [ 0.,  2., 16., 16., 14., 12.,  9.,  1.]]) 사진의 진짜 모습
'''
img_test.shape # (450, 64) # FM대로라면 3차원으로 해야되나, 걍 해도 된다



# 3. model 생성
lr = LogisticRegression(solver='lbfgs', multi_class='multinomial')
model = lr.fit(img_train, lable_train)
y_pred = model.predict(img_test)

# 4. model 평가
acc = accuracy_score(lable_test, y_pred)         # 0.9688888888888889
con_max = confusion_matrix(lable_test, y_pred)
'''
array([[50,  0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0, 39,  0,  0,  0,  0,  0,  0,  0,  1],
       [ 0,  0, 52,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0, 43,  0,  0,  0,  0,  0,  0],
       [ 0,  1,  0,  0, 47,  0,  0,  0,  0,  0],
       [ 0,  0,  1,  2,  0, 35,  0,  1,  0,  0],
       [ 0,  1,  0,  0,  0,  0, 48,  0,  0,  0],
       [ 0,  0,  0,  0,  1,  1,  0, 42,  0,  1],
       [ 0,  1,  0,  0,  0,  2,  0,  0, 44,  0],
       [ 0,  1,  0,  0,  0,  0,  0,  0,  0, 36]], dtype=int64)
'''
result = lable_test == y_pred
result.mean() # 0.9688888888888889 = acc
len(result) # 450

# 틀린 image
false_img = img_test[result==False]
false_img.shape # (14, 64)
false_img3d = false_img.reshape(-1,8,8)

false_img3d

for idx in range(false_img3d.shape[0]):
    print(idx)
    plt.imshow(false_img3d[idx])
    plt.show()































