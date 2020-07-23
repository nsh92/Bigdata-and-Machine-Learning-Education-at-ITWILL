# -*- coding: utf-8 -*-
'''
# 문) 2019년11월 ~ 2020년2월 까지(4개월) daum 뉴스기사를 다음과 같이 크롤링하고, 단어구름으로 시각화 하시오.
# <조건1> 날짜별 5개 페이지 크롤링
# <조건2> 불용어 전처리 
# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
'''
import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup
from konlpy.tag import Kkma
from wordcloud import WordCloud
from re import match

# 학생들이 카페에 올릴 예정





