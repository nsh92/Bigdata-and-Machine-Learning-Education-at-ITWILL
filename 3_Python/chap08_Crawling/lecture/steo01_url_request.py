'''
원격 서버의 웹문서 수집
'''
from bs4 import BeautifulSoup  # sourece -> html 파싱
import urllib.request as res   # 별칭 : 원격 서버 파일 요청

url = "http://www.naver.com/index.html"

# 1. 원격 서버 url 요청
req = res.urlopen(url)  # 요청 -> 응답
print(req)  # object at 0x00000125B6BB0E48
data = req.read()  # source
print(data)  # <!doctype html> -> source

# 2. source(문자열) -> html 형식 : html 파싱
# 웹페이지에서 마우스 우클릭 페이지 소스 보기 참고
src = data.decode('utf-8')
print(src)
html = BeautifulSoup(src, 'html.parser')  # 생성자 # source -> html
print(html)

# 3. Tag 내용
link = html.find('a')  # <a href='url'>내용</a> 이 단위를 묶어서 엘리먼트라 함
print(link)  # 가장 먼저 발견된 엘리먼트 : find와 find_all의 차이임
'''
element : <시작태그 속성명='값'> 내용 </종료태그>
'''
print('a 태그내용 :', link.string)  # 태그 내용 추출

## data의 로컬상의 웹페이지를 써보자 : step02
























