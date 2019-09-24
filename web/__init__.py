from flask import Flask, jsonify
import requests
import socket

app = Flask(__name__)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


@app.route('/')
def hello_world():
    return 'Hello, World from ' + IPAddr


@app.route('/user')
def user():
    return jsonify(
        username='Axl',
        email='axl@darknet.com',
        id=666
    )


@app.route('/aggregate')
def aggregate():
    r1 = requests.get('http://localhost:8080/user')
    r2 = requests.get('http://localhost:8080/user')
    r3 = requests.get('http://localhost:8080/user')
    return jsonify(r1.json(), r2.json(), r3.json())
