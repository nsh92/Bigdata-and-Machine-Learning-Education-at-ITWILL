# -*- coding: utf-8 -*-
"""
news Crawling : url 쿼리 이용
url : http://media.daum.net -> 페이지 하단의 배열이력 클릭
url : https://news.daum.net/newsbox -> 달력 버튼의 5월 5일 클릭
url : https://news.daum.net/newsbox?regDate=20200505 -> 2번 페이지 클릭
url : https://news.daum.net/newsbox?regDate=20200505&page=2
"""
import urllib.request as req
from bs4 import BeautifulSoup
# 1. url 쿼리 만들기
'''
date : 2020.2.1 ~ 2020.2.29
page : 1 ~ 10
'''
## base url + date
base_url = "http://media.daum.net/newsbox?regDate="
date = list(range(20200201, 20200230))

url_list = [base_url+str(d) for d in date] # date는 숫자로 넘어오니 스트링으로

## base url + date + page
page = list(range(1, 11))
pages = ['&page'+str(p) for p in page]

final_url = []
for url in url_list:
    for page in pages:
        final_url.append(url + page)

len(final_url) # 290 = 29일 X 각10page
final_url[0]  # 'http://media.daum.net/newsbox?regDate=20200201&page1'
final_url[-1] # 'http://media.daum.net/newsbox?regDate=20200229&page10'


# 2. 크롤러 함수 정의 step1에서 그대로 퍼오고 약간 수정
def Crawlier(url):
    res = req.urlopen(url)
    src = res.read()
    
    src = src.decode('utf-8')
    html = BeautifulSoup(src, 'html.parser')
    
    links = html.select('a[class="link_txt"]')
    
    one_page_data = []
    cnt = 0
    for link in links:
        link_str = str(link.string)
        cnt += 1
        print('cnt :', cnt)
        print('news :', link_str)
        one_page_data.append(link_str.strip())
    return one_page_data[:40]


one_page_data = Crawlier(final_url[0])  # 함수 자체는 하루치만 크롤링함 : 2020.02.01의 1page
len(one_page_data)  # 134
type(one_page_data) # list
one_page_data[0]   # '의협 "감염병 위기경보 상향 제안..환자 혐오 멈춰야"'
one_page_data[-1]  # '대역전극으로 만든 LG의 상승세, 윌슨 부활투로 이어갈까'
one_page_data[:10] # 각 원소는 ,로 구분되는 리스트 변수들
# 근데, 이렇게 다 돌리면 메인 테마가 아니라 옆의, 아래의 부수적 링크도 수집되니깐
# 의도하는 부분만 하려면 어느 범위(번호)까지인지 구분을 해야 함
one_page_data[:40] # 이 자체를 함수의 리턴 부분에 넣어도 되겠지


## 2월(1개월) 전체 news 수집
month_news = []
page_cnt = 0
# 3. 크롤러 함수 호출
for url in final_url:
    page_cnt += 1
    print('페이지 : ', page_cnt)
    try : # 예외처리 - url 없는 경우
        one_page_news = Crawlier(url)
        # month_news.append(one_page_news) # [[1page], [2page]....] 중첩 리스트로 만들어지겠지
        month_news.extend(one_page_news) # [1page ~ 290page ] 단일 리스트를 의도한다면 이렇게
    except:
        print('해당 url 없음 :', url)
    
len(month_news) # 11600 = 29일 X 10페이지 X 40번


# 4. binary file save
import pickle # 리스트 -> 피클파일 -> 리스트로 로드
file = open('../data/news_data.pck', mode = 'wb')
pickle.dump(month_news, file)
file.close()

file = open('../data/news_data.pck', mode = 'rb')
month_news_crawling = pickle.load(file)
month_news_crawling
file.close()


















