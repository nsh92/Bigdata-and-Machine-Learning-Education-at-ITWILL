# -*- coding: utf-8 -*-
"""
Random Forest Hyper parameter : step02참고
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV

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

model = rf.fit(X,y)


# 3. 그리드 서치

# 3. gride search model 
grid_model = {'n_estimators':[100,200,300,400], 'max_depth':[3,6,8,10], 
              'min_samples_split':[2,3,4,5], 'min_samples_leaf':[1,3,5,7]}

gs = GridSearchCV(estimator=rf, param_grid=grid_model, scoring='accuracy', n_jobs=-1, cv=5)
# n_jobs=-1 : 모든 시피유 다 쓰겠다
model2 = gs.fit(X,y)

model2.cv_results_["mean_test_score"]
acc = model2.score(X,y) # 1.0


# 4. best score, best params
best_score = model2.score(X,y)
print('best score =',best_score)
best_params = model2.best_params_
print('best parameter =', best_params)
# {'max_depth': 6, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}
# best parameter이지만 과적합이 고려된 것은 아니









