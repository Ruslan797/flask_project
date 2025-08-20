# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
# @app.route('/hello/<name>')
# def hello(name):
#  return f'Hello, {name}!'
#
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, jsonify
from app_exemple_01 import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user: User = User(**data)
        return jsonify(user.model_dump()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/reverse/<path:text>')
def reverse_text(text):
    return f'{text} reversed is {text[::-1]}'


if __name__ == '__main__':
    app.run(debug=True)