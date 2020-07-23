# -*- coding: utf-8 -*-
"""
Decision Tree 모델
 - 중요변수 선정 기준 : GINI, Entropy
 - GINI : 불확실성을 개선하는데 기여하는 척도
 - Entropy : 불확실성을 나타내는 지수
 - 둘다 작을수록 불확실성이 낮은 거임
"""
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_wine
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree.export import export_text # tree 구조 텍스트로 시각화
from sklearn import tree                    # 시각화 관련

iris = load_iris()
iris.target_names  # ['setosa', 'versicolor', 'virginica']
names = iris.feature_names # 이런식으로도 집단 이름 추출 가능
X = iris.data
y = iris.target
X.shape # (150, 4)
y.shape # (150,)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

help(DecisionTreeClassifier)

dtc = DecisionTreeClassifier(criterion='gini', random_state=123, max_depth=3)
model = dtc.fit(X=x_train,y=y_train)


# tree 모델 시각화
tree.plot_tree(model) # 팝업창으로 뜸
print(export_text(model))
''' 
|--- feature_2 <= 2.50
|   |--- class: 0
|--- feature_2 >  2.50
|   |--- feature_3 <= 1.75
|   |   |--- feature_2 <= 5.35
|   |   |   |--- class: 1
|   |   |--- feature_2 >  5.35
|   |   |   |--- class: 2
|   |--- feature_3 >  1.75
|   |   |--- feature_2 <= 4.85
|   |   |   |--- class: 2
|   |   |--- feature_2 >  4.85
|   |   |   |--- class: 2
feature = 변수
class = 분류결과(setosa = 0 등)
'''

print(export_text(model, names))
'''
|--- petal length (cm) <= 2.50
|   |--- class: 0
|--- petal length (cm) >  2.50
|   |--- petal width (cm) <= 1.75
|   |   |--- petal length (cm) <= 5.35
|   |   |   |--- class: 1
|   |   |--- petal length (cm) >  5.35
|   |   |   |--- class: 2
|   |--- petal width (cm) >  1.75
|   |   |--- petal length (cm) <= 4.85
|   |   |   |--- class: 2
|   |   |--- petal length (cm) >  4.85
|   |   |   |--- class: 2
이런식으로 더 보기 좋게 가능
'''

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred) # 0.9333333333333333
con = confusion_matrix(y_true, y_pred)
'''[[12,  0,  0],
    [ 0, 16,  0],
    [ 0,  3, 14]]'''


########### 모델의 파라미터를 바꿔보자 #####################
dtc2 = DecisionTreeClassifier(criterion='entropy', random_state=123, max_depth=2)
model2 = dtc2.fit(X=x_train,y=y_train)
tree.plot_tree(model2) # 똑같은 변수를 가장 중요하게 꼽았음, 근대 뎁스가 깊은 것이 더 정확함
print(export_text(model, names))
y_pred2 = model2.predict(x_test)
y_true2= y_test
acc2 = accuracy_score(y_true2, y_pred2)    # 0.9111111111111111
con2 = confusion_matrix(y_true2, y_pred2)
'''[[12,  0,  0],
    [ 0, 16,  0],
    [ 0,  4, 13]]'''


dtc3 = DecisionTreeClassifier(criterion='entropy', random_state=123)
model3 = dtc3.fit(X=x_train,y=y_train)
tree.plot_tree(model3) # 뎁스를 생략하니 최대한 정확도를 높이도록 최대한의 깊이로 갔음
# 물론 이렇게하면 과적합에 대한 고려도 동시에 생기는 법임


################# 오버피팅을 고려하자 #################################
wine = load_wine()
X=wine.data
y=wine.target
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)
dt = DecisionTreeClassifier()
model = dt.fit(x_train, y_train)
train_score = model.score(x_train, y_train)  # 1.0
test_score = model.score(x_test, y_test)     # 0.9629629629629629

tree.plot_tree(model) # 뎁스 : 5

# 다른 모델 뎁스3짜리
dt2 = DecisionTreeClassifier(max_depth=3)
model2 = dt2.fit(x_train, y_train)
train_score2 = model2.score(x_train, y_train)  # 1.0
test_score2 = model2.score(x_test, y_test)     # 0.9629629629629629

tree.plot_tree(model2)
# 뭐 암튼 오버피팅을 주의하여 파라미터를 잘 조절해야 한다

################### graphviz설치 ###############################
export_graphviz(model2, out_file='DT_tree_graph.dot',
                feature_names=wine.feature_names, max_depth=3, 
                class_names=True)
# 이제 갓 생긴 파일은 걍 텍스트고 설치한 프로그램으로 열어야 함



































