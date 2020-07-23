'''
선택자(selector)
 - 보통 웹문서 디자인(css)에서 사용되는 용어
 - 선택자 : id(#) : 중복불가, class(.) : 중복가능
 - html.select('선택자')      : 여러 엘리먼트 수집
 - html.select_one('선택자')  : 한 개의 엘리먼트 수집
'''
from bs4 import BeautifulSoup

file = open("./chap08_crawling/data/html03.html", encoding='utf-8')
src = file.read()
print(src)

html = BeautifulSoup(src, 'html.parser')

# 태그 & 선택자 -> element 수집

# 1) id 선택자 : #
table = html.select_one("#tab")  # id = 'tab'
print(table)  # 저 태그가 달린 블록 전체를 가져옴  : <table> ~~ </table>

## <table>태그 안에 <tr> <th> <td> 이런 애들이 있는데,
## 점마들을 골라서 데려오고 싶다 : th를
ths = html.select("#tab > tr > th")  # find_all 하면 list로 반환했듯이 얘도 이러함
print(ths)
print(len(ths))  # 4
# content 조회
for th in ths:
    print(th.string)
'''
 학번 
 이름 
 학과 
 이메일 
'''

# 2) class 선택자 : .
trs = html.select("#tab > .odd")  # 5<tr> -> 2<tr>
print(trs)  # ,를 기준으로 2개의 원소(엘리먼트) 수집

for tr in trs:
    # print(tr)
    tds = tr.find_all('td')  # list
    for td in tds:
        print(td.string)
'''
 201602 
 이순신 
 해양학과 
 lee@naver.com 
 201604 
 유관순 
 유아교육 
 you@naver.com 
'''
## 위와 같이 계층적으로 접근하기보단 직접적으로 찾고싶다
# 3) tag[속성='값'] 찾기
trs = html.select("tr[class='odd']")  # ""와 ''를 안밖으로 혼용해야함, 일괄되게 쓰면 안됨
print(trs)
'''
[<tr class="odd"> <!-- 3행(홀수) -->
<td> 201602 </td>
<td> 이순신 </td>
<td> 해양학과 </td>
<td> lee@naver.com </td>
</tr>, <tr class="odd"> <!-- 5행 -->
<td> 201604 </td>
<td> 유관순 </td>
<td> 유아교육 </td>
'''
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.string)
'''
 201602 
 이순신 
 해양학과 
 lee@naver.com 
 201604 
 유관순 
 유아교육 
 you@naver.com 
'''

















