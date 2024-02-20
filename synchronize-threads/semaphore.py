import random, time
from threading import BoundedSemaphore, Thread

max_items = 5  # default 1 item
container = BoundedSemaphore(max_items)


def producer(nloops):
    for _ in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        
        try:
            container.release()
            print("Produced an item.")
        except ValueError:
            print("Full, skipping.")


def consumer(nloops):
    for _ in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")

        if container.acquire(blocking=False):
            print("Consumed an item.")
        else:
            print("Empty, skipping.")


threads = []
nloops = random.randrange(3, 6)
print("Starting with %s itmes." % max_items)

threads.append(Thread(target=producer, args=(nloops, )))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops + max_items + 2), )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All done.")