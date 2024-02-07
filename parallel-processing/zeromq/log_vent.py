# task ventilator
from log_simulator import generate_log

import zmq
import time

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

logs = []
for _ in range(1000000):
    logs.append(generate_log())

print("Press Enter when the workers are ready: ")
_ = input()
print("Sending tasks to workers...")

sink.send(b'0')

for i in range(1000000):
    sender.send_string(logs[i])

print("All tasks have been sent.")
time.sleep(1)
