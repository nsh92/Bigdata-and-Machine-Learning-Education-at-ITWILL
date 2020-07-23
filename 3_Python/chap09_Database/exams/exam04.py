'''
문제4) emp.csv 파일을 읽어서 다음과 같이 db 테이블에 저장하시오.
 <조건1> 테이블명 : emp_table
 <조건2> 사원 이름으로 레코드 조회(sql문 작성)
 
 <작업순서>
 1. table 생성 : emp_table(sql 폴더) (컬럼 : no(int), name(varchar20), pay(int)
 2. python code : 레코드 추가 
 3. python code : 레코드 조회(사원이름)  
'''

import pandas as pd 

# 칼럼 단위 읽기 
emp = pd.read_csv("./chap09_database/data/emp.csv", encoding='utf-8')
print(emp)
# No Name  Pay
no = emp.No
name = emp.Name
pay = emp.Pay
print(no, name, pay)


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
    '''
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """create or replace table emp_table(
    no int not null,
    name varchar(20) not null,
    pay int)
    """
    cursor.execute(sql)
    print('테이블 작성 완료')
    '''
    sql = "select * from emp_table"
    cursor.execute(sql)
    data = cursor.fetchall()

    if data:
        for row in data:
            print("%s    %s    %s"% row)
        print('전체 레코드 수 :', len(data))

        ename = input("사원 이름으로 레코드 조회")
        sql = f"select * from emp_table where name like '%{ename}%'"
        cursor.execute(sql)
        data2 = cursor.fetchall()
        if data2:
            for row in data2:
                print("%s    %s    %s"% row)
            print('검색된 사원의 수 :', len(data2))
        else:
            print('그런 사원 없음')

    else:
        for i in range(len(no)):
            eno = no[i]; ename = name[i]; epay = pay[i]
            sql = f"""insert into emp_table values(
                {eno}, '{ename}', {epay})"""
            cursor.execute(sql)
            conn.commit()
        print('레코드 추가 성공')

except Exception as e:
    print('db 연동 오류', e)
    conn.rollback()

finally:
    pass