import flask
from value_object import Student

app=flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("lecture.html")

@app.route("/sugang")
def sugang():
    return flask.render_template("sugang.html")

@app.route("/student")
def student():
    students=[]
    for i in range(5):
        students.append(
            Student(f"S{i:07d}", f"학생이름-{i:04d}", 20+i%10, f"학생주소-{i:04d}")
        )
    data={"students":students, "show_footer": True}
    return flask.render_template("student_ex2.html", data=data)

@app.route("/teacher")
def teacher():
    return flask.render_template("teacher.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)