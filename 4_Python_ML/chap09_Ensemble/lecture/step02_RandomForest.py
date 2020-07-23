# -*- coding: utf-8 -*-
"""
Random Forest Ensemble model
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# 1. dataset load
wine = load_wine()
wine.feature_names # X변수명들
wine.target_names  # y범주이름들 ['class_0', 'class_1', 'class_2']

X = wine.data
y = wine.target
X.shape # (178, 13)
y.shape # (178,)


# 2. RF model
rf = RandomForestClassifier()
'''
n_estimators      : 트리 수 기본값100
criterion         : 중요변수 선정 기준 기본값:지니
max_depth         : 트리의 깊이 기본값없음
min_samples_split : 노드 분할에 사용할 최소 샘플 수 기본값2
min_samples_leaf  : 단노드 분할 최소 샘플 수(터미널 노드) 기본값1
max_feature       : 최대 x변수 사용 수 기본값1
n_jobs            : cpu 수 기본값없음
random_state      : 시드값 지정 기본값없음
'''
import numpy as np
idx = np.random.choice(a=X.shape[0], size=int(X.shape[0]*0.7), replace=False)

X_train = X[idx]
y_train = y[idx]

model = rf.fit(X_train,y_train)

idx_test = [i for i in range(len(y)) if not i in idx]
len(idx_test) # 54

X_test = X[idx_test]
y_test = y[idx_test]

y_pred = model.predict(X_test)
y_true = y_test

confusion_matrix(y_true, y_pred)
'''[[18,  0,  0],
    [ 0, 19,  1],
    [ 0,  0, 16]]'''
acc = accuracy_score(y_true, y_pred) # 0.9814814814814815
report = classification_report(y_true, y_pred)
print(report) # 이렇게 해줘야 깔끔하게 출력됨
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        18
           1       1.00      0.95      0.97        20
           2       0.94      1.00      0.97        16

    accuracy                           0.98        54
   macro avg       0.98      0.98      0.98        54
weighted avg       0.98      0.98      0.98        54
'''

print(model.feature_importances_)
#[0.12552133 0.01974698 0.01660979 0.02279754 0.04214117 0.0388188
# 0.16696258 0.00943387 0.02355585 0.15558198 0.07465116 0.12078643
# 0.18339253] 13개의 변수에 대하여 중요한 수준을 반환
model.feature_names # 이거랑 같이 봐야함


## 중요변수 시각화
import matplotlib.pyplot as plt
x_size = X.shape[1] # 컬럼 수
plt.barh(range(x_size), model.feature_importances_)  # (y, x)
plt.yticks(range(x_size), wine.feature_names)
plt.xlabel('importance')
plt.show()

model.best_param_













