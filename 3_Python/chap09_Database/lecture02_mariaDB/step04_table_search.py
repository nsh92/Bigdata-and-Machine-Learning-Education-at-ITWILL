'''
table 전체 조회 -> 생성 및 조회
1. 없는 경우 : table 생성
2. 있는 경우 : table 조회
'''
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
    # 1. 전체 테이블 조회
    cursor.execute("show tables")
    tables = cursor.fetchall()

    ## 테이블 유무 조회
    sw = False
    if tables:
        for t in tables:
            # print(t[0])                     # 튜플타입으로 결과값 반환, 이름만 보고싶다 : t[0]
            if t[0] == 'emp':
                sw = True

    if sw == False:                           # 없으면 테이블을 만들고 레코드 삽입해라
        sql = """create or replace table emp(
        eno int auto_increment primary key,
        ename varchar(20) not null,
        hiredate date not null,
        sal int,
        bonus int default 0,
        job varchar(20) not null,
        dno int
        )"""
        cursor.execute(sql)                   # 테이블 생성
        sql2 = "alter table emp auto_increment = 1001"
        cursor.execute(sql2)

        sql3 = "insert into emp(ename, hiredate, sal, bonus, job, dno) values('홍길동', '2010-01-20', 300, 35, '관리자', 10)"
        cursor.execute(sql3)
        sql4 = "insert into emp(ename, hiredate, sal, job, dno) values('강호동', '2015-09-20', 250, '사원', 20)"
        cursor.execute(sql4)
        sql5 = "insert into emp(ename, hiredate, sal,  job, dno) values('유관순', '2020-01-20', 220, '사원', 10)"
        cursor.execute(sql5)
        conn.commit()  # 레코드 3개 추가
        print('emp 테이블 작성 완료')


    else:                                     # 전체 레코드 조회
        sql = "select * from emp"
        cursor.execute(sql)
        data = cursor.fetchall()
        
        for row in data:
            print(row)
        print('전체 레코드 수 :', len(data))

        '''
        # 문제1) 사원 조회 : 키보드(이름) -> 사번, 이름, 부서, 칼럼, 출력 or '없음'
        name = input('검색할 사원명 입력 :')
        sql = f"select eno, ename, dno from emp where ename like '%{name}%'"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data:
            for row in data:
                print(row[0], row[1], row[2])
        else:
            print('해당 사원 없음')
        '''
        '''
        # 문제2) 사원 수정 : 키보드(사번, 급여, 보너스) -> 급여 보너스 수정
        eno = int(input('수정 사번 : '))
        sal = int(input('수정 급여 : '))
        bonus = int(input('수정 보너스 : '))
        sql = f"update emp set sal={sal}, bonus={bonus} where eno={eno}"
        cursor.execute(sql)
        conn.commit()

        cursor.execute(f"select * from emp where eno = {eno}")
        row = cursor.fetchone()
        print(row)
        '''
        '''
        # 문제3) 레코드 삭제 : 키보드(사번) -> 검색(유무) -> 레코드 삭제 or '없음'
        eno = int(input('삭제 사번 입력 :'))
        sql = f"select * from emp where eno = {eno}"
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:
            cursor.execute(f'delete from emp where eno={eno}')
            conn.commit()
            print(str(eno) + ' 레코드 삭제됨')
        else:
            print('해당 사번 없음')
        '''

except Exception as e:
    print('db 연동 오류', e)
    conn.rollback()
finally:
    cursor.close(); conn.close()
































