# -*- coding: utf-8 -*-
"""
kMeans 알고리즘
 - 비계층적(확인적) 군집분석
 - 군집수(k) 알고 있는 경우 이용
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. 데이터셋
# 텍스트->넘파이 해주는 함수 정의
def dataMat(file):
    dataset = [] # data mart 개념
    f = open(file, mode='r')
    lines = f.readlines()
    for line in lines:
        cols = line.split('\t')
        rows = []
        for col in cols:
            rows.append(float(col))
        dataset.append(rows)
    return np.array(dataset)
        
dataset = dataMat('C:/ITWILL/4_Python-II/data/testSet.txt')

dataset.shape
dataset[:5]

dataset_df = pd.DataFrame(dataset, columns = ['x', 'y'])
dataset_df.info()


# 모델 생성
kmeans = KMeans(n_clusters=4, algorithm='auto')

model = kmeans.fit(dataset_df)
model
'''
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
       n_clusters=4, n_init=10, n_jobs=None, precompute_distances='auto',
       random_state=None, tol=0.0001, verbose=0)
'''
pred = model.predict(dataset_df)
pred # 0~3


# 각 cluster의 센터
center = model.cluster_centers_
'''
array([[-2.46154315,  2.78737555,  3.        ],
       [ 2.80293085, -2.7315146 ,  2.        ],
       [-3.38237045, -2.9473363 ,  0.        ],
       [ 2.6265299 ,  3.10868015,  1.        ]])
'''

# 시각화
dataset_df['cluster'] = pred
dataset_df.head()

plt.scatter(x=dataset_df['x'], y=dataset_df['y'], c=dataset_df['cluster'], marker='o') # 군집표시
plt.scatter(x=center[:,0], y=center[:,1], c='RED', marker='D')                         # 중심점 표시
plt.show()

grp = dataset_df.groupby('cluster')
grp.mean()
'''
                x         y
cluster                    
0       -3.382370 -2.947336
1        2.626530  3.108680
2        2.802931 -2.731515
3       -2.461543  2.787376
'''

