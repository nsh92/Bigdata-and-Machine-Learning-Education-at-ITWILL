'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건> <tr> 태그 하위 태그인 <th> 태그의 모든 내용 출력
    
   <출력 결과>
   th 태그 내용 
    아이디 
    비밀번호 
'''

from bs4 import BeautifulSoup

# 1. 파일 읽기 
file = open("./chap08_crawling/data/login.html", mode='r', encoding='utf-8')
source = file.read()
print(source)

# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')
print(html)

# 3. 태그 찾기 
ths = html.find_all('th')
th = [th.string for th in ths]

# 4. 태그 내용 출력 
print('<출력 결과>')
print('th 태그 내용')
print(th[0])
print(th[1])