from uuid import uuid4
from typing import Generator
from threading import Timer, Thread
from multiprocessing import Process
from logger import get_logger
from datetime import datetime   


logger = get_logger('root')


class Job:
    def __init__(
            self,
            task :str,
            args :tuple=(),
            kwargs :dict={},
            uid: str='',
            execution_duration=None,
            start_time='',
            number_of_restarts: int = 0,
            depended: list = None

    ) -> None:
        self.uid = uuid4().hex
        self._args = args or ()
        self._kwargs = kwargs or {}
        self.task = task(*self._args, **self._kwargs)
        self.execution_duration = execution_duration
        self.start_time = start_time
        self.number_of_restarts = number_of_restarts
        self.depended = depended or []
        self.worker = None

    @staticmethod
    def start_job(job: 'Job') -> None:
        task_name = job.task.__name__
        start_at = job.start_time
        if job.start_time and job.start_time > datetime.now():
            total_second = (job.start_time - datetime.now())
            worker = Timer(total_second, job.task)
            worker.start()
            logger.info('Задача "%s" остановлена.', task_name)
        else:
            worker = Thread(target=job.task)
            worker.start()
            worker.join()
            logger.info('Задача "%s" выполнена успешно.', task_name)
        job.worker = worker

    @staticmethod
    def run(self):
        while job := (yield):
            try:
                Job.start_job(job)
            except GeneratorExit:
                logger.info('Метод start_job() остановлен.')
                raise
            except Exception as err:
                logger.error(err)
                while job.number_of_restats > 0:
                    job.number_of_restarts -= 1
                    task_name = job.task.__name__
                    try:
                        Job.start_job(job)
                        logger.info('Задача "%s" успешно завершена.', task_name )
                    except Exception as err:
                        logger.error(err)

    def pause(self):
        if (self.start_at):
            pass

    def stop(self):
        pass
