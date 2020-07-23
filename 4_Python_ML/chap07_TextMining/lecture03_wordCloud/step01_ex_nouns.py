# -*- coding: utf-8 -*-
'''
# 1. text file 읽기
# 2. 명사 추출 : kkma
# 3. 전처리 : 단어 길이 제한, 숫자 제외
# 4. WordCloud
'''
from konlpy.tag import Kkma
from wordcloud import WordCloud # class
help(WordCloud)

# object 생성
kkma = Kkma()

# 1. text file 읽기
file = open('../data/text_data.txt', mode='r', encoding='utf-8')
docs = file.read()
docs

## docs -> sentence
ex_sent = kkma.sentences(docs) 
ex_sent # 리스트 반환
'''
['형태소 분석을 시작합니다.',
 '나는 데이터 분석을 좋아합니다.',
 '직업은 데이터 분석 전문가 입니다.',
 'Text mining 기법은 2000대 초반에 개발된 기술이다.']
'''
len(ex_sent) # 4

## docs -> nouns
ex_nouns = kkma.nouns(docs)
ex_nouns
len(ex_nouns) # 13 # 출현한 빈도를 세야 하는데, 여기까지는 어떤 단어들이 있는지만 조회됨


# 2. 명사 추출 : Kkma
nouns_word = []
for sent in ex_sent:
    for noun in kkma.nouns(sent): # 문장 -> 명사
        nouns_word.append(noun)
nouns_word # 이래되야 카운트를 하재
len(nouns_word) # 13 -> 15


# 3. 전처리 : 단어 길이 제한(1음절), 숫자 족치기
from re import match
nouns_count = {}
for noun in nouns_word:
    if len(noun) > 1 and not(match('^[0-9]', noun)):
        # key[noun] = value[출현빈도수]
        nouns_count[noun] = nouns_count.get(noun,0) + 1

nouns_count
'''
{'형태소': 1,
 '분석': 3,
 '데이터': 2,
 '직업': 1,
 '전문가': 1,
 '기법': 1,
 '초반': 1,
 '개발': 1,
 '기술': 1}
'''


# 4. WordCloud
## 1) top5 word
from collections import Counter # class
word_count = Counter(nouns_count)
word_count.most_common(5) # [('분석', 3), ('데이터', 2), ('형태소', 1), ('직업', 1), ('전문가', 1)]

## 2) word cloud
help(WordCloud)
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100, min_font_size=4, max_font_size=150,
          background_color='white')

wc_result = wc.generate_from_frequencies(dict(word_count))
import matplotlib.pyplot as plt
plt.imshow(wc_result)
plt.axis('off')
plt.show()




















