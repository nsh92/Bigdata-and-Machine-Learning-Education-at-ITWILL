# -*- coding: utf-8 -*-
"""
XGBoost model
아나콘다 프롬프트에서 install
"""
from xgboost import XGBClassifier, XGBRFRegressor
from xgboost import plot_importance # 중요변수 시각화
from sklearn.datasets import make_blobs # 클러스터 데이터셋 생성
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 1. dataset load
X, y = make_blobs(n_samples=2000, n_features=4, centers=2, cluster_std=2.5)
                   # 표본 수,      x변수 수,    집단 수(y변수)      표준편차=허용가능한 오차수준

X.shape # (2000, 4)
y.shape # (2000,)  # [0, 0, 0, ..., 0, 1, 1]
# centers가 3 이상이 되면 다항분류가 되겠지

plt.scatter(x=X[:,0], y=X[:,1], s=100, c=y, marker='o')
plt.show()


# 2. train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3)


# 3. model
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model


# 4. model 평가
y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred) # 1.0
report = classification_report(y_test, y_pred)
print(report)


# 5. 중요변수 시각화
plot_importance(model)
plt.show()
## 중요변수 별도로 추출 가능
model.get_booster().get_fscore() # {'f1': 23}


# 데이터 좀 다르게
X, y = make_blobs(n_samples=2000, n_features=4, centers=3, cluster_std=2.5)
y # [1, 2, 1, ..., 0, 0, 1]
plt.scatter(x=X[:,0], y=X[:,1], s=100, c=y, marker='o')
plt.show()
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model # objective='multi:softprob' : 알아서 다항, 소프트맥스로 바뀐 거 확인
y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred) # 0.9866666666666667
report = classification_report(y_test, y_pred)
print(report)
plot_importance(model)
plt.show()
model.get_booster().get_fscore() #  {'f0': 313, 'f2': 270, 'f3': 302, 'f1': 277}

model
# n_estimators=100          : tree 수
# learning_rate=0.300000012 : 학습률 : 정확도와 정비례, 커질수록 느려짐










