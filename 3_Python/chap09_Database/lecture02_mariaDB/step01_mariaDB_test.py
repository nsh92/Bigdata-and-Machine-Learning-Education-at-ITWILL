'''
마리아DB 연동 TEST
'''
import pymysql
print(pymysql.version_info)  # (1, 3, 12, 'final', 0) 버전정보가 출력됨 : 정상

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    # 1. db 연동 객체
    conn = pymysql.connect(**config)  # 가변인수를 넣겠다 : ** 함수파트에서 했었음 : 인증과정임
    # 2. sql 실행 객체
    cursor = conn.cursor()

    # 3. table 생성, 재생성
    sql = """create or replace table goods(
    code int primary key,
    name varchar(30) not null,
    su int not null,
    dan int not null
    )"""
    cursor.execute(sql)

    # 4. 레코드 추가
    cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    cursor.execute("insert into goods values(3, '전자레인지', 2, 350000)")
    cursor.execute("insert into goods values(4, 'HDTV', 2, 1500000)")
    conn.commit()

    # 5. slq문 실행
    sql = "select * from goods"
    cursor.execute(sql)
    dataset = cursor.fetchall()
    for row in dataset :
        print(row[0], row[1], row[2], row[3])
    print('전체 레코드 수 :', len(dataset))

except Exception as e:
    print('db 연동 error :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()











