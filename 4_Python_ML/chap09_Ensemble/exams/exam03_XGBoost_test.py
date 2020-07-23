'''
 문) iris dataset을 이용하여 다음과 같은 단계로 XGBoost model을 생성하시오.
'''

import pandas as pd # file read
from xgboost import XGBClassifier # model 생성 
from xgboost import plot_importance # 중요변수 시각화  
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report # model 평가 


# 단계1 : data set load 
iris = pd.read_csv("C:/ITWILL/4_Python-II/data/iris.csv")

# 변수명 추출 
cols=list(iris.columns)
col_x=cols[:4] # x변수명 
col_y=cols[-1] # y변수명 

# 단계2 : 훈련/검정 데이터셋 생성
train_set, test_set = train_test_split(iris, test_size=0.25)
type(train_set)

# 단계3 : model 생성 : train data 이용
xgb = XGBClassifier()
model = xgb.fit(train_set[col_x], train_set[col_y])

# 단계4 :예측치 생성 : test data 이용  
pred = model.predict(test_set[col_x])

# 단계5 : 중요변수 확인 & 시각화  
model.get_booster().get_fscore()
'''
{'Petal.Length': 142,
 'Petal.Width': 102,
 'Sepal.Length': 32,
 'Sepal.Width': 50}
'''
plot_importance(model)
plt.show()

# 단계6 : model 평가 : confusion matrix, accuracy, report
confusion_matrix(test_set[col_y], pred)
'''
[[14,  0,  0],
 [ 0, 10,  3],
 [ 0,  2,  9]]'''
acc = accuracy_score(test_set[col_y], pred) # 0.868421052631579
report = classification_report(test_set[col_y], pred)
print(report)
'''
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        14
  versicolor       0.83      0.77      0.80        13
   virginica       0.75      0.82      0.78        11

    accuracy                           0.87        38
   macro avg       0.86      0.86      0.86        38
weighted avg       0.87      0.87      0.87        38
'''

## 확률로 예측치 생성
pred2 = model.predict_proba(test_set[col_x])
pred2_dit = pred2.argmax(axis=1)
## 차원 축소가 관찰





