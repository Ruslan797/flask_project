from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/user/<name>')
def greet_user(name):
    return f"Привет, {name}!"

if __name__ == '__main__':
    app.run(debug=True)