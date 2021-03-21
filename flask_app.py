from flask import Flask, escape, request, session

'''
开启调试模式，运行flask：
 $env FLASK_ENV=development FLASK_APP=flask_app.py flask run
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
