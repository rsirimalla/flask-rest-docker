from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user')
def user():
    return jsonify(
        username='Axl',
        email='axl@darknet.com',
        id=666
    )
