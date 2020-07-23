# -*- coding: utf-8 -*-
"""
방법2) url query 이용 : 연도별 뉴스 자료 수집
      ex) 2015.01.01 ~ 2020.01.01
          page : 1 ~ 5
"""
# 360 * 5 = 1800
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd # 시계열을 위하여
# 1. 수집 연도 생성 : 시계열 date 이용
date = pd.date_range("2015-12-01", "2020-01-01")
len(date) # 1827 = 대충 5*365
date[0]  # Timestamp('2015-01-01 00:00:00', freq='D')
date[-1] # Timestamp('2020-01-01 00:00:00', freq='D')

import re # sub('패턴', '제거할거', 대상스트링)
sdate = [re.sub('-', '', str(d))[:8] for d in date]
sdate[:10]
sdate[-10:]


# 2. 크롤러 함수
def newsCrawler(date, pages = 5):  # 가인수의 초기값을 저렇게 지정해도 됨
    one_day_date = []
    for page in range(1, pages+1): # 1~5
        url = f"https://news.daum.net/newsbox?regDate={date}&page={page}"
        try:
            res = req.urlopen(url)
            src = res.read()
            
            src = src.decode('utf-8')
            html = BeautifulSoup(src, 'html.parser')
            
            links = html.select('a[class="link_txt"]')
            
            one_page_data = []
            print('date :', date)
            cnt = 0
            for link in links:
                link_str = str(link.string)
                cnt += 1
                print('cnt :', cnt)
                print('news :', link_str)
                one_page_data.append(link_str.strip())
            one_day_date.extend(one_page_data[:40])
        except Exception as e:
            print('오류 발생 :', e)
    return one_day_date        
        

# 3. 크롤러 함수 호출
year3_news_data = [newsCrawler(date) for date in sdate]
year3_news_data = [newsCrawler(date)[0] for date in sdate] # [1day(1~5p), 2day(1~5p), ....]

































