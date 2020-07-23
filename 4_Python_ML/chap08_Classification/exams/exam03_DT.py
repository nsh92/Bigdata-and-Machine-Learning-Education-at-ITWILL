'''
 문) load_breast_cancer 데이터 셋을 이용하여 다음과 같이 Decision Tree 모델을 생성하시오.
 <조건1> 75:25비율 train/test 데이터 셋 구성 
 <조건2> y변수 : cancer.target, x변수 : cancer.data 
 <조건3> 중요변수 확인 

'''
import pandas as pd
from sklearn import model_selection
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# 데이터 셋 load 
cancer = load_breast_cancer()
print(cancer)
print(cancer.DESCR)

# 변수 선택 
X = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
dtc = DecisionTreeClassifier(criterion='gini', random_state=123)
model = dtc.fit(X=x_train,y=y_train)
tree.plot_tree(model)
print(export_text(model))

# 20번째 변수가 제일 중요함

y_pred = model.predict(x_test)
y_true = y_test
acc = accuracy_score(y_true, y_pred) # 0.958041958041958
con = confusion_matrix(y_true, y_pred)
'''[[53,  2],
    [ 4, 84]]'''


dtc = DecisionTreeClassifier(max_depth=3)
model = dtc.fit(X=x_train,y=y_train)
tree.plot_tree(model)
print(export_text(model))



