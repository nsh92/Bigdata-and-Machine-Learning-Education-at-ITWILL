# -*- coding: utf-8 -*-
"""
SVM model
 - 선형 SVM, 비선형 SVM
 - Hyper parameter(kernel, C, gamma)
"""
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

iris = pd.read_csv("C:/ITWILL/4_Python-II/data/iris.csv")
iris.info()

cols = list(iris.columns)
cols
x_cols = cols[:4]
y_cols = cols[-1]

train, test = train_test_split(iris, test_size=0.4, random_state=123)

svc = SVC(C=1.0, gamma='auto', kernel='rbf') # default : c=1.0, kernel='rbf'
# rbf : 비선형svm model 생성
svc2 = SVC(C=1.0, kernel='linear')

model = svc.fit(X=train[x_cols], y=train[y_cols])
model2 = svc2.fit(X=train[x_cols], y=train[y_cols])

y_pred = model.predict(X=test[x_cols])
y_true = test[y_cols]

acc = accuracy_score(y_true, y_pred)
acc # 0.9666666666666667

y_pred2 = model2.predict(X=test[x_cols])
y_true2 = test[y_cols]
acc2 = accuracy_score(y_true2, y_pred2)
acc2 # 0.9666666666666667
# 아이리스의 경우 선형과 비선형의 차이가 없내
# 가장 좋은 것은 돌리기 전에 산점도를 보고 선형이냐 비선형이냐 판단하는 거임
# 파라미터를 여러 차례 뿅뿅해서 최적화된 값을 찾아야되는데
# 이걸 또 도와주는 것이 하이퍼 파라미터 및 그리드 서치라고 함


##########################################
### Grid Search
##########################################
# Hyper parameter(kernel, C, gamma)

# C, gamma
params = [0.001, 0.01, 0.1, 1, 10, 100]  # e-3 ~ e+2 # 0은 넣으면 안댐
kernel = ['linear', 'rbf']
best_score = 0
best_parameter = {}

for k in kernel:
    for gamma in params:
        for C in params:
            svc = SVC(kernel = k, gamma = gamma, C = C)
            model = svc.fit(X=train[x_cols], y=train[y_cols])
            score = model.score(test[x_cols], test[y_cols])
            
            if score > best_score:
                best_score = score
                best_parameter = {'kernel':k, 'gamma':gamma, 'C':C}

print('best score =', best_score)
print('best parameter =', best_parameter)






























