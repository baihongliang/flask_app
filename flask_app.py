from flask import Flask, escape, request, session

'''
开启调试模式，运行flask：
 $env FLASK_ENV=development FLASK_APP=flask_app.py flask run
 env FLASK_APP=flask_app.py flask run
 
 终端发起请求：
baihongliang@localhost ~ % curl -XPOST 'http://127.0.0.1:5000/login?username=xiaoming&password=1234'
baihongliang@localhost ~ % curl -XPOST 'http://127.0.0.1:5000/login?username=xiaoming&password=1234' -d "c=1"
'''
app = Flask(__name__)
app.secret_key = "dsfsdf"


@app.route('/')
def hello():
    name = request.args.get("name", "world")
    return f'Hello, {escape(name)}'


@app.route('/login', methods=['get', 'post'])
def login():
    res = {
        "method": request.method,
        "url": request.path,
        "args": request.args,
        "form": request.form
    }
    session['username'] = request.args.get("name")

    return res
