'''
sqlite3
 - 내장형 DBMS : 기기 내부에서만 사용 가능
 - 외부 접근 허용 안됨
'''
import sqlite3
print(sqlite3.version_info)  # (2, 6, 0)
print(sqlite3.sqlite_version_info)  # (3, 31, 1)

try:
    # 1. database 생성
    conn = sqlite3.connect("./chap09_database/data/sqlite.db")  # 해당 경로에 db를 만들고, db를 연동할 수 있는 객체를 만든다
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2, table 생성
    sql = """create table if not exists test_tab(name text(10), 
    phone text(15), addr text(50))"""
    cursor.execute(sql)  # 테이블 생성

    # 3. 테이블에 레코드 추가
    '''
    cursor.execute("insert into test_tab values('홍길동', '010-111-1111', '서울시')")
    cursor.execute("insert into test_tab values('이순신', '010-111-1111', '해남시')")
    cursor.execute("insert into test_tab values('유관순', '010-111-1111', '충남시')")
    conn.commit()  # db 반영
    '''
    # 4. 레코드가 추가되었는지 조회
    cursor.execute("select * from test_tab")
    dataset = cursor.fetchall()  # 객체에 저장된 레코드를 가져옴
    for row in dataset:
        print(row)  # 튜플
    print("이름\t\t전화번호\t\t주소")
    for row in dataset:
        print(row[0]+'\t'+row[1]+'\t'+row[2])

except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()  # 이전 쿼리 실행 취소
finally:
    cursor.close()
    conn.close()
# 오류는 뜨지 않았고 data폴더에 db가 생성됨
# ('홍길동', '010-111-1111', '서울시')
# ('이순신', '010-111-1111', '해남시')
# ('유관순', '010-111-1111', '충남시')
# 이름		전화번호		    주소
# 홍길동	010-111-1111	서울시
# 이순신	010-111-1111	해남시
# 유관순	010-111-1111	충남시




















