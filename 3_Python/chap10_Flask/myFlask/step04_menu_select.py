'''
get vs post
 - 파라미터 전송 방식
 - get : url에 노출(소량의 데이터, 중요하지 않은)
 - post : body에 포함되어 전송(대량)

 <작업순서>
 1. index 페이지 : 메뉴 선택(radio or select) -> get 방식
 2. flask server 파라미터 받기(메뉴 번호)
 3. 메뉴 번호에 따라서 각 페이지 이동

9장 연습문제3 그대로 but 무한루프 및 프로그램종료 버튼은 안 필요
'''
# db 연결 객체 생성 함수
def db_conn():
    import pymysql

    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True}

    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor

def select_func():
    sql = "select * from goods"
    conn, cursor = db_conn()  # db 연동 객체
    cursor.execute(sql)
    data = cursor.fetchall()
    '''
    for row in data:
        print(row[0], row[1], row[2], row[3])
    print('전체 레코드 수 :', len(data))
    '''
    cursor.close()
    conn.close()
    return data

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/app04/index.html")

@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'GET':
        menu = int(request.args.get('menu'))  #url에 더 많은 변수가 연결(&)되어있으면 이런 문장이 더 추가되어야겠지
        # print('menu :', menu)

    if menu == 1:  # 전체 레코드 조회
        data = select_func()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)

    if menu == 2:  # 레코드 삽입
        return render_template("/app04/insert_form.html")

    if menu == 3:  # 레코드 수정
        return render_template("/app04/update_form.html")

    if menu == 4:  # 레코드 삭제
        return render_template("/app04/delete_form.html")

# 레코드 삽입
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    try:  # 입력창에서 오류 발생 가능하니깐(숫자창에 문자입력, 중복코드 입력 등)
        if request.method == 'POST':
            code = int(request.form['code'])
            name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            conn, cursor = db_conn()
            sql = f"insert into goods values({code}, '{name}', {su}, {dan})"  # name에 ''표시 강조
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", error_info=e)  # 여기선 에러를 위한 페이지를 팠음

# 레코드 수정
@app.route('/update', methods=['GET', 'POST'])
def update():
    try:  # 입력창에서 오류 발생 가능하니깐(숫자창에 문자입력, 중복코드 입력 등)
        if request.method == 'POST':
            code = int(request.form['code'])
            #name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            conn, cursor = db_conn()
            sql = f"update goods set su = {su}, dan = {dan} where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", error_info=e)  # 여기선 에러를 위한 페이지를 팠음

# 레코드 삭제
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    try:
        if request.method == 'GET':
            code = int(request.args.get('code'))
            conn, cursor = db_conn()
            sql = f"delete from goods where code = {code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", error_info=e)  # 여기선 에러를 위한 페이지를 팠음


if __name__ == "__main__":
    app.run()


