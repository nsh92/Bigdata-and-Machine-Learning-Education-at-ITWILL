# -*- coding: utf-8 -*-
"""
뉴스 크롤링 -> 워드 벡터
문장 -> 단어 벡터 -> 희소행렬(Sparse Matrix)
ex) '직업은 데이터 분석가 입니다' -> 직업 데이터 분석가
"""
from konlpy.tag import Kkma
from wordcloud import WordCloud # class
import pickle
from re import match

# object 생성
kkma = Kkma()

# 1. text file 읽기
file = open('../data/news_data.pck', mode='rb')
new_data = pickle.load(file)
new_data
type(new_data) # list
len(new_data)

# 2. docs -> sentence
ex_sent = [kkma.sentences(sent)[0] for sent in new_data]
ex_sent
len(ex_sent)

# 3. 명사 추출 : Kkma : 이전 스텝 복붙 안하고 다시 작성
# 3. sentence -> word vector
sentence_nouns = []  # 단어 벡터 저장
for sent in ex_sent: # 11600
    word_vec = ""
    for noun in kkma.nouns(sent):
        if len(noun) > 1 and not(match('^[0-9]', noun)):
            word_vec += noun + " " # word_vec에 누적시키고 공백으로 구분
    print(word_vec)
    sentence_nouns.append(word_vec)

len(sentence_nouns) # 11600 길이는 그대로
ex_sent[0]          # '의협 " 감염병 위기 경보 상향 제안.. 환자 혐오 멈춰야"'
sentence_nouns[0]   # '의협 감염병 위기 경보 상향 제안 환자 혐오 ' 내용은 명사들로

# 4. file save
file = open('../data/sentence_nouns.pck', mode='wb')
pickle.dump(sentence_nouns, file)

# 5. file load
file = open('../data/sentence_nouns.pck', mode='rb')
word_vector = pickle.load(file)



















