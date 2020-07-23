'''
emp join dept
subquery : emp(사원정보) vs dept(부서정보)
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

    '''
    # 1. ANSI표준의 inner join
    sal = int(input("join 급여 : "))
    sql = f"""select e.eno, e.ename, e.sal, d.dname
    from emp e inner join dept d
    on e.dno = d.dno and e.sal >= {sal}"""

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3])
    '''
    '''
    # 2. 서브쿼리 : 부서번호(dept) -> 사원정보(emp)
    dno = int(input("부서번호 입력 : "))
    sql = f"""select eno, ename, hiredate, dno from emp
    where dno = (select dno from dept where dno = {dno})"""

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3])
    print('해당 부서 사원 수 : ', len(data))
    '''
    '''
    # 문) 서브쿼리2 : 사원이름(ename) 입력 -> 어떤 부서에 근무하는지 출력
    name = input("이름을 입력하세요 : ")
    sql = f"""select * from dept
    where dno = (select dno from emp where ename = '{name}')"""
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        for row in data:
            print(row[0], row[1], row[2])
    else:
        print('그런 사람 없습니다')
    '''
except:
    pass
finally:
    cursor.close()
    conn.close()



























