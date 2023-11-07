import flask

app=flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("lecture.html")

@app.route("/sugang")
def sugang():
    return flask.render_template("sugang.html")

@app.route("/student")
def student():
    return flask.render_template("student.html")

@app.route("/teacher")
def teacher():
    return flask.render_template("teacher.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)