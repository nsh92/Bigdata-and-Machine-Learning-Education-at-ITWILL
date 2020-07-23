# -*- coding: utf-8 -*-
"""
1. XGBoost Hyper parameter
2. model 학습 조기종료 : early stopping rounds
3. Best Hyper Parameter : Grid Search
"""
from xgboost import XGBClassifier
from xgboost import plot_importance 
from sklearn.datasets import make_blobs # 다항으로해보자
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report 

# 1. XGBoost Hyper parameter
X, y = make_blobs(n_samples=2000, n_features=4, centers=3, cluster_std=2.5)

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# 2. model
xgb = XGBClassifier(colsample_bylevel=1, 
                    learning_rate=0.3,
                    max_depth=3,
                    min_child_weight=1,
                    n_estimators=200) 

model = xgb.fit(x_train, y_train)
model

eval_set = [(x_test, y_test)] # 평가셋
                  
model_early = xgb.fit(X, y, eval_set=eval_set, eval_metric='merror',
                      early_stopping_rounds=100,
                      verbose=True) 
'''
X,y                   : 훈련셋
eval_set              : 평가셋
eval_metric           : 평가방법 : 이항error, 다항merror, 회귀rmse
early_stopping_rounds : 학습조기종료
verbose               : 학습 -> 평가 출력 유무
'''
score = model_early.score(x_test, y_test) # 1.0


# 3. Best Hyper paramether : Grid Search
from sklearn.model_selection import GridSearchCV
model

params = {'colsample_bylevel':[0.7,0.9], 'learning_rate':[0.01, 0.1],
          'max_depth':[3,5], 'min_child_weight':[1,3], 'n_estimators':[100,200]}

gs = GridSearchCV(estimator=xgb, param_grid=params, cv=5)

model = gs.fit(x_train, y_train, eval_set=eval_set, eval_metric='merror', verbose=True)

# best
model.best_score_  # 0.9992857142857143
model.best_params_
'''
{'colsample_bylevel': 0.7,
 'learning_rate': 0.01,
 'max_depth': 3,
 'min_child_weight': 1,
 'n_estimators': 100}
'''


