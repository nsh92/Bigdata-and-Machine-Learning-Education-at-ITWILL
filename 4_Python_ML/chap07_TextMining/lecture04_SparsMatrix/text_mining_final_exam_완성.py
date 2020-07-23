'''
TextMining 과제  

 문) movies.dat 파일의 자료를 이용하여 다음과 같이 단계별로 단어의 빈도수를 구하고,
    단어 구름으로 시각화하시오.
'''

import pandas as pd
import numpy as np

# [단계1] 영화 dataset 가져오기  
name = ['movie_id', 'title', 'genres']
movies = pd.read_csv('../data/movies1.dat', sep='::', header=None, names=name )
print(movies.info())
print(movies.head())
print(movies.tail())
print('전체 영화수 : ', len(movies)) # 전체 영화수 :  3883(행)

# [단계2] zero 행렬 만들기[행수 : 전체 영화수, 열수 : 중복되지 않은 장르 수]  
# 힌트 : 중복되지 않은 장르 수 구하기

# 중복되지 않은 장르 수 구하기 
genres = [] # 장르 저장 list
for  genre  in  movies.genres : 
    for g in genre.split("|"): 
        genres.append(g) 
        
genres_unique = pd.unique(genres) # 유일한 장르
len(genres_unique) # 18

# zero 행렬 : numpy
zero = np.zeros( (len(movies), len(genres_unique))  ) 
print(zero)


# [단계3] zero 행렬 -> DataFrame 변환(열 제목 = 장르명) 
# 설명 : zero 행렬을 대상으로 열 이름에 장르명을 지정하여 DataFrame을 생성한다.

dummy = pd.DataFrame(zero, columns = genres_unique)
dummy

# [단계4] 희소행렬(Sparse matrix) 생성 
# 설명 : 각 영화별로 해당 장르에 해당하는 교차 셀에 0 -> 1 교체하여 희소행렬을 만든다.
  
for n, g in enumerate(movies.genres) : 
    dummy.loc[n, g.split("|")] = 1 


# 희소행렬 -> DTM 변경 
DTM = dummy
print(DTM)

# [단계5] 단어문서 행렬(TDM) 만들기 
# 설명 : 희소행렬(Sparse matrix)에 전치행렬을 적용하여 장르명과 영화 index를 교체한다. 
TDM = DTM.T # 전치행렬 
print(TDM)


# [단계6] 장르 빈도수(word count)
# 설명 : 단어문서 행렬(TDM)를 대상으로 행 단위 합계를 계산하여 장르별 출현빈도수를 계산한다. 
movie_count = TDM.sum(axis = 1)
print(movie_count)

# 5) word counter
word_count = dict(movie_count)


# [단계6] 장르 빈도수(word count)
from collections import Counter

word_count = Counter(word_count)
print(word_count)
'''
Counter({'Drama': 1603.0, 'Comedy': 1200.0, 
'Action': 503.0, 'Thriller': 492.0, 'Romance': 471.0, 
'Horror': 343.0, 'Adventure': 283.0, 'Sci-Fi': 276.0, 
"Children's": 251.0, 'Crime': 211.0, 'War': 143.0, 
'Documentary': 127.0, 'Musical': 114.0, 'Mystery': 106.0, 
'Animation': 105.0, 'Fantasy': 68.0, 'Western': 68.0, 
'Film-Noir': 44.0})
'''

# [단계7] 단어 구름 시각화
# 설명 : 장르 빈도수를 Counter 객체를 생성하고, WordCloud 클래스를 이용하여 단어 구름으로 시각화한다.

from wordcloud import WordCloud

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=800, height=600,
          max_words=100,max_font_size=200,
          background_color='white')

wc_result = wc.generate_from_frequencies(dict(word_count)) # dict

import matplotlib.pyplot as plt 
plt.figure(figsize = (12, 8))
plt.imshow(wc_result)
plt.axis('off') # x.y축 눈금 감추기 
plt.show()



