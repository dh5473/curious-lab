# task sink
import sys
import time
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

s = receiver.recv()

start_time = time.time()

buy_cnt = 0
for _ in range(1000000):
    s = receiver.recv().decode('utf-8')

    if s == "buy":
        buy_cnt += 1

end_time = time.time()
print()
print(f"Total time: {(end_time - start_time) * 1000} msec")
print(f"Buy count: {buy_cnt}")