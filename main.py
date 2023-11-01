from redis import Redis
from flask import Flask, request, jsonify
from rq import Queue
from worker import worker_task


app = Flask(__name__)

redis = Redis(
    host="127.0.0.1",
    port=6379)
queue = Queue(connection=redis)


@app.route("/enqueuer", methods=["POST"])
def index():
    if request.method == "POST":
      msg = "Hello friend!"
      queue.enqueue(worker_task, args=[msg])
      return jsonify({'status': 'ok', 'code': 200})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
