from uuid import uuid4
from functools import wraps


# def coroutine(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         gen = f(*args, **kwargs)
#         gen.send(None)
#         return gen
#     return wrap


# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         fib(n - 1) + fib(n - 2)




class Job:
    def __init__(
            self,
            target,
            args: tuple = None,
            __kwargs: dict = None,
            start_at="",
            max_working_time=-1,
            tries=0,
            dependencies=[],
    ) -> None:
        self._id = uuid4
        self.start_at = start_at
        self.max_working_time = max_working_time
        self.tries = tries
        self.dependencies = dependencies
        self.__args = args or ()
        self.__kwargs = __kwargs or {}
        self.coroutine = target(*self.__args, **self.__kwargs)

    def run(self):
        self.coroutine.send()

    def pause(self):
        if (self.start_at):
        

    def stop(self):
        pass
