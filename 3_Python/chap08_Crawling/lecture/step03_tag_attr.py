'''
tag 속성과 내용
 - 엘리먼트 : 태그 + 태그의속성 + 내용
   ex) <a href='www.naver.com">네이버</a>
        a : 태그
        href : 속성(attribute)
        네이버 : 내용(content)
'''
from bs4 import BeautifulSoup
# 1. 로컬파일 가져오기
file = open("./chap08_crawling/data/html02.html", encoding='utf-8')
src = file.read()

# 2. 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

help(BeautifulSoup)
# 3. a태그 엘리먼트 가져오기
links = html.find_all('a')  # 리스트로 받음
print(links)

# 4. a태그의 속성(href(5개), target(1개)) 가져오기
urls = []
for link in links:
    print(link.string)  # 태그의 내용 : 네이버
    atts = link.attrs
    print(atts)   # <a href="www.naver.com">네이버</a>  태그의 속성 : {'href': 'www.naver.com'} : {속성=키 : 속성의 내용} dict
    print(atts['href'])  # 키를 넣어서 값을 보겠다 : 링크만 조회하겠다
    urls.append(atts['href'])
    try:
        print(atts['target'])  # 그냥 이 문장만 치면 에러가 뜸 : 모든 태그에 target이 없지 : try 써야함
    except Exception as e:
        print('예외발생 :', e)
print(urls)
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']
# 이렇게 하면 어따쓰노?
# step01에서 url 들어가서 뭔 짓을 했는지 다시 살펴보자
# 이렇게 따와가지고 그 페이지의 정보를 수집하는 거다
print(len(urls))  # 5

# 문제) 저 중에 잘못된 링크가 있음
# urls -> 정상 url -> new_urls
import re  # findall, match, sub
new_urls = [re.match("http://www.[a-z]{1:}.[a-z]{1:}", url) for url in urls]
print(new_urls)
# 이렇게 하면 조건이 참인지 아닌지만 들어가게 되지

# 교수님 코딩1
new_urls = []
for url in urls:
    tmp = re.findall('^http://', url)
    if tmp:
        new_urls.append(url)
print(new_urls)

# 교수님 코딩2
new_urls = []
for url in urls:
    tmp = re.match('^http://', url)
    if tmp:
        new_urls.append(url)
print(new_urls)










