# -*- coding: utf-8 -*-
"""
TFiDF 단어 생성기 : TfidfVectorizer  
  1. 단어 생성기[word tokenizer] : 문장(sentences) -> 단어(word) 생성
  2. 단어 사전[word dictionary] : (word, 고유수치)
  3. 희소행렬[sparse matrix] : 단어 출현 비율에 의해서 가중치 적용[type-TF, TFiDF]
    1] TF : 가중치 설정 - 단어 출현 빈도수
    2] TFiDF : 가중치 설정 - 단어 출현 빈도수 x 문서 출현빈도수의 역수            
    - tf-idf(d,t) = tf(d,t) x idf(t) [d(document), t(term)]
    - tf(d,t) : term frequency - 특정 단어 빈도수 
    - idf(t) : inverse document frequency - 특정 단어가 들어 있는 문서 출현빈도수의 역수
       -> TFiDF = tf(d, t) x log( n/df(t) ) : 문서 출현빈도수의 역수(n/df(t))
"""

from sklearn.feature_extraction.text import TfidfVectorizer
# 문장 생성
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

# 문장을 넣으면 단어를 뱉는다
# 1. 단어 생성자[word tokenizer]
tfidf = TfidfVectorizer()
tfidf

# 2. 문장 -> 단어 생성
tfidf_fit = tfidf.fit(sentences)
tfidf_fit
vocs = tfidf_fit.vocabulary_
vocs # dict임 {'word': 고유숫자, 'word2': 고유숫자}
len(vocs) # 31 # 고유숫자는 알파벳 순(영문 오름차순)으로 결정됨 : 이를 두고 단어사전이라고도 함
# 그냥 희소행렬은 너무 크니까 실제 데이터가 있는 것만 골라서 '밀도행렬'로 바꾸더라

# 3. 희소행렬
sparse_mat = tfidf.fit_transform(sentences) # [Doc x Term]
type(sparse_mat) # scipy.sparse.csr.csr_matrix : 사이파이 통계관련 객체
sparse_mat # 3x31 sparse matrix of type
sparse_mat.shape # (3, 31) #  3문장, 중복되지 않는 31개의 단어들
print(sparse_mat) # 객체를 그냥 실행시키는 것과 와꾸가 다름
                  # (행의인수, 열의인수)     가중치(weight)(tfidf방식의 가중치, 뭐대충빈도수임)

# 사이파이 -> 넘파이
sparse_mat_arr = sparse_mat.toarray() # 넘파이객체로 바꿔주는 건데 자체적으로 바꿔주는 모듈이 있어서 따로 업로드를 안해도 댐
sparse_mat_arr
sparse_mat_arr.shape # (3, 31)



















