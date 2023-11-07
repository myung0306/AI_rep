"""
Flask : 파이썬으로 작성된 마이크로 웹 프레임워크
Apache : 아파치 소프트웨어 재단에서 관리하는 오픈 소스, HTTP 웹서버 소프트웨어
Tomcat : 아파치 소프트웨어 재단에서 개발한 서블릿 컨테이너(또는 웹 컨테이너)만 있는 웹 애플리케이션 서버
"""
import flask

app=flask.Flask(__name__)

@app.route("/")
def index():
    return """
<html>
    <head>
        <title>강의 목록</title>
    </head>
    <body>
        <h1>현재 진행중인 강의 목록입니다.</h1>
        <!-- link -->
        <a href="/sugang">강의 수강 정보<a>로 이동<br/>
        <a href="/student">학생 목록<a>로 이동<br/>
        <a href="/teacher">강사 목록<a>로 이동
    </body>
</html>
"""

@app.route("/sugang")
def sugang():
    return"""
<html>
    <head>
        <title>강의 수강 정보</title>
    </head>
    <body>
        <h1>현재 강의 수강 정보 입니다.</h1>
        <!-- link -->
        <a href="/">강의 목록<a>으로 이동
    </body>
</html>
"""

@app.route("/student")
def student():
    return"""
<html>
    <head>
        <title>학생 목록</title>
    </head>
    <body>
        <h1>현재 학생 목록 입니다.</h1>
        <!-- link -->
        <a href="/">강의 목록<a>으로 이동
    </body>
</html>
"""

@app.route("/teacher")
def teacher():
    return"""
<html>
    <head>
        <title>강사 목록</title>
    </head>
    <body>
        <h1>현재 강사 목록 입니다.</h1>
        <!-- link -->
        <a href="/">강의 목록<a>으로 이동
    </body>
</html>
"""
    
if __name__=="__main__":
    """
    debug가 활성화 된 상태면 app.py 저장시 자동으로 변경
    debug가 비활성화 된 상태면 app.py를 재실행 해야 변경
    """
    app.run(host='0.0.0.0', port=8000, debug=True)