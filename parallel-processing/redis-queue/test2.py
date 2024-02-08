from redis import Redis
from rq import Queue
import tasks
import time

queue = Queue(connection=Redis())

if __name__ == "__main__":
    urls = [
        'http://www.google.com',
        'http://www.naver.com',
        'http://www.bing.com',
    ]
    
    jobs = [queue.enqueue(tasks.count_words_at_url, url) for url in urls]
    print(f"{len(jobs)} jobs queued.")


    while not all(job.is_finished for job in jobs):
        time.sleep(1)

    for job in jobs:
        print(f"Result for {job.args[0]}: {job.result}")