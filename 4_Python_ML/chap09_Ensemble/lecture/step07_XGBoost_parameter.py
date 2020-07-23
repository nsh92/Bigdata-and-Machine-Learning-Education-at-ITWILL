# -*- coding: utf-8 -*-
"""
1. XGBoost Hyper parameter
2. model 학습 조기종료 : early stopping rounds
3. Best Hyper Parameter : Grid Search
"""
from xgboost import XGBClassifier
from xgboost import plot_importance 
from sklearn.datasets import load_breast_cancer # 이항
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report 

# 1. XGBoost Hyper parameter
X, y= load_breast_cancer(return_X_y=True)

X.shape # (569, 30)
y # 0,1
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model
'''
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
              importance_type='gain', interaction_constraints='',
              learning_rate=0.300000012, max_delta_step=0, max_depth=6,
              min_child_weight=1, missing=nan, monotone_constraints='()',
              n_estimators=100, n_jobs=0, num_parallel_tree=1,
              objective='binary:logistic', random_state=0, reg_alpha=0,
              reg_lambda=1, scale_pos_weight=1, subsample=1,
              tree_method='exact', validate_parameters=1, verbosity=None)

대표적 파라미터
- colsample_bylevel=1         : 트리 모델 생성시 훈련셋의 샘플링 비율 (1=100%, 보통 0.6~1)
- learning_rate=0.3           : 학습율(보통0.01 ~ 0.1)
- max_depth=6                 : 트리의 깊이, 과적합 관련
- min_child_weight=1          : 자식 노드 분할을 결정하는 최소 가중치들의 합 : 역시 과적합 관련
- n_estimators=100            : 트리 모델 수 : 이 수만큼 만들어내고 비교한다
- objective='binary:logistic' : 이항인지 다항인지 : 알고리즘이 자동으로 판단함
'''

# 2. model 학습 조기종료 : early stopping rounds : 더 좋은 모델을 찾기위해 더 반복적으로 수행할 의미가 없다
xgb = XGBClassifier(colsample_bylevel=1, 
                    learning_rate=0.3,
                    max_depth=6,
                    min_child_weight=1,
                    n_estimators=100,
                    objective='binary:logistic') # 원래 이런 내용이 담겨있는거지 ()안에

eval_set = [(x_test, y_test)] # 평가셋
                  
model_early = xgb.fit(X, y, eval_set=eval_set, eval_metric='error',
                      early_stopping_rounds=50, # n_estimators=100이나, 50번째 되었을때 개선되지 않으면 종료하셈
                      verbose=True) # 위 과정을 화면상에 출력해줘라
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

# 디폴트 모델 객체 생성
xgb2 = XGBClassifier()
params = {'colsample_bylevel':[0.6,0.8,1.0], 'learning_rate':[0.01, 0.1, 0.5],
          'max_depth':[3,5,7], 'min_child_weight':[1,3,5], 'n_estimators':[100,300,500]}

gs = GridSearchCV(estimator=xgb2, param_grid=params, cv=5)

model = gs.fit(x_train, y_train, eval_set=eval_set, eval_metric='error', verbose=True)

# best
model.best_score_ # 0.9599050632911392
model.best_params_
'''
{'colsample_bylevel': 0.8,
 'learning_rate': 0.1,
 'max_depth': 3,
 'min_child_weight': 1,
 'n_estimators': 300}
'''




















