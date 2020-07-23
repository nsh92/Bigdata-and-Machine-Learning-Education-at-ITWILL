# -*- coding: utf-8 -*-

'''
# 1. pickle file 읽기 : 뉴스 크롤링해서 피클로 저장시켜놓은거
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
file = open('../data/news_data.pck', mode='rb')
new_data = pickle.load(file)
new_data
type(new_data) # list
len(new_data)

## docs -> sentence
ex_sent = [kkma.sentences(sent)[0] for sent in new_data]
ex_sent # 리스트 반환

len(ex_sent)

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

# 4. WordCloud
## 1) top50 word
from collections import Counter # class
word_count = Counter(nouns_count)
word_count.most_common(50) 

## 2) word cloud
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=800, height=600,
          max_words=100, min_font_size=4, max_font_size=200,
          background_color='white')

wc_result = wc.generate_from_frequencies(dict(word_count))
import matplotlib.pyplot as plt
plt.imshow(wc_result)
plt.axis('off')
plt.show()

# 진자 -> 확진자 : 수작업이 필요하긴 하다
nouns_count['확진자'] = nouns_count['진자']
del nouns_count['진자']
# 4번부터 다시 돌리면 됨












































