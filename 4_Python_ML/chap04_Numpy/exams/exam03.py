'''
step03_reshape 관련문제
문) 다음과 같이  단계별로 자료구조를 생성하시오.
    단계1 : 1~84 정수를  이용하여 벡터 생성
    단계2 : 벡터를 대상으로 7x3x4 구조의 3차원 배열로 모양 변경
    단계3 : 3차원 배열을 대상으로 (행,면,열) 축의 순서로 구조 변경
'''

import numpy as np

# 1. vector 생성 
data = np.arange(1, 85)

# 2. 3차원 배열 
data2 = data.reshape(7,3,4)

# 3. transpose(행,면,열)
data3 = data2.transpose(1,0,2)
data3
