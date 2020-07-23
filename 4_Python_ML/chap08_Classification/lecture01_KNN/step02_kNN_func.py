# -*- coding: utf-8 -*-
from step01_kNN_data import data_set


know, not_know, cate = data_set()

# 거리계산식 : 차 > 제곱 > 합 > 제곱근
diff = know - not_know
diff
square_diff = diff ** 2
square_diff
sum_square_diff = square_diff.sum(axis = 1) # 행단위합계
sum_square_diff # (4,)
distance = np.sqrt(sum_square_diff)
distance # array([0.47169906, 0.61846584, 0.20615528, 0.40311289]) 최종적으로 계산된 거리
cate # ['A', 'A', 'B', 'B'] : 정답지 # B에 가깝내 : B에 속한다 를 프로그래밍해야 함

sortDist = distance.argsort() # 해당 객체를 오름차순으로 소트
sortDist # [2, 3, 0, 1]       # 오름차순에 따른 순서 번호를 반환
result = cate[sortDist]
result                        # ['B', 'B', 'A', 'A']

# k = 3 : 최근접 이웃 3개
result[:3] # ['B', 'B', 'A']
k3 = result[:3]

# dict
classify_result = {}
for key in k3:
    classify_result[key] = classify_result.get(key, 0) + 1

classify_result # {'B': 2, 'A': 1} : B는 2번, A는 1번
# b가 2, a도 2 이러면 보팅을 못하니까 k는 홀수이어야 함

vote_re = max(classify_result)
print('분류결과 :', vote_re) # 분류결과 : B


# 이 과정을 함수로 만들자
def knn_classfy(know, not_know, cate, k):
    # 단계1. 유클리디안 거리계산
    diff = know - not_know
    square_diff = diff ** 2
    sum_square_diff = square_diff.sum(axis = 1)
    distance = np.sqrt(sum_square_diff)
    
    # 단계2. 오름차순 인덱싱
    sortDist = distance.argsort()
    
    # 단계3. 최근접 이웃 및 보팅
    class_re = {}
    for i in range(k):
        key = cate[sortDist[i]]
        class_re[key] = class_re.get(key, 0) + 1

    return class_re

class_re = knn_classfy(know, not_know, cate, 3)
# {'B': 2, 'A': 1}
print('분류결과 :', max(class_re))

# 이 과정을 클래스로 정의하자
















