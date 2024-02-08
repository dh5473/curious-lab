import requests
import time


def print_task(seconds):
    print("Starting task")
    for num in range(seconds):
        print(num, ".Hello World!")
        time.sleep(1)
    print("Task completed")


def print_numbers(seconds):
    print("Starting num task")
    for num in range(seconds):
        print(num)
        time.sleep(1)
    print("Task to print_numbers completed")


def count_words_at_url(url):
    time.sleep(10)
    response = requests.get(url)
    return len(response.text.split())
