
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

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/app05/main.html")

@app.route('/docForm')
def docForm():
    return render_template("/app05/docForm.html")

@app.route('/docPro', methods=['GET', 'POST'])
def docPro():
    if request.method == 'POST':
        doc_id = int(request.form['id'])
        major = request.form['major']

        conn, cursor = db_conn()
        sql = f"""select * from doctors where doc_id = {doc_id}
                  and major_treat = '{major}'"""
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:  # 로그인 성공 확인 -> 진료 정보
            # print('lonin 성공') : 601 + 내과인 양반의 진료정보를 가져오자
            sql = f"""select d.doc_id, t.treat_id, t.treat_contents, t.tread_date
                  from doctors d inner join treatments t
                  on d.doc_id = t.doc_id and d.doc_id = {doc_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                for row in data:
                    print(row)
                size = len(data)
            else:
                size = 0

            return render_template("/app05/docPro.html", dataset=data)

        else:    # 로그인 실패
            return render_template("/app05/error.html", info="id 또는 진료과목 확인")

@app.route('/nurseForm')
def nurseForm():
    return render_template("/app05/nurseForm.html")

@app.route('/nursePro', methods=['GET', 'POST'])
def nursePro():
    if request.method == 'POST':
        id = int(request.form['id'])

        conn, cursor = db_conn()
        sql = f"select * from nurses where nur_id = {id}"
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:  # 로그인 성공 확인 -> 진료 정보
            sql = f"""select n.nur_id, p.doc_id, p.pat_name, p.pat_phone
                  from nurses n inner join patients p
                  on n.nur_id = p.nur_id and n.nur_id = {id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                for row in data:
                    print(row)
                size = len(data)
            else:
                size = 0

            return render_template("/app05/nursePro.html", dataset=data, size=size)

        else:    # 로그인 실패
            return render_template("/app05/error.html", info="id 또는 진료과목 확인")

if __name__ == "__main__":
    app.run()