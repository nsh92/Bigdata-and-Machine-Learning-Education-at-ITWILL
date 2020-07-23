# -*- coding: utf-8 -*-
"""
계층적 군집분석
 - 상향식(Bottom-up)으로 계층적 군집 형성
 - 유클리디안 거리계산식 이용
 - 숫자형 변수만 가능
"""
import pandas as pd
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# 1. 데이터셋
iris = load_iris()
iris.feature_names
X = iris.data
y = iris.target
iris_df = pd.DataFrame(X, columns=iris.feature_names)
species = pd.Series(y)
iris_df['species'] = species 
iris_df.info()

# 2. 계층적 군집분석
clusters = linkage(iris_df, method='complete', metric='euclidean')
'''method 파라미터
1. single   : 단순연결
2. complete : 완전연결
3. average  : 평균연결
'''
clusters # 거리값들이 배출됨
clusters.shape # (149, 4)

# 3. 덴드로그램 시각화
plt.figure(figsize=(20,5))
dendrogram(clusters, leaf_rotation=90, leaf_font_size=20,)
plt.show()
## 근대 이걸 또 어떻게, 몇 개로 쪼갤 것인지는 사용자가 판단해야 함

# 4. 클러스터 자르기 : 덴드로그램으로 판단
from scipy.cluster.hierarchy import fcluster # cluster자르기
## 1) 클러스터 자르기
cluster = fcluster(clusters, t=3, criterion='distance')
cluster # 1~3

## 2) DF 컬럼 추가
iris_df['cluster'] = cluster
iris_df.info()
iris_df.head()
iris_df.tail()

## 3) 산점도 시각화
plt.scatter(x=iris_df['sepal length (cm)'], y=iris_df['petal length (cm)'], c=iris_df['cluster'], marker='o')
plt.show()

## 4) 관측치 vs 예측치
tab = pd.crosstab(index=iris_df['species'], columns=iris_df['cluster'])
tab
'''
cluster   1   2   3
species            
0        50   0   0
1         0   0  50
2         0  34  16 
'''
## 5) 군집별 특성 분석
## DF.groupby('집단변수')
cluster_grp = iris_df.groupby('cluster')
cluster_grp.size()
cluster_grp.mean()
'''      sepal length (cm)  sepal width (cm)  ...  petal width (cm)   species
cluster                                       ...                            
1                 5.006000          3.428000  ...          0.246000  0.000000
2                 6.888235          3.100000  ...          2.123529  2.000000
3                 5.939394          2.754545  ...          1.445455  1.242424'''






