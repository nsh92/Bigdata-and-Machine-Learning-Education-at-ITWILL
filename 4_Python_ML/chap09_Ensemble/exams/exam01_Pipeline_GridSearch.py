'''
 문) digits 데이터 셋을 이용하여 다음과 단계로 Pipeline 모델을 생성하시오.
  <단계1> dataset load
  <단계2> Pipeline model 생성
          - scaling : StndardScaler 클래스, modeing : SVC 클래스    
  <단계3> GridSearch model 생성
          - params : 10e-2 ~ 10e+2, 평가방법 : accuracy, 교차검정 : 5겹
          - CPU 코어 수 : 2개 
  <단계4> best score, best params 출력 
'''

from sklearn.datasets import load_digits # dataset 
from sklearn.svm import SVC # model
from sklearn.model_selection import GridSearchCV # gride search model
from sklearn.pipeline import Pipeline # pipeline
from sklearn.preprocessing import StandardScaler # dataset scaling
from sklearn.model_selection import train_test_split
# 1. dataset load
digits = load_digits()
X = digits.data
y = digits.target
X.shape
X.min() # 0
X.max() # 16

# 2. pipeline model : data 표준화 -> model 
pipe_model = Pipeline([('scaler', StandardScaler()), ('svc', SVC(random_state=1))])

# 3. gride search model 
params = [0.01, 0.1, 1.0, 10.0, 100.0]
grid_model = [{'svc__C':params, 'svc__kernel':['linear']},                     
              {'svc__C':params, 'svc__gamma':params, 'svc__kernel':['rbf']}]

gs = GridSearchCV(estimator=pipe_model, param_grid=grid_model, scoring='accuracy', n_jobs=2, cv=5)
model = gs.fit(X,y)

model.cv_results_["mean_test_score"]

# 4. best score, best params
best_score = model.score(X,y)
print('best score =',best_score)
best_params = model.best_params_
print('best parameter =', best_params)
