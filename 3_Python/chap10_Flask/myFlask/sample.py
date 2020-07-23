import flask
from flask import Flask
print(flask.__version__)  # 1.1.2

# flask application
app = Flask(__name__)  # 생성자 -> object(app)

# 함수 장식자 : 사용자 요청 url -> 함수 호출
@app.route('/')  # 기본url : http://localhost/
def hello():
    return "hello flask~"  # 반환값

# 프로그램 시작점
if __name__ == "__main__":
    app.run()  # application 실행
    # http://127.0.0.1:5000/ : 시작 url 생성  # 서버가 동작 중이다 # 끝내라 할 때까지
















