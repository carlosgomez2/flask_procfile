import time
import rq
from redis import Redis

redis = Redis(
    host="127.0.0.1",
    port=6379)

queue = rq.Queue(connection=redis)


def worker_task(msg):
    print(time.time())
    print(f'{msg} from worker')


if __name__ == "__main__":
    worker = rq.Worker([queue], connection=redis, name='default')
    worker.work()
