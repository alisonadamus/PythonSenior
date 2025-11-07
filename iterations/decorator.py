def decorator(func):
    def wrapper():
        print("Перед виконанням")
        func()
        print("Після виконання")
    return wrapper

@decorator
def say_hello():
    print("Привіт!")
# decorated = decorator(say_hello)
# decorated()
say_hello()

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} виконалась за {end - start:.5f} сек.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
    print("Готово!")

slow_function()

@timer
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f"[{i}] {result}")

factorial(100)

