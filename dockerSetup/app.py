import socket
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return 'Hello there! I am {}\n'.format(hostname)