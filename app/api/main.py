from flask import Flask, jsonify, request
from datetime import datetime
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)
tasks = []

# Prometheus metrics
REQUEST_COUNT = Counter(
    'taskmaster_requests_total',
    'Total request count',
    ['method', 'endpoint', 'status']
)
REQUEST_LATENCY = Histogram(
    'taskmaster_request_latency_seconds',
    'Request latency in seconds',
    ['endpoint']
)
TASK_COUNT = Gauge(
    'taskmaster_tasks_total',
    'Total number of tasks'
)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    latency = time.time() - request.start_time
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).observe(latency)
    return response

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "taskmaster-api",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks, "count": len(tasks)})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    }
    tasks.append(task)
    TASK_COUNT.set(len(tasks))
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
