'''
1. pickle file load
2. 텍스트 전처리
3. word count
'''
import pickle

# 1. pickle file load
file = open("./chap08_Crawling/data/new_crawling.pickle", mode='rb')
news_crawling = pickle.load(file)  # 리스트
print(type(news_crawling))  # <class 'list'>
print(news_crawling)  # 저장하기 전의 모습 그대로 나옴

# 2. 텍스트 전처리
def clean_text(texts):
    from re import sub  # gsub() 유사함
    # 1. 소문자 변경
    texts_re = texts.lower()
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장 부호 제거
    punc_str = '[,.<>/?;:!@#$%^&*()]'
    text_re3 = sub(punc_str, '', texts_re2)
    # 4. 공백 제거
    text_re4 = ' '.join(text_re3.split())
    return text_re4

clean_news = [clean_text(news) for news in news_crawling]
print(clean_news)

# 3. word count
word_count = {}  # 빈 set 생성
for texts in clean_news:
    for word in texts.split():
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)

word_count2 = word_count.copy()  # 사본 생성(객체 복제)
# 2음절 이상 단어 선택
for word in word_count.keys():
    if len(word) < 2:
        del word_count2[word]

print(word_count2)  # dict

# 5. top10, top5 선정
'''
pip install collections-extended
'''
from collections import Counter
count = Counter(word_count2)
del count['none']
del count['[바로잡습니다]']

top5 = count.most_common(5)  # 탑5
print(top5)
top10 = count.most_common(10)
print(top10)

# list[(),()]
import pandas as pd
top10_df = pd.DataFrame(top10, columns=['word', 'count'])
print(top10_df)
'''
    word  count
0    코로나      4
1     지급      3
2     수출      3
3     고용      3
4     소득      3
5   기여도는      3
6     만원      3
7    이사장      3
8    트럼프      3
9  재난지원금      2
'''

'''
pip install matplotlib
'''
# 차트를 그리고 싶다
import matplotlib.pyplot as pl

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

pl.plot(top10_df['word'], top10_df['count'])  # (x, y)
pl.title('top10 word count')
pl.show()
# 기능은 여기이나, 그냥 하면 한글이 깨짐 : 저기 폰트 어쩌구가 한글이 나오게끔 함

# 막대그래프
pl.bar(top10_df['word'], top10_df['count'])
pl.title('top10 word count')
pl.show()

