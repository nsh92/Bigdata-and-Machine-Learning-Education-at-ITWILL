# -*- coding: utf-8 -*-
'''
1. news Crawling
    url = http://media.daum.net
2. pickle save
    binary file save
'''
import urllib.request as req
from bs4 import BeautifulSoup

url = 'http://media.daum.net'

# 1. url 요청
res = req.urlopen(url)
src = res.read()  # 소스로 읽어오기
print(src)

# 2. html 파싱
src = src.decode('utf-8')
html = BeautifulSoup(src, 'html.parser')
print(html)
# 기사를 담고 있는 태그가 무엇인지 찾아봄 : <a href> or <class="link_thumb"> or <class="link_txt">

# 3. tag[속성='값'] -> 'a[class="link_txt"]'
## 저 엘리먼트를 수집하겠다
links = html.select('a[class="link_txt"]')
print(len(links))  # 62
print(links)

crawling_data = []  # 빈 리스트 만들기
for link in links:
    link_str = str(link.string)              # 내용 추출
    crawling_data.append(link_str.strip())   # 문장 끝 불용어 처리(\n, 공백)
print(crawling_data)
print(len(crawling_data))  # 62
# 근대 여전히 불용어 좀 있음

# 뽑아냈으니 피클 형식으로 저장해보자
#  : 62개의 원소 및 리스트 형태 그대로 보존하겠다, 그냥 저장하면 원소개념이 무시됨
# 4. pickle file save
import pickle
file = open("C:/ITWILL/3_Python-I/workspace/chap08_Crawling/data/new_crawling.pickle", mode='wb')
pickle.dump(crawling_data, file)
print('피클 저장 완료')







