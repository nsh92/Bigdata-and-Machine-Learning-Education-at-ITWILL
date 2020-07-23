'''
문) load_wine() 함수를 이용하여 와인 데이터를 다항분류하는 로지스틱 회귀모델을 생성하시오. 
  조건1> train/test - 7:3비울
  조건2> y 변수 : wine.data 
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# 1. wine 데이터셋 
wine = load_wine()

# 2. 변수 선택 
wine_x = wine.data # x변수 
wine_y = wine.target # y변수

# 3. train/test split(7:3)
wx_train, wx_test, wy_train, wy_test = train_test_split(wine_x, wine_y, random_state = 123, test_size=0.3)

# 4. model 생성  : solver='lbfgs', multi_class='multinomial'
lr = LogisticRegression(random_state = 123, solver='lbfgs', 
                        multi_class='multinomial', 
                        max_iter=200, # 반복횟수(기본값100)
                        n_jobs=1,     # 병렬처리cpu수(속도개선)
                        verbose=1)    # 학습과정 출력여부
wmodel = lr.fit(wx_train, wy_train)

# 5. 모델 평가 : accuracy, confusion matrix
wy_pred = wmodel.predict(wx_test)  
wy_pred2 = wmodel.predict_proba(wx_test)  

acc0 = wmodel.score(wx_test, wy_test) # 0.9444444444444444
acc = metrics.accuracy_score(wy_test, wy_pred)  # 0.9444444444444444
con_max = metrics.confusion_matrix(wy_test, wy_pred)
'''
array([[13,  1,  0],
       [ 1, 17,  0],
       [ 0,  1, 21]], dtype=int64)
'''
acc1 = (con_max[0,0] + con_max[1,1] + con_max[2,2]) / con_max.sum() # 0.9444444444444444
