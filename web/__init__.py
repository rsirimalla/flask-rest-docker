from flask import Flask, jsonify
import requests
import socket
import os

app = Flask(__name__)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

service_endpoint = os.environ['SERVICE_ENDPOINT']


@app.route('/')
def hello_world():
    return jsonify(
        message='Hello world',
        host=hostname,
    )


@app.route('/service')
def service():
    response = requests.get('http://{}/response'.format(service_endpoint))
    return response.json()


@app.route('/response')
def response():
    return jsonify(
        message='Hello from service',
        host=hostname,
    )
