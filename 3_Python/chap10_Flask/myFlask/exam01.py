'''
문) emp 테이블을 대상으로 사원명을 조회하는 application 을 구현하시오.
  조건1> index 페이지에서 사원명을 입력받아서 post 방식 전송
  조건2> 해당 사원이 있으면 result 페이지에 사번, 이름, 직책, 부서번호 칼럼 출력
  조건3> 해당 사원이 없으면 result 페이지에 '해당 사원 없음' 이라고 출력
'''
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/exam01/index.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ename = request.form['ename']
        print('name=', ename)

    import pymysql

    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True}

    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()

        sql = "select * from emp"
        cursor.execute(sql)
        data = cursor.fetchall()

        if data:
            sql = f"select * from emp where ename like '%{ename}%'"
            cursor.execute(sql)
            data2 = cursor.fetchall()
        if data2:
            for row in data2:
                print("%s    %s    %s    %s    %s    %s    %s" % row)
            print('검색된 사원의 수 :', len(data2))
            size = len(data2)
        else:
            print('그런 사원 없음')
            size = 0

    except Exception as e:
        print('db 연동 오류', e)
        conn.rollback()

    finally:
        cursor.close();
        conn.close()
    return render_template("/exam01/result.html", ename=ename, data=data2, size=size)

if __name__ == "__main__":
    app.run()














