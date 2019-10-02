from flask import Flask, jsonify, request
import requests
import socket
import os

app = Flask(__name__)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

service_endpoint = os.environ.get('SERVICE_ENDPOINT')


@app.route('/')
def hello_world():
    return jsonify(
        message='Hello World',
        host=hostname,
    )


@app.route('/service')
def service():
    headers = {
        "source-system": request.headers.get('source-system'),
        "loan-type": request.headers.get('loan-type'),
    }
    response = requests.get('http://{}/response'.format(service_endpoint), headers=headers)
    return jsonify(response.json())


@app.route('/response')
def response():
    return jsonify(
        message='Hello from service',
        host=hostname,
    )
