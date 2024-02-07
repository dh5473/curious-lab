# task worker
import sys
import time
import zmq
import json

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

while True:
    log_data = receiver.recv()
    log_parsing_data = json.loads(log_data)
    
    if log_parsing_data["response_code"] == 200:
        event = log_parsing_data["url"].split("/")[2]
        if log_parsing_data["param"] and (event == "buy" or event == "cart"):
            sender.send_string(f"{event}")
        else:
            sender.send_string(f"")
    else:
        sender.send_string(f"")