from functools import wraps
from threading import Timer 


def coroutine(f):

    @wraps(f)
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap


class Scheduler:
    def __init__(self, pool_size=10):
        self._pending = []
        self._running = {}
        self.pool_size = pool_size
        self.ready = ''
        self._completed = {}
        self.result = None
        self.error = None
        self.executor = self._executor()

    def schedule(self, *tasks):
        for task in tasks:
            if len(self._pending) + len(self._running) > self.pool_size:
                raise ValueError('Queue full')

            task.scheduler = self

    def run(self):
        pass
    
    def _executor():
        pass

    def restart(self):
        pass

    def stop(self):
        pass
