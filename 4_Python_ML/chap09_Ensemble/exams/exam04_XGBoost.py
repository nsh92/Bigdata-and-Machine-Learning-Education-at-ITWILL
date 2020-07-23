'''
외식업종 관련 data set 분석

문) food_df를 대상으로 다음과 같이 xgboost 모델을 생성하시오.
   <조건1> 6:4 비율 train/test set 생성 
   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
   <조건3> 중요변수에 대한  f1 score 출력
   <조건4> 중요변수 시각화  
   <조건5> accuracy와 model report 출력 
'''

import pandas as pd
from sklearn import model_selection, metrics
from sklearn.preprocessing import minmax_scale # 정규화 함수 
from xgboost import XGBClassifier # xgboost 모델 생성 
from xgboost import plot_importance # 중요변수 시각화  
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 중요변수 시각화 
from matplotlib import pyplot
from matplotlib import font_manager, rc # 한글 지원
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 외식업종 관련 data set
food = pd.read_csv("C:/ITWILL/4_Python-II/data/food_dataset.csv",encoding="utf-8",thousands=',')

# 결측치 제거
food=food.dropna()  
print(food.info())


y = food.iloc[:,-1]
X = food.iloc[:,:20]

x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.4)

xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)

fscore = model.get_booster().get_fscore()
'''
{'소재지면적': 486,
 '주변': 346,
 'bank': 256,
 '기간평균': 509,
 'pop': 243,
 'X1km_초등학교갯수': 98,
 'X1km_영화관갯수': 91,
 'X1km_고등학교갯수': 88,
 '유동인구_주중_오전': 313,
 '유동인구_주말_오전': 271,
 'tax_sum': 222,
 'X1km_지하철역갯수': 92,
 '유동인구_주중_오후': 280,
 '유동인구_주말_오후': 278,
 'X1km_병원갯수': 147,
 'nonbank': 234,
 'X3km_대학교갯수': 127,
 '주변동종': 221,
 '위생업태명': 116}'''
plot_importance(model)
plt.show()

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred) # 0.7873832624732003
report = classification_report(y_test, y_pred)
print(report)
'''           precision    recall  f1-score   support

           0       0.80      0.98      0.88     21654  전반적으로 예측을 잘 하는 것으로 보이나,
           1       0.51      0.09      0.15      5865  f1을 봤을 때, 1을 잘 예측못하내

    accuracy                           0.79     27519
   macro avg       0.65      0.53      0.51     27519
weighted avg       0.74      0.79      0.72     27519      '''
