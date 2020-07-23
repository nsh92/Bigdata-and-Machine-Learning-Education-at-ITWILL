# -*- coding: utf-8 -*-
from step01_kNN_data import data_set
know, not_know, cate = data_set()

class kNNClassify:
    # 생성자, 멤버(메소드, 변수)
    def knn_classfy(self, know, not_know, cate, k):
        # 단계1. 유클리디안 거리계산
        diff = know - not_know
        square_diff = diff ** 2
        sum_square_diff = square_diff.sum(axis = 1)
        distance = np.sqrt(sum_square_diff)
        
        # 단계2. 오름차순 인덱싱
        sortDist = distance.argsort()
        
        # 단계3. 최근접 이웃 및 보팅
        self.class_re = {}  # 멤버변수
        for i in range(k):
            key = cate[sortDist[i]]
            self.class_re[key] = self.class_re.get(key, 0) + 1

    def vote(self):
        vote_re = max(self.class_re)
        print('분류결과 :', vote_re)

# 객체 생성
knn = kNNClassify()
knn.knn_classfy(know, not_know, cate, 3)
knn.vote()











































