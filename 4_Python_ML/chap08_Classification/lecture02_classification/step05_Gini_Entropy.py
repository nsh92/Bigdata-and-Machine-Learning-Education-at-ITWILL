# -*- coding: utf-8 -*-
"""
지니 불순도, 엔트로피
 - 트리 모델에 중요변수 선정 기준
 - 정보이득 = base 지수 - Gini 불순도 or entropy
 - 정보이득이 클수록 중요변수로 본다
 - 불확실성이 작아질수록 정보의 효용이 커진다
 - Gini impurity = sum(p*(1-p))
 - Entropy = -sum(p*log(p))
"""
import numpy as np

# 1. 불확실성이 큰 경우
x1 = 0.5; x2 = 0.5 # 전체확률 1

gini = sum([x1*(1-x1), x2*(1-x2)]) # 0.5

entropy = -sum([x1*np.log2(x1), x2*np.log2(x2)]) # 1.0 : 가장 불확실성이 큼

'''
cost(loss) function : 정답과 예측치 -> 오차 반환 함수
x1 -> y_true, x2 -> y_pred
y_true = x1*np.log2(x1)
y_pred = x2*np.log2(x2)
'''
y_true = x1*np.log2(x1)
y_pred = x2*np.log2(x2)
cost = -sum([y_true, y_pred])
print('cost =', cost) # cost = 1.0 : 정답과 예측차가 제일 큼 : 비용이 제일 큼


# 2. 불확실성이 작은 경우
x1 = 0.9; x2 = 0.1 # 전체확률 1
gini = sum([x1*(1-x1), x2*(1-x2)])               # 0.18
entropy = -sum([x1*np.log2(x1), x2*np.log2(x2)]) # 0.4689955935892812
# cost가 1에서 0.4로 줄었음 : 불확실성이 현저히 줄었다


#######################################
### dataset 적용
#######################################
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']] # X1, X2, label
    columns = ['dark_clouds','gust'] # X1, X2의 이름
    
    return dataSet, columns
dataSet, columns = createDataSet()
type(dataSet) # 리스트임
dataset = np.array(dataSet)
dataset.shape # (5, 3)
columns

X = dataset[:, :2]
y = dataset[:, 2]
y = [1 if d == 'yes' else 0 for d in y]
y # [1, 1, 0, 0, 0]

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score
from sklearn import tree

dt = DecisionTreeClassifier()
model = dt.fit(X, y) # default : 지니계수를 선정함

pred = model.predict(X)
acc = accuracy_score(y, pred)
acc # 1.0

tree.plot_tree(model)
export_graphviz(model, out_file='dataset_tree.dot',
                max_depth=3, feature_names=columns)

# 엔트로피로 하고자 한다면 이렇게
dt = DecisionTreeClassifier('entropy')
model = dt.fit(X, y)
pred = model.predict(X)
acc = accuracy_score(y, pred)
acc
tree.plot_tree(model)


















