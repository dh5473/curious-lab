import threading

num = 0
lock = threading.Lock()

lock.acquire()
num += 1
lock.acquire()  # block
num += 2
lock.release()


lock = threading.RLock()

lock.acquire()
num += 3
lock.acquire()  # not block
num += 4
lock.release()
lock.release()  # call release once for each call to acquire

print(num)