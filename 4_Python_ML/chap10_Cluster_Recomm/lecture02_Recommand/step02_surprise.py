# -*- coding: utf-8 -*-
"""
SVD 알고리즘 - 추천시스템
"""
from surprise import SVD, accuracy    # 모델생성 / 평가
from surprise import Reader, Dataset  # 데이터셋 생성
import pandas as pd

# 1. 데이터
ratings = pd.read_csv("C:/ITWILL/4_Python-II/data/movie_rating.csv")
print(ratings)

# 2. rating 데이터 생성
reader = Reader(rating_scale=(1,5))
data = Dataset(reader)
dataset = data.load_from_df(ratings[['critic','title','rating']], reader)

# train / test
train = dataset.build_full_trainset()
test = train.build_anti_testset()

# 모델 생성
svd = SVD()
model = svd.fit(train)

# 3. 전체 사용자 대상 예측치
pred = model.test(test) # predict말고 test, predict는 개별 사용자에 대한 예측치
pred
# Prediction(uid='Jack', iid='Just My', r_ui=3.225806451612903, est=3.19769380841094, details={'was_impossible': False})
# 잭이라는 놈의 Just My란 영화에 대한 예측치    실제평점           모델에 의해 추정된평점

'''
uid='Toby', iid='Lady', r_ui=3.225806451612903, est=2.9190166872533134     : 가장 낮은 추정 평점
uid='Toby', iid='The Night', r_ui=3.225806451612903, est=3.144031930830455 : 가장 높은 추정 평점
uid='Toby', iid='Just My', r_ui=3.225806451612903, est=2.888897922860577
'''

# 4. 개별 사용자 대상 예측치
user_id = 'Toby' # 추천 대상자
items_id = ['The Night', 'Just My', 'Lady'] # 토비가 미관람한 영화, 평점에 의한 리스트를 가독성있게 출력하자
actual_rating = 0

for item in items_id:
    print(model.predict(user_id, item, actual_rating))
'''
user: Toby       item: The Night  r_ui = 0.00   est = 3.14   {'was_impossible': False}
user: Toby       item: Just My    r_ui = 0.00   est = 2.89   {'was_impossible': False}
user: Toby       item: Lady       r_ui = 0.00   est = 2.92   {'was_impossible': False}
'''








