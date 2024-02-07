import time
import random
import datetime
import json


def generate_log():
    log_data = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        "user_id": random.randint(1, 10000),
        "user_info": {
            "gender": random.choice(["male", "female"]),
            "age": random.randint(20, 60),
        },
        "url": random.choice(["/api/buy/items", "/api/cart/items", "/api/signup", "/api/login"]),
        "param": random.choice(["", "cake"]),
        "response_code": random.choice([200, 404, 500])
    }
    return json.dumps(log_data)