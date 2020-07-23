'''
CRUD
    - Create, Read, Update, Delete
'''
import sqlite3

try:
    # 1. database 생성
    conn = sqlite3.connect("./chap09_database/data/sqlite.db")  # 해당 경로에 db를 만들고, db를 연동할 수 있는 객체를 만든다
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2. 테이블 생성
    sql = """create table if not exists goods(
    code integer primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0)    
    """
    cursor.execute(sql)

    # 3. 레코드 추가
    cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    cursor.execute("insert into goods(code, name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 1500000)")
    conn.commit()  # DB에 반영한다
    '''
    code = int(input('코드 입력 :'))
    name = input('상품명 입력 :')
    su = int(input('수량 입력 :'))
    dan = int(input('단가 입력 :'))
    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit'''

    print('전체 레코드 수 :', len(dataset))

    # 레코드 조회, 조건식 조회
    # cursor.execute("select * from goods where su >= 2")
    # dataset = cursor.fetchall()

    # 5. 레코드 수정
    '''
    sql = "update goods set name = '테스트' where code=4"
    cursor.execute(sql)
    conn.commit()
    '''
    '''
    code = int(input("수정 코드 입력 :"))
    su = int(input('수정 수량 입력 :'))
    dan = int(input('수정 단가 입력 :'))
    sql = f"update goods set su = {su}, dan = {dan} where code={code}"
    cursor.execute(sql)
    conn.commit()
    '''
    '''
    # 키보드 입력 -> 검색
    name = input("검색할 상품명 입력 :")
    cursor.execute(f"select * from goods where name like '%{name}%'")
    dataset = cursor.fetchall()
    if dataset : # True : 검색된 레코드 존재
        for row in dataset:
            print("%d       %s       %d       %d"%(row))
            print('검색된 레코드 수 :', len(dataset))
    else:
        print*("그런거 없다")
    '''
    '''
    # 6. 레코드 삭제
    code = int(input("삭제할 코드 입력 :"))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    dataset = cursor.fetchall()

    if dataset:
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql)
        conn.commit()
    else:
        print("그런거없다")
    '''
    # 4. 레코드 조회
    cursor.execute("select * from goods")
    dataset = cursor.fetchall()
    for row in dataset:
        # print(row[0], row[1], row[2], row[3])
        print("%d       %s       %d       %d"%(row))

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()





















