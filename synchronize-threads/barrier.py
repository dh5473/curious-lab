from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num = 4
barrier = Barrier(num)
names = ["Dony", "George", "Isabel", "Bin"]


def player():
    sleep(randrange(2, 5))

    name = names.pop()
    print("%s reached the barrier at: %s" % (name, ctime()))
    barrier.wait()


threads = []
print("Race starts now...")

for _ in range(num):
    threads.append(Thread(target=player))
    threads[-1].start()

for thread in threads:
    thread.join()

print()
print("Race over!")