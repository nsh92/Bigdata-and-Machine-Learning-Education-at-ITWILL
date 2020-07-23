
import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    '''
    # Insert
    code = int(input("code :"))
    name = input("name :")
    su = int(input("su :"))
    dan = int(input("dan :"))
    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"  # name에 ''표시 강조
    cursor.execute(sql)
    conn.commit()
    '''
    '''
    # Updata : code -> su, dan 수정
    code = int(input("수정 code :"))
    su = int(input("수정 su :"))
    dan = int(input("수정 dan :"))
    sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
    cursor.execute(sql)
    conn.commit()
    '''
    '''
    # Delete : code -> 유무 -> 삭제 or '코드없음'
    code = int(input("삭제 code :"))
    cursor.execute(f"select * from goods where code = {code}")
    row = cursor.fetchone()
    if row:
        cursor.execute(f"delete from goods where code = {code}")
        conn.commit()
    else:
        print('해당 코드 없음')
    '''
    sql = "select * from goods"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3])
    print('전체 레코드 수 :', len(data))
    '''
    # Read(Select)
    # 상품명 조회
    name = input("조회 상품명 입력 :")
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql)
    data2 = cursor.fetchall()

    if data2:
        for row in data2:
            print(row)
    else:
        print('조회 상품 없음')

    # 상품 코드로 조회
    code = int(input("조회 코드 입력 :"))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    row = cursor.fetchone()  # 검색된 레코드 하나만 반환 : 코드는 primary key이니깐
    if row:
        print(row)
    else:
        print('조회 코드 없음')
    '''


except Exception as e:
    print("db 연동 error :", e)
    conn.rollback()
finally:
    cursor.close(); conn.close()



























