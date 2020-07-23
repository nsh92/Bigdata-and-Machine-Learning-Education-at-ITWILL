'''
1. templates 파일 작성
 - 사용자 요청과 서버의 응답을 작성하는 html file
2. static 파일 작성
 - static : 정적 파일 : 이미지, 자바스크립트(동적 기능), css(디자인) 등
'''
from flask import Flask, render_template
# render_template : html 페이지 호출 기능

# flask application
app = Flask(__name__)

# 함수 장식자
@app.route('/') # 시작 url : http://127.0.0.1:5000/
def index():    # 호출 함수
    return render_template('/app01/index.html')  # 호출 html 페이지

@app.route('/info')  # http://127.0.0.1:5000/info
def info():
    return render_template('/app01/info.html')
    # 저 페이지에 들어가서 해당 주소에 info를 뒤에 붙이면 해당하는 html로 감

# 프로그램 시작점 # 서버의 동작 : 빨간 중지 버튼을 누르지 않으면 계속 가동중임
if __name__ == "__main__":
    app.run()

# html 파일끼리의 연결을 구현함























































