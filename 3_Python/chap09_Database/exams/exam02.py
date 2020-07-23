'''
문제2) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 전자레인지 2 350000
4 HDTV 2 1500000
전체 레코드 수 : 4

    [ 상품별 총금액 ]
냉장고 상품의 총금액은 1,700,000
세탁기 상품의 총금액은 1,650,000
전자레인지 상품의 총금액은 700,000
HDTV 상품의 총금액은 3,000,000
'''

import sqlite3

try :
    conn = sqlite3.connect("./chap09_database/data/sqlite.db")
    cursor = conn.cursor()
    cursor.execute("select * from goods")
    dataset = cursor.fetchall()
    for row in dataset:
        # print(row[0], row[1], row[2], row[3])
        print("%d       %s       %d       %d"%(row))
    print('전체 레코드 수 :', len(dataset))

    print('[ 상품별 총금액 ]')
    for row in dataset:
        price = row[2] * row[3]
        print("%s 상품의 총금액은 "%row[1], format(int(price), '3,d'))


except Exception as e :
    print('db 연동 오류 :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

