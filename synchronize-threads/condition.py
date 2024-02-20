import random, time
from threading import Condition, Thread

condition = Condition()
box = []


def producer(box, nitems):
    for _ in range(nitems):
        time.sleep(random.randrange(2, 5))

        condition.acquire()
        num = random.randint(1, 10)
        box.append(num)  # puts an item into box for consumption

        condition.notify()  # notifies the consumer about the availability
        print("Produced:", num)
        condition.release()


def consumer(box, nitems):
    for _ in range(nitems):
        condition.acquire()
        condition.wait()  # blocks until an item is available for consumption
        print("%s: Acquired: %s" % (time.ctime(), box.pop()))
        condition.release()


threads = []
nloops = random.randrange(3, 6)

for func in [producer, consumer]:
    threads.append(Thread(target=func, args=(box, nloops)))
    threads[-1].start()

for thread in threads:
    thread.join()

print("All done.")