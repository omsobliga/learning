import multiprocessing

import gevent
from gevent.pool import Pool
from gevent import monkey, sleep
monkey.patch_all()

def report_task(task):
    jobs = []
    for i in range(10):
        jobs.append(gevent.spawn(krun, task))
    gevent.joinall(jobs)

def krun(task):
    while 1:
        gevent.sleep(1)

if __name__ == "__main__":
    plist = []
    pool = multiprocessing.Pool(processes=4)
    for i in range(0,2):
        pool.apply_async(report_task, (i, ))

    pool.close()
    pool.join()
