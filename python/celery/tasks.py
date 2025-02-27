import traceback

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    traceback.print_stack()
    return x + y
