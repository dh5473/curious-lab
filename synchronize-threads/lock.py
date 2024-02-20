from threading import Lock, Thread

lock = Lock()
total = 0


def add_one():
    global total

    lock.acquire()
    total += 1
    lock.release()


def add_two():
    global total

    lock.acquire()
    total += 2
    lock.release()


threads = []

for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for thread in threads:
    thread.join()

print(total)