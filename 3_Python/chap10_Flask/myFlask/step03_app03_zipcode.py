'''
<작업순서>
1. index 페이지 작성 -> 동 입력
2. flask server에서 동(파라미터) 받기
3. DB 연동(9장 스텝3 복붙) -> 주소 조회
4. 조회 결과 -> result 페이지 출력
'''
from flask import Flask, render_template, request  # app 생성, 템플릿 호출

app = Flask(__name__)  # object -> app object

# 함수 장식자
@app.route('/')  # 기본 url 요청 -> 함수 호출
def index():
    return render_template("/app03/index.html")

@app.route('/search', methods=['GET', 'POST'])  # url키워드와 받을 방식
def search():
    if request.method == 'POST':
        dong = request.form['dong']
        #print('dong=', dong)   # 이 상태에서 전달이 되는지 확인이 가능해짐(링크페이지에서 실제로 동을 누르고 여기 콘솔에 프린트가 뜨는지의 여부)

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

        # 2. 레코드 조회
        sql = "select * from zipcode_tab"
        cursor.execute(sql)
        data = cursor.fetchall()

        if data:  # True : 전체 레코드 검색
            '''
            for row in data:
                print("[%s]    %s    %s    %s    %s" % row)
            print('전체 레코드 수 :', len(data))
            '''
            ### 1. 동으로 검색
            #dong = input("검색할 동 입력 :")
            sql = f"select * from zipcode_tab where dong like '%{dong}%'"
            cursor.execute(sql)
            data2 = cursor.fetchall()
            if data2:
                for row in data2:
                    print("[%s]    %s    %s    %s    %s" % row)
                print('검색된 동의 수 :', len(data2))
                size = len(data2)
            else:
                print('그런 동 없음')
                size = 0

    except Exception as e:
        print('db 연동 오류', e)
        conn.rollback()

    finally:
        cursor.close();
        conn.close()
    return render_template("/app03/result.html", dong=dong, data=data2, size=size)

# 프로그램 시작점
if __name__ == "__main__":
    app.run()





















