'''
tag명으로 찾기
형식)
html.find('tag')     : 최초로 발견된 tag 수집
html.find_all('tag') : 해당 tag 전체 수집

'''
from bs4 import BeautifulSoup
# 1. 로컬 파일 불러오기
file = open("./chap08_crawling/data/html01.html", mode='r', encoding='utf-8')
src = file.read()
print(src)

# 2. src -> html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. tag 찾기 -> 내용 추출
# html 문서도 계층적 구조로 만들어졌다

## 1) tag
h1 = html.html.body.h1  # <h1>
print(h1)          # 엘리먼트 : <h1> 시멘틱 태그 ?</h1>
print(h1.string)   # 내용 :  시멘틱 태그 ?
## 복잡한 편이라 이런 방법도 있다는 참고용임

## 2) find('tag')
h2 = html.find('h2')
print(h2)           # 엘리먼트 : <h2> 주요 시멘틱 태그 </h2>
print(h2.string)    # 주요 시멘틱 태그

## 3) find_all('tag')  # list
lis = html.find_all('li')
print(lis)
print(len(lis))  # 5개의 리스트

for li in lis:
    print(li.string)   #lis는 리스트자체이기에 스트링멤버를 못 붙이지
''' 
 header : 문서의 머리말(사이트 소개, 제목, 로그 )
 nav : 네이게이션(메뉴) 
 section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그
 aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) 
 footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) 
'''
li_cont = [li.string for li in lis]
print(li_cont)  # 5원소의 리스트, 원소 : 엘리먼트의 내용










