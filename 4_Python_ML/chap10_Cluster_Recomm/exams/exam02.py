# -*- coding: utf-8 -*-
"""
문2) 아래와 같은 단계로 kMeans 알고리즘을 적용하여 확인적 군집분석을 수행하시오.

 <조건> 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
                   visit_count : 매장방문횟수, avg_price : 평균구매액

  단계1 : 3개 군집으로 군집화
 
  단계2: 원형데이터에 군집 예측치 추가
  
  단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)
  
  단계4 : 산점도에 군집의 중심점 시각화
"""

import pandas as pd
from sklearn.cluster import KMeans # kMeans model
import matplotlib.pyplot as plt
sales = pd.read_csv("C:/ITWILL/4_Python-II/data/product_sales.csv")
print(sales.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
tot_price      150 non-null float64 -> 총구매금액 
visit_count    150 non-null float64 -> 매장방문수 
buy_count      150 non-null float64 -> 구매횟수 
avg_price      150 non-null float64 -> 평균구매금액 
'''

kmeans = KMeans(n_clusters=3, algorithm='auto')
model = kmeans.fit(sales)
model
pred = model.predict(sales)

sales.corr() # avg_price
sales['cluster'] = pred
center = model.cluster_centers_

plt.scatter(x=sales['tot_price'], y=sales['avg_price'], c=sales['cluster'], marker='o') # 군집표시
plt.scatter(x=center[:,0], y=center[:,3], c='RED', marker='D')                         # 중심점 표시
plt.show()
