from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import random

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')
CPU_INTENSIVE_COUNT = Counter('cpu_intensive_operations_total', 'Total CPU intensive operations')

@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return 'Hello! This is a demo app for HPA testing.\n'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/load')
def cpu_intensive():
    REQUEST_COUNT.inc()
    CPU_INTENSIVE_COUNT.inc()
    for i in range(10000):
        random.random()
    return 'CPU intensive task completed!\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2025)