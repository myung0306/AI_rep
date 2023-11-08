import flask
from database import select_student

app=flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("lecture.html")

@app.route("/sugang")
def sugang():
    return flask.render_template("sugang.html")

@app.route("/student")
def student():
    params = flask.request.args.to_dict()
    limit = int(params.get("limit", 10))
    offset = int(params.get("offset", 0))

    result = select_student(limit, offset)
    data = {"students": result[3], "show_footer": True}
    return flask.render_template("student.html", data=data)

@app.route("/teacher")
def teacher():
    return flask.render_template("teacher.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)